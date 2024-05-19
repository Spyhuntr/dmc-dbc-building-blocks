from dash import Dash, html, dash, dcc
import dash_mantine_components as dmc
import sys
import utils as u
sys.path.append('../components')

dash._dash_renderer._set_react_version('18.2.0')

from components.navbar import head

stylesheets = [
    "https://unpkg.com/@mantine/code-highlight@7/styles.css",
    "https://unpkg.com/@mantine/notifications@7/styles.css"
]

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
                {'property':'og:image:height', 'content':'100'}
            ],
            external_stylesheets=stylesheets,
            suppress_callback_exceptions=True,
            use_pages=True
)

app.title = 'DMC & DBC Building Blocks'

app.layout = dmc.MantineProvider(
    theme={
        'fontFamily': '"Open Sans", sans-serif'
    },
    children=[
        dmc.NotificationProvider(),
        dmc.AppShell([
            head,
            dmc.AppShellMain(
                children=[
                    dcc.Loading(dmc.Container(
                        dash.page_container,
                        id="page-container",
                        pb='1rem',
                        size='xl'
                    ), type="dot", fullscreen=True),
                    html.Div([
                        dmc.Center(id='contributors', children=u.build_contributors()),
                        dmc.Center([
                            dmc.Text(
                                "Contributors",
                            )
                        ])
                    ])
                ]
            )
        ],
        header={"height": 60},
        padding="xl"
        )
    ]
)

server = app.server

if __name__ == '__main__':
    app.run(dev_tools_hot_reload=True, debug=True)
