
import dash
from dash import callback, Output, Input, State, MATCH, html, ctx, dcc
import dash_mantine_components as dmc
import utils as u

dash.register_page(__name__, path='/app_cards', title='Cards')

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
                id='cards-back_btn',
                href="/",
                children=[
                    dmc.Button("< Back to all categories", variant="outline")
                ])
        ),
        dmc.Col(
            dmc.Title(f"Application Cards", order=1)
        ),
        dmc.Col(
            id="cards-sample-container",
            children=[]
        )
    ])


@callback(
    Output('cards-sample-container', 'children'),
    [Input('url', 'pathname'),
     Input('cards-sample-container', 'children')]
)
def build_layout(_, children):

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
                                            "type": "cards-code-switch",
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
                        "type": "cards-rendering",
                        "index": key
                    },
                    children=[]
                )
            ]
        )

        children.append(new_sample)

    return children


@callback(
    Output({'type': 'cards-rendering', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'cards-code-switch', 'index': MATCH}, 'checked')],
    State({'type': 'cards-code-switch', 'index': MATCH}, 'id')
)
def state_change(_, switch, id):

    if switch:
        with open(card_desc[id["index"]]["code"], "r") as file:
            code = file.read()


        return dmc.Prism(
            language='python',
            children=code
        )
    else:
        return dmc.Center(dmc.Image(src=card_desc[id["index"]]["image"], width=600), p='xl')

