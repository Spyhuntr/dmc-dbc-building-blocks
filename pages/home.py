
import dash
from dash import html, dcc, Output, Input, callback, State
import dash_mantine_components as dmc
from utils import upload_file, file_listings
import base64

dash.register_page(__name__, path='/', title='DMC/DBC Home')

layout = html.Div([
    dmc.LoadingOverlay([
    dmc.Grid(
        id='card-grid',
        children=[
            dmc.Col([
                dmc.Center(
                    style={"height": '100%'},
                    children=[
                dmc.Stack([
                    dmc.Text(
                        "Build your next Dash application even faster with premade responsive components designed"
                        " and built by DMC and DBC maintainers and community.",
                        size="xl",
                        color="gray",
                        style={'textAlign': 'center'}
                    ),
                    dmc.Text("Contribute Building Block",
                             color="gray",
                             style={'textAlign': 'center'}),
                    dmc.Group([
                        dcc.Link(
                            id='github-btn',
                            href="https://github.com/Spyhuntr/dmc-dbc-building-blocks/issues/1#issue-1506988208",
                            target='_blank',
                            children=[
                                dmc.Button(
                                    "Github",
                                    leftIcon=html.I(
                                        className='fa-brands fa-github fa-lg fa-fw'),
                                )
                            ]),
                        dmc.Button(
                            "Upload",
                            id='add-building-block-btn',
                            rightIcon=html.I(
                                className='fas fa-upload fa-lg fa-fw'),
                        )
                    ], position='center')
                ], justify='center')]),
            ], span=8),
            dmc.Col([
                dmc.Center(
                    style={"height": '100%'},
                    children=[
                        dmc.Image(
                            id='home_logo',
                            src="/assets/home_logo.png",
                            className='animate__animated animate__fadeInTopRight',
                            style={'maxWidth': '150px'}
                        )
                    ]
                )
            ], span=2, offset=1)
        ]),
    ]),
    dmc.Modal(
        id="upload-modal",
        size='xl',
        transition='slide-down',
        transitionDuration=400,
        children=[
            dmc.LoadingOverlay([
            dmc.Text("Upload a zip file of your code.  The filename should include your github handle "
                     " if you would like to get credit for your building block.  "
                     "I will get a notification when new building blocks have been submitted.",
                     color="gray",
                     style={'textAlign': 'center'}),
            dmc.Space(h=10),
            dmc.Text("What are building blocks?",
                     color="gray",
                     style={'textAlign': 'center'}),
            dmc.Text("Building blocks are small UI components that are part of an app.  "
                     "These building blocks are not a full app but rather can be added into an "
                     "existing app to enhance the UI/UX experience of your dash application.",
                     color="gray",
                     style={'textAlign': 'center'}),
            dmc.Space(h=20),
            dcc.Upload(
                id='upload',
                max_size=3145728,
                accept='.zip,.py,.css',
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
    )])
    ]
)


@callback(Output('card-grid', 'children'),
          Input('card-grid', 'children'),
          State('card-grid', 'children'),
          )
def create_cards(_, children):

    card_info = [
        {'image': '/assets/cards-light.svg', 'title': 'Application Cards', 'page': '/app_cards', 'prefix': 'examples/cards/'},
        {'image': '/assets/navbars-light.svg', 'title': 'Navbars', 'page': '/navbars', 'prefix': 'examples/navbars/'},
        {'image': '/assets/footers-light.svg', 'title': 'Footers', 'page': '/footers', 'prefix': 'examples/footers/'},
        {'image': '/assets/headers-light.svg', 'title': 'Headers', 'page': '/headers', 'prefix': 'examples/headers/'},
        {'image': '/assets/menus-light.svg', 'title': 'Menus', 'page': '/menus', 'prefix': 'examples/menus/'}

    ]

    for card in card_info:
        card = dmc.Col([
            dmc.Paper(
                children=[
                    dmc.Anchor(
                        href=card['page'],
                        children=[
                            html.Div(
                                dmc.Image(
                                    src=card['image'],
                                ), className='card-hdr'
                            ),
                            dmc.Text(
                                card['title'],
                                pt="md",
                                pl="md"
                            ),
                            dmc.Text(
                                f"{file_listings(card['prefix'])} Components",
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
            )], xs=12, sm=6, md=3, lg=3)
        children.append(card)

    return children


@callback(
    Output('upload-modal', 'opened'),
    Input('add-building-block-btn', 'n_clicks'),
    prevent_initial_call=True,
)
def open_modal(_):

    if _ is not None:
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

    message = upload_file(content_decoded, name, date)

    if message is not None:
        if message.status_code == 204:
            return dmc.Notification(
                id="upload-notify",
                action="show",
                message="File successfully uploaded!",
                icon=html.I(className='fas fa-check fa-lg fa-fw'),
                color='green'
            )
        else:
            return f"{message.status_code} - {message.reason}"