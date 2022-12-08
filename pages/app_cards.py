
import dash
from dash import callback, Output, Input, State, MATCH, html, ctx, dcc
import dash_mantine_components as dmc
import utils as u
import pyperclip as clip

dash.register_page(__name__, path='/app_cards', title='Home')

card_desc = [
    {"header": "Card with Embedded Chart", "user": "spyhuntr",
     "code": "./rendered_code/card_embedded_chart.py", "image": "/assets/card_embedded_chart_img.png"
     },
    {"header": "KPI Card Group", "user": "AnnMarieW",
     "code": "./rendered_code/card_group.py", "image": "/assets/card_group_kpi.png"
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
            dmc.Title(f"Application Cards", order=1)
        ),
        dmc.Col(
            id="sample-container",
            children=[]
        )
    ])


@callback(
    Output('sample-container', 'children'),
    [Input('url', 'pathname'),
    Input('sample-container', 'children')]
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
                                            "type": "copy-tooltip",
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
                                                    "type": "copy-icon",
                                                    "index": key
                                                },

                                                color='gray'
                                            )]), span='content'
                                ),
                                dmc.Col(
                                    dmc.Switch(
                                        id={
                                            "type": "code-switch",
                                            "index": key
                                        },
                                        size="xl",
                                        onLabel="Code",
                                        offLabel="Preview"
                                    ), span='content', style={"marginTop": "-21px"}),
                            ], gutter=0, grow=True, justify='space-around')
                    ]),

                dmc.Center([dmc.Container(id={
                    "type": "rendering",
                    "index": key
                }, p="xl")]),

                html.Div(id={
                    "type": "copy-code-div",
                    "index": key
                }, children=[])
            ]
        )

        children.append(new_sample)

    return children


@callback(
    Output({'type': 'rendering', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'code-switch', 'index': MATCH}, 'checked')],
    State({'type': 'code-switch', 'index': MATCH}, 'id')
)
def state_change(url, switch, id):

    if switch:
        with open(card_desc[id["index"]]["code"], "r") as file:
            code = file.read()

            return u.build_code(code)
    else:
        return dmc.Image(src=card_desc[id["index"]]["image"], width=600)


@callback(
    Output({'type': 'copy-code-div', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'copy-icon', 'index': MATCH}, 'n_clicks')],
    State({'type': 'copy-icon', 'index': MATCH}, 'id')
)
def copy_code(url, clicks, id):

    with open(card_desc[id["index"]]["code"], "r") as file:
        code = file.read()

    clip.copy(code)

    return None














# dash.register_page(__name__, path='/app_cards', title='Home')

# card_desc = [
#     {"header": "Card with Embedded Chart", "user": "spyhuntr",
#      "code": "./rendered_code/card_embedded_chart.py", "image": "/assets/card_embedded_chart_img.png"
#      },
#     {"header": "KPI Card Group", "user": "AnnMarieW",
#      "code": "./rendered_code/card_group.py", "image": "/assets/card_group_kpi.png"
#      }
# ]

# layout = html.Div([
#             dmc.Anchor(
#                 href="/",
#                 children=[
#                     dmc.Button("< Back to all categories", variant="outline")
#                 ]),
#     html.Button("Add Filter", id="dynamic-add-filter", n_clicks=0),
#     html.Div(id='dynamic-dropdown-container', children=[]),
# ])

# @callback(
#     Output('dynamic-dropdown-container', 'children'),
#     Input('dynamic-add-filter', 'n_clicks'),
#     State('dynamic-dropdown-container', 'children'))
# def display_dropdowns(n_clicks, children):

#     print(n_clicks, children)
#     new_element = html.Div([
#        dcc.Dropdown(
#             ['NYC', 'MTL', 'LA', 'TOKYO'],
#             id={
#                 'type': 'dynamic-dropdown',
#                 'index': n_clicks
#             }
#         ),
#         html.Div(
#             id={
#                 'type': 'dynamic-output',
#                 'index': n_clicks
#             }
#         )
#     ])
#     children.append(new_element)
#     return children


# @callback(
#     Output({'type': 'dynamic-output', 'index': MATCH}, 'children'),
#     Input({'type': 'dynamic-dropdown', 'index': MATCH}, 'value'),
#     State({'type': 'dynamic-dropdown', 'index': MATCH}, 'id'),
# )
# def display_output(value, id):
#     return html.Div('Dropdown {} = {}'.format(id['index'], value))
