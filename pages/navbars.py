
import dash
from dash import callback, Output, Input, State, MATCH, html, ctx, dcc
import dash_mantine_components as dmc
import utils as u

dash.register_page(__name__, path='/navbars', title='Home')

card_desc = [
    {"header": "Hover Navbar", "user": "Sohibjon",
     "code": ["./rendered_code/hover_navbar.py",
              "./rendered_code/hover_navbar.css"],
     "image": "/assets/hover_navbar.gif"
     },
    {"header": "Responsive Navbar", "user": "spyhuntr",
     "code": ["./rendered_code/responsive_navbar.py",
              "./rendered_code/responsive_navbar.css"],
     "image": "/assets/responsive_navbar.gif"
     }
]


layout = dmc.Grid(
    children=[
        dmc.Col(
            dcc.Link(
                id='navbars-back-btn',
                href="/",
                children=[
                    dmc.Button("< Back to all categories", variant="outline")
                ])
        ),
        dmc.Col(
            dmc.Title(f"Navbars", order=1)
        ),
        dmc.Col(
            id="navbars-sample-container",
            children=[]
        )
    ])


@callback(
    Output('navbars-sample-container', 'children'),
    [Input('url', 'pathname'),
     Input('navbars-sample-container', 'children')]
)
def build_layout(url, children):

    if ctx.triggered_id == 'url':
        return None

    for key, sample in enumerate(card_desc):
        new_sample = dmc.Paper(
            withBorder=True,
            radius="md",
            mb="2rem",
            style={"backgroundColor": "#f8f9fa", "overflow": "hidden"},
            children=[
                dmc.Header(
                    height=50,
                    p="xs",
                    children=[
                        dmc.Grid(
                            children=[
                                u.card_hdr(
                                    sample["header"], sample["user"]),
                                dmc.Col(
                                    dmc.Switch(
                                        id={
                                            "type": "navbars-code-switch",
                                            "index": key
                                        },
                                        size="xl",
                                        onLabel="Code",
                                        offLabel="Preview"
                                    ), span='content', style={"marginTop": "-21px"}),
                            ], gutter=0, grow=True, justify='space-around')
                    ]),

                html.Div(
                    id={
                        "type": "navbars-rendering",
                        "index": key
                    },
                    children=[]
                )
            ]
        )

        children.append(new_sample)

    return children


@callback(
    Output({'type': 'navbars-rendering', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'navbars-code-switch', 'index': MATCH}, 'checked')],
    State({'type': 'navbars-code-switch', 'index': MATCH}, 'id')
)
def state_change(url, switch, id):

    if switch:
        files = card_desc[id["index"]]['code']

        with open(files[0], "r") as py, open(files[1], "r") as css:
            py_file = py.read()
            css_file = css.read()

        return html.Div([
            dmc.Grid([
                dmc.Col([
                    dmc.Text("Python", p="xs"),
                    dmc.Prism(
                        language='python',
                        children=py_file,
                        style={'border': '1px solid #ececec'},
                        mr='1rem'
                    )], span=6),
                dmc.Col([
                    dmc.Group([dmc.Text("CSS"), dmc.Text(
                        "Add to ./assets/style.css in your app", size='sm', color='grey')], p='xs'),
                    dmc.Prism(
                        language='css',
                        children=css_file,
                        style={'border': '1px solid #ececec'}
                    )], span=6)
            ], gutter=0)
        ])

    else:

        return dmc.Center(dmc.Image(src=card_desc[id["index"]]["image"], width=600), p='xl')
