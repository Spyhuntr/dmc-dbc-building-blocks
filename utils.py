import boto3
import dash_mantine_components as dmc
import logging
from botocore.exceptions import ClientError
import requests

def card_hdr(title: str, user: str):

    link = dmc.Anchor(
        href=f"https://github.com/{user}",
        children=['@' + user],
        size="xs",
        ml="-0.7rem",
        style={'color': 'rgb(134, 142, 150)'})

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
            ]
            )], span=10)


def build_contributors():

    contributors = ['snehilvj', 'tcbegley', 'AnnMarieW', 'Spyhuntr', 'Sohibjon']
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
            pl='1rem',
            target='_blank'
        )

        contrib_group.append(new_link)

    return contrib_group


def create_presigned_post(bucket_name, object_name):
    """Generate a presigned URL S3 POST request to upload a file

    :param bucket_name: string
    :param object_name: string
    :param fields: Dictionary of prefilled form fields
    :param conditions: List of conditions to include in the policy
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

    result = create_presigned_post("dmc-dbc-building-blocks", filename)

    if result is not None:
        #Upload file to S3 using presigned URL
        files = {'file': contents}
        r = requests.post(result['url'], data=result['fields'], files=files)

        return r