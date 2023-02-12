
import dash
from dash import callback, Output, Input, State, MATCH, html, ctx, dcc
import dash_mantine_components as dmc
import utils as u

dash.register_page(__name__, path='/authentication', title='Authentication')
prefix = 'examples/auth/'


layout = dmc.LoadingOverlay([dmc.Grid(
    children=[
        dmc.Col(
            dcc.Link(
                id='auth-back_btn',
                href="/",
                children=[
                    dmc.Button("< Back to all categories", variant="outline")
                ])
        ),
        dmc.Col(
            dmc.Title(f"Authentication", order=1)
        ),
        dmc.Col(
            id="auth-sample-container",
            children=[]
        )
    ])])


@callback(
    Output('auth-sample-container', 'children'),
    [Input('url', 'pathname'),
     Input('auth-sample-container', 'children')]
)
def build_layout(_, children):

    if ctx.triggered_id == 'url':
        return None

    for key, card_info in enumerate(u.get_example_files(prefix)):
        new_sample = dmc.Paper(
            withBorder=True,
            radius="md",
            mb="3rem",
            shadow='xl',
            style={"backgroundColor": "#f8f9fa", "overflow": "hidden"},
            children=[
                dmc.Header(
                    height=50,
                    p="xs",
                    children=[
                        dmc.Grid(
                            children=[
                                u.card_hdr(
                                    card_info['card_heading'], card_info['user'], card_info['deps']),
                                    dmc.Switch(
                                        id={
                                            "type": "auth-code-switch",
                                            "index": key
                                        },
                                        size="xl",
                                        onLabel="Code",
                                        offLabel="Preview",
                                    style={"marginTop": "-1.313rem", 'marginRight':'0.5rem'}),
                            ], gutter=0, grow=True, justify='space-around')
                    ]),

                html.Div(
                    id={
                        "type": "auth-rendering",
                        "index": key
                    },
                    children=[]
                )
            ]
        )

        children.append(new_sample)

    return children


@callback(
    Output({'type': 'auth-rendering', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'auth-code-switch', 'index': MATCH}, 'checked')],
    State({'type': 'auth-code-switch', 'index': MATCH}, 'id')
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

            img_file = 'https://dmc-dbc-building-blocks.s3.amazonaws.com/examples/auth/images/' + \
                card_dict[id['index']]['image']

            return dmc.Center(dmc.Image(src=img_file, style={'minWidth': '70%', 'maxWidth': '70%'}), p='xl')
