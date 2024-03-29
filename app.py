from dash import Dash, dash, html
import dash_mantine_components as dmc
import utils as u
import sys
sys.path.append('../components')

from components.navbar import head

app = Dash(__name__,
           external_scripts=[{
               "src": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/js/all.min.js",
               "crossorigin": "anonymous"
           }],
            meta_tags=[
        {'name':'DMC-DBC-Building-Blocks', 'content':'DMC/DBC Building Blocks'},
        {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},
        {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'},
        {'property':'og:url', 'content': 'https://dmc-dbc-building-blocks.onrender.com/'},
        {'property':'og:type', 'content': 'website'},
        {'property':'og:title', 'content': 'DMC/DBC Building Blocks'},
        {'property':'og:description','content':'Building blocks for DMC/DBC'},
        {'property':'og:image', 'content':'https://dmc-dbc-building-blocks.onrender.com/assets/logo.png'},
        {'property':'og:image:width', 'content':'500'},
        {'property':'og:image:height', 'content':'100'}],
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
                span='auto', p='sm'),
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
                ], mt='6px'), span='content', p=0, pr='2rem')
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
            head,
            dmc.Container(
                [dash.page_container],
                id="page-container",
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
        ], position='top-right')
    ],
)

server = app.server

if __name__ == '__main__':
    app.run()
