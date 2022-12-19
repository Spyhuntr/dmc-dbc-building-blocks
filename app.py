from dash import Dash, dash, dcc, html
import dash_mantine_components as dmc
import utils as u

app = Dash(__name__,
           external_scripts=[{
               "src": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/js/all.min.js",
               "crossorigin": "anonymous"
           }],
           external_stylesheets=[{
               "href": "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
               "rel": "stylesheet"
           }],
           meta_tags=[
               {'name': 'DMC-DBC-Building-Blocks',
                   'content': 'DMC/DBC Building Blocks'},
               {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},
               {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'},
               {'property': 'og:url',
                   'content': 'https://dmc-dbc-building-blocks.onrender.com/'},
               {'property': 'og:type', 'content': 'website'},
               {'property': 'og:title', 'content': 'DMC/DBC Building Blocks'},
               {'property': 'og:description',
                   'content': 'Building blocks for DMC/DBC'},
               {'property': 'og:image',
                   'content': 'https://dmc-dbc-building-blocks.onrender.com/assets/logo.png'},
               {'property': 'og:image:width', 'content': '500'},
               {'property': 'og:image:height', 'content': '100'}],
           suppress_callback_exceptions=True,
           use_pages=True)

app.title = 'DMC & DBC Building Blocks'

head = dmc.Header(
    height=60,
    p="sm",
    mb="1rem",
    children=[
        dmc.Grid([
            dmc.Col([
                dmc.MediaQuery([
                    dmc.Group([
                        dmc.Image(
                            src="/assets/logo.png", width=50
                        ),
                        dmc.Text(
                            "Dash Mantine & Dash Bootstrap Building Blocks",
                            size="xl",
                            color="gray",
                        )], p=0, m=0)
                ], smallerThan='md', styles={'display': 'none'}),
                dmc.MediaQuery([
                    dmc.Text(
                        "DMC & DBC",
                        size="xl",
                        color="gray",
                    )
                ], largerThan='md', styles={'display': 'none'})],
                span=10, lg=10, md=10, sm=11, xs=11, p='sm'),
            dmc.Col([
                dmc.MediaQuery([
                    dmc.Group([
                        dmc.Anchor(
                            dmc.Avatar(
                                src="/assets/mantine.png"
                            ),
                            href="https://www.dash-mantine-components.com/",
                            pl='1rem',
                            target='_blank'
                        ),
                        dmc.Anchor(
                            dmc.Avatar(
                                src="/assets/dbc.png"
                            ),
                            href="https://dash-bootstrap-components.opensource.faculty.ai",
                            pl='1rem',
                            target='_blank'
                        )
                    ], mt='6px')
                ], smallerThan='md', styles={'display': 'none'}),
                dmc.MediaQuery([
                    dmc.Menu(
                        [
                            dmc.MenuTarget(dmc.ActionIcon(
                                html.I(className='fas fa-bars fa-2x fa-fw'))),
                            dmc.MenuDropdown(
                                [
                                    dmc.MenuItem(
                                        "Dash Mantine Components",
                                        icon=dmc.Avatar(
                                            src="/assets/mantine.png",
                                            size='sm'
                                        ),
                                        href="https://www.dash-mantine-components.com/",
                                        target="_blank"
                                    ),
                                    dmc.MenuItem(
                                        "Dash Bootstrap Components",
                                        icon=dmc.Avatar(
                                            src="/assets/dbc.png",
                                            size='sm'
                                        ),
                                        href="https://dash-bootstrap-components.opensource.faculty.ai",
                                        target="_blank"
                                    ),
                                ]
                            ),
                        ], style={'paddingTop': '0.7rem'}
                    ),
                ], largerThan='md', styles={'display': 'none'})
            ], span=2, lg=2, md=2, sm=1, xs=1, p=0)
        ])
    ])

app.layout = dmc.MantineProvider(
    theme={
        'fontFamily': '"Inter", sans-serif'
    },
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
        dmc.NotificationsProvider([
        dcc.Location(id='url', refresh=False),
        head,
        dmc.Container(
            [dash.page_container],
            id="page-container",
            style={'minWidth': '800px'},
            pb='1rem',
            size='xl'
        ),
        html.Div([
            dmc.Center(id='contributors', children=u.build_contributors()),
            dmc.Center([
                dmc.Text(
                    "Contributors",
                    pt='1rem'
                )
            ])
        ], className="footer")
        ])
    ],
)

server = app.server

if __name__ == '__main__':
    app.run_server(
        debug=True
    )
