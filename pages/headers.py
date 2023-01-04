
import dash
from dash import callback, Output, Input, State, MATCH, html, ctx, dcc
import dash_mantine_components as dmc
import utils as u

dash.register_page(__name__, path='/headers', title='Headers')
prefix = 'examples/headers/'


layout = dmc.LoadingOverlay([dmc.Grid(
    children=[
        dmc.Col(
            dcc.Link(
                id='headers_back_btn',
                href="/",
                children=[
                    dmc.Button("< Back to all categories", variant="outline")
                ])
        ),
        dmc.Col(
            dmc.Title(f"Headers", order=1)
        ),
        dmc.Col(
            id="headers-sample-container",
            children=[]
        )
    ])])


@callback(
    Output('headers-sample-container', 'children'),
    [Input('url', 'pathname'),
     Input('headers-sample-container', 'children')]
)
def build_layout(_, children):

    if ctx.triggered_id == 'url':
        return None

    for key, card_info in enumerate(u.get_example_files(prefix)):
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
                                    card_info['card_heading'], card_info['user']),
                                dmc.Col(
                                    dmc.Switch(
                                        id={
                                            "type": "headers-code-switch",
                                            "index": key
                                        },
                                        size="xl",
                                        onLabel="Code",
                                        offLabel="Preview"
                                    ), span='auto', style={"marginTop": "-21px"}),
                            ], gutter=0, grow=True, justify='space-around')
                    ]),

                html.Div(
                    id={
                        "type": "headers-rendering",
                        "index": key
                    },
                    children=[]
                )
            ]
        )

        children.append(new_sample)

    return children


@callback(
    Output({'type': 'headers-rendering', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'headers-code-switch', 'index': MATCH}, 'checked')],
    State({'type': 'headers-code-switch', 'index': MATCH}, 'id')
)
def build_examples(_, switch, id):

    card_dict = u.get_example_files(prefix)

    for name in card_dict[id['index']]['file'].namelist():

        if switch:

            if name.endswith(('py', 'css')):
                return dmc.Prism(
                    language='python',
                    children=card_dict[id['index']]['file'].read(
                        name).decode('utf-8')
                )

        else:

            img_file = 'https://dmc-dbc-building-blocks.s3.amazonaws.com/examples/headers/images/' + \
                card_dict[id['index']]['image']

            return dmc.Center(dmc.Image(src=img_file, style={'minWidth': '70%', 'maxWidth': '70%'}), p='xl')
