from dash import Dash, dash, dcc, html
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
           external_stylesheets=[{
               "href": "https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css",
               "rel": "stylesheet"
           }],
           meta_tags=[
               {'name': 'Dash-Building-Blocks',
                   'content': 'Dash Building Blocks'},
               {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'},
               {'http-equiv': 'X-UA-Compatible', 'content': 'IE=edge'},
               {'property': 'og:url',
                   'content': 'https://dash-building-blocks.com/'},
               {'property': 'og:type', 'content': 'website'},
               {'property': 'og:title', 'content': 'Dash Building Blocks'},
               {'property': 'og:description',
                   'content': 'Building blocks for Dash'},
               {'property': 'og:image',
                   'content': 'https://dash-building-blocks.com/assets/logo.png'},
               {'property': 'og:image:width', 'content': '500'},
               {'property': 'og:image:height', 'content': '100'}],
           suppress_callback_exceptions=True,
           use_pages=True)

app.title = 'Dash Building Blocks'

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
    app.run_server(
        debug=True
    )
