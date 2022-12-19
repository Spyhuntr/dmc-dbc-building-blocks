
import dash
from dash import html, dcc, Output, Input, callback, State
import dash_mantine_components as dmc
from utils import upload_file
import io
import base64
import zipfile

dash.register_page(__name__, path='/', title='DMC/DBC Home')

layout = html.Div([
    dmc.Grid(
        children=[
            dmc.Col([
                dmc.Stack([
                    dmc.Text(
                        "Build your next Dash application even faster with premade responsive components designed"
                        " and built by DMC and DBC maintainers and community.",
                        size="xl",
                        color="gray",
                        style={'textAlign': 'center'}
                    ),
                    dmc.Group([
                        dcc.Link(
                            id='github-btn',
                            href="https://github.com/Spyhuntr/dmc-dbc-building-blocks",
                            target='_blank',
                            children=[
                                dmc.Button(
                                    "Github",
                                    leftIcon=html.I(
                                        className='fa-brands fa-github fa-lg fa-fw'),
                                )
                            ]),
                        dmc.Button(
                            "Add Building Block",
                            id='add-building-block-btn',
                            rightIcon=html.I(
                                className='fas fa-upload fa-lg fa-fw'),
                        )
                    ], position='center')
                ], style={"height": 300}, justify='center'),
            ], span=8),
            dmc.Col([
                dmc.Image(
                    id='home_logo',
                    src="/assets/home_logo.png",
                    width=150,
                    className='animate__animated animate__fadeInTopRight',
                )
            ], span=2, offset=1),
            dmc.Col([
                dmc.Paper(
                    children=[
                        dmc.Anchor(
                            href="/app_cards",
                            children=[
                                html.Div(
                                    dmc.Image(
                                        src="/assets/cards-light.svg",
                                    ), className='card-hdr'
                                ),
                                dmc.Text(
                                    "Application Cards",
                                    pt="md",
                                    pl="md"
                                ),
                                dmc.Text(
                                    "2 Components",
                                    size="xs",
                                    pl="md",
                                    pb="md",
                                    color="#868e96"
                                )
                            ],
                            variant="text"
                        )],
                    shadow="xl",
                    withBorder=True,
                    radius="md",
                    style={"overflow": "hidden"}
                )], span=3),
            dmc.Col([
                dmc.Paper(
                    children=[
                        dmc.Anchor(
                            href="/navbars",
                            children=[
                                html.Div(
                                    dmc.Image(
                                        src="/assets/navbars-light.svg",
                                    ), className='card-hdr'
                                ),
                                dmc.Text(
                                    "Navbars",
                                    pt="md",
                                    pl="md"
                                ),
                                dmc.Text(
                                    "2 Components",
                                    size="xs",
                                    pl="md",
                                    pb="md",
                                    color="#868e96"
                                )
                            ],
                            variant="text"
                        )],
                    shadow="xl",
                    withBorder=True,
                    radius="md",
                    style={"overflow": "hidden"}
                )], span=3)
        ]),
    dmc.Modal(
        id="upload-modal",
        size='xl',
        transition='slide-down',
        transitionDuration=400,
        children=[
            dmc.Text("Upload a zip file of your code.  Include your github handle in the file name"
                     " so I can give you credit on the site for your building block.  "
                     "I will get a notification when new building blocks have been submitted.",
                     color="gray",
                     style={'textAlign': 'center'}),
            dmc.Space(h=20),
            dcc.Upload(
                id='upload',
                max_size=3145728,
                accept='.zip',
                children=html.Div([
                    'Drag and Drop or ',
                    dmc.Anchor(
                        "Select Files",
                        href="#",
                    ),
                ]),
                style={
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center'
                },
            ),
            html.Div(id='output-upload')
        ],
    )]


)


@callback(
    Output('upload-modal', 'opened'),
    Input('add-building-block-btn', 'n_clicks'),
    prevent_initial_call=True,
)
def open_modal(_):

    return True


@callback(Output('output-upload', 'children'),
          Input('upload', 'contents'),
          State('upload', 'filename'),
          State('upload', 'last_modified'),
          prevent_initial_call=True)
def update_output(content, name, date):

    # the content needs to be split. It contains the type and the real content
    content_type, content_string = content.split(',')
    # Decode the base64 string
    content_decoded = base64.b64decode(content_string)
    # Use BytesIO to handle the decoded content
    zip_str = io.BytesIO(content_decoded)
    # Now you can use ZipFile to take the BytesIO output
    zip_obj = zipfile.ZipFile(zip_str, 'r')
    message = upload_file(zip_obj, name, date)

    if message is not None:
        if message.status_code == 204:
            return dmc.Notification(
                id="simple-notify",
                action="show",
                message="File successfully uploaded!",
                icon=html.I(className='fas fa-check fa-lg fa-fw')
        )
        else:
            return f"{message.status_code} - {message.reason}"
