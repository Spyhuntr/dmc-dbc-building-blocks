import boto3
import dash_mantine_components as dmc
import logging
from botocore.exceptions import ClientError
import requests
from zipfile import ZipFile
import io
from dash import html
from typing import List, Union

bucket = 'dmc-dbc-building-blocks'

def card_hdr(title: str, user: str, deps: str):

    link = dmc.Anchor(
        href=f"https://github.com/{user}",
        children=['@' + user],
        size="xs",
        ml="-0.7rem",
        style={'color': 'rgb(134, 142, 150)'})


    menu_items: List[Union[dmc.MenuItem, dmc.MenuLabel]] = [dmc.MenuLabel("Dependencies")]
    for dep in list(deps.split(',')):
        menu_item = dmc.MenuItem(dep)

        menu_items.append(menu_item)

    menu = dmc.Menu([
        dmc.MenuTarget(
            dmc.ActionIcon(
                html.I(className='fas fa-sitemap fa-fw')
            )
        ),
        dmc.MenuDropdown(
            children=menu_items
            
        ),
    ], trigger='hover')

    return dmc.Col(
        children=[
            dmc.Group([
                dmc.Text(
                    title,
                    size="xl"
                ),
                dmc.Text(
                    'Made by',
                    size="xs"
                ),
                link,
                menu
            ]
            )], span=9)


def build_contributors():

    contributors = ['snehilvj', 'tcbegley', 'AnnMarieW', 'Spyhuntr', 'Sohibjon', 'pip-install-python',
                    'amihaiOff', 'BSd3v']
    contrib_group = []
    for contributor in contributors:

        new_link = dmc.Anchor(
            dmc.Tooltip(
                label=contributor,
                withArrow=True,
                transition="pop-top-right",
                transitionDuration=300,
                children=[
                    dmc.Avatar(
                        src=f"https://github.com/{contributor}.png", radius="xl"
                    )
                ]
            ),
            href=f"https://github.com/{contributor}",
            # pl='1rem',
            target='_blank'
        )

        contrib_group.append(new_link)

    return dmc.AvatarGroup(contrib_group)


def create_presigned_post(bucket_name, object_name):
    """Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Dictionary with the following keys:
        url: URL to post to
        fields: Dictionary of form fields and values to submit with the POST
    :return: None if error.
    """

    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3')

    try:
        response = s3_client.generate_presigned_post(bucket_name,
                                                     object_name,
                                                     ExpiresIn=3600)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL and required fields
    return response


def upload_file(contents, filename, date):

    result = create_presigned_post(bucket, 'uploads/' + filename)

    if result is not None:
        #Upload file to S3 using presigned URL
        files = {'file': contents}
        r = requests.post(result['url'], data=result['fields'], files=files)

        return r


def get_example_files(prefix):

    s3_client = boto3.client('s3')
    
    example_files = s3_client.list_objects_v2(
        Bucket=bucket,
        Prefix=prefix,
        Delimiter='/'
    )

    file_list=[]
    for obj in example_files.get('Contents'):
        
        if obj['Size'] > 0:
            key=obj.get('Key')

            #sample file
            file = s3_client.get_object(Bucket=bucket, Key=key)
            #meta data on the file that has user-id etc on it
            header = s3_client.head_object(Bucket=bucket, Key=key)

            f = ZipFile(io.BytesIO(file['Body'].read()), 'r')
            user = header['ResponseMetadata']['HTTPHeaders']['x-amz-meta-userid']
            card_heading = header['ResponseMetadata']['HTTPHeaders']['x-amz-meta-header']
            image_file = header['ResponseMetadata']['HTTPHeaders']['x-amz-meta-image']
            dependencies = header['ResponseMetadata']['HTTPHeaders']['x-amz-meta-deps']

            file_payload = {'file': f, 
                            'user': user, 
                            'card_heading': card_heading, 
                            'image': image_file,
                            'deps': dependencies}

            file_list.append(file_payload)

    return file_list


def file_listings(prefix):

    s3_client = boto3.client('s3')
    
    num_files = 0

    example_files = s3_client.list_objects_v2(
        Bucket=bucket,
        Prefix=prefix,
        Delimiter='/'
    )['Contents']
    
    for content in example_files:
        if content['Size'] > 0:
            num_files += 1

    return num_files