
import dash
from dash import callback, Output, Input, State, MATCH, html, ctx, dcc
import dash_mantine_components as dmc
import utils as u
import pyperclip as clip

dash.register_page(__name__, path='/navbars', title='Home')

card_desc = [
    {"header": "Hover Navbar", "user": "Sohibjon",
     "code": "./rendered_code/hover_navbar.py", "image": "/assets/hover_navbar.gif"
     },
    {"header": "Responsive Navbar", "user": "spyhuntr",
     "code": "./rendered_code/responsive_navbar.py", "image": "/assets/responsive_navbar.gif"
     }
]


layout = dmc.Grid(
    children=[
        dmc.Col(
            dcc.Link(
                id='back_btn',
                href="/",
                children=[
                    dmc.Button("< Back to all categories", variant="outline")
                ])
        ),
        dmc.Col(
            dmc.Title(f"Navbars", order=1)
        ),
        dmc.Col(
            id="navbar-sample-container",
            children=[]
        )
    ])


@callback(
    Output('navbar-sample-container', 'children'),
    [Input('url', 'pathname'),
    Input('navbar-sample-container', 'children')]
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
                                    sample["header"], sample["user"], key),
                                dmc.Col(
                                    dmc.Tooltip(
                                        id={
                                            "type": "navbar-copy-tooltip",
                                            "index": key
                                        },
                                        label="Copy Code",
                                        transition="pop-top-right",
                                        transitionDuration=300,
                                        withArrow=True,
                                        children=[
                                            dmc.ActionIcon(
                                                html.I(
                                                    className="fa-regular fa-clipboard fa-lg"),
                                                id={
                                                    "type": "navbar-copy-icon",
                                                    "index": key
                                                },

                                                color='gray'
                                            )]), span='content'
                                ),
                                dmc.Col(
                                    dmc.Switch(
                                        id={
                                            "type": "navbar-code-switch",
                                            "index": key
                                        },
                                        size="xl",
                                        onLabel="Code",
                                        offLabel="Preview"
                                    ), span='content', style={"marginTop": "-21px"}),
                            ], gutter=0, grow=True, justify='space-around')
                    ]),
                dmc.Center([dmc.Container(id={
                    "type": "navbar-rendering",
                    "index": key
                }, p="xl")]),

                html.Div(id={
                    "type": "navbar-copy-code-div",
                    "index": key
                }, children=[])
            ]
        )

        children.append(new_sample)

    return children


@callback(
    Output({'type': 'navbar-rendering', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'navbar-code-switch', 'index': MATCH}, 'checked')],
    State({'type': 'navbar-code-switch', 'index': MATCH}, 'id')
)
def state_change(url, switch, id):

    if switch:
        with open(card_desc[id["index"]]["code"], "r") as file:
            code = file.read()

            return u.build_code(code)
    else:
        return dmc.Image(src=card_desc[id["index"]]["image"], width=600)


@callback(
    Output({'type': 'navbar-copy-code-div', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'navbar-copy-icon', 'index': MATCH}, 'n_clicks')],
    State({'type': 'navbar-copy-icon', 'index': MATCH}, 'id')
)
def copy_code(url, clicks, id):

    with open(card_desc[id["index"]]["code"], "r") as file:
        code = file.read()

    clip.copy(code)

    return None

