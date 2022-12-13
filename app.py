from dash import Dash, dash, dcc, html
import dash_mantine_components as dmc
import utils as u

app = Dash(__name__,
           external_scripts=[{
               "src": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/js/all.min.js",
               "crossorigin": "anonymous"
           }],
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
                    dmc.Text(
                        "Dash Mantine & Dash Bootstrap Building Blocks",
                        size="xl",
                        color="gray",
                    )
                ], smallerThan='md', styles={'display': 'none'}),
                dmc.MediaQuery([
                    dmc.Text(
                        "DMC & DBC",
                        size="xl",
                        color="gray",
                    )
                ], largerThan='md', styles={'display': 'none'})],
            span=10, p='sm'),
            dmc.Col(
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
                ], mt='6px'), span=2, p=0)
        ])
    ])

app.layout = dmc.MantineProvider(
    theme={
        'fontFamily': '"Inter", sans-serif'
    },
    withGlobalStyles=True,
    withNormalizeCSS=True,
    children=[
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
    ],
)

server = app.server

if __name__ == '__main__':
    app.run_server(
        debug=True
    )
