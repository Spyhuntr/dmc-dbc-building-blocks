from dash import Dash, dash, dcc, html
import dash_mantine_components as dmc

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
        dmc.Text(
            "Dash Mantine & Dash Bootstrap Components Building Blocks",
            size="xl",
            color="gray",
        )
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
            size='xl',
            style={'minWidth': '800px'},
            pb='1rem'
        ),
        html.Div([
        dmc.Center([
            dmc.Anchor(
                dmc.Tooltip(
                    label="snehilvj",
                    withArrow=True,
                    transition="pop-top-right",
                    transitionDuration=300,
                    children=[
                        dmc.Image(
                            src="https://github.com/snehilvj.png",
                            width="50px"
                        )]),
                href="https://github.com/snehilvj"
            ),
            dmc.Anchor(
                dmc.Tooltip(
                    label="snehilvj",
                    withArrow=True,
                    transition="pop-top-right",
                    transitionDuration=300,
                    children=[
                        dmc.Image(
                            src="https://github.com/AnnMarieW.png",
                            width="50px"
                        )]),
                href="https://github.com/AnnMarieW",
                pl='1rem'
            )
        ]),
        dmc.Center([
            dmc.Text(
                "Special thanks to @snehilvj & @AnnMarieW for making DMC and DBC!",
                pt='1rem'
            )
        ])
    ], className="footer")
    ],
)


server = app.server

if __name__ == '__main__':
    app.run_server(
        host='0.0.0.0',
        port='8050',
        debug=True,
        dev_tools_props_check=True
    )
