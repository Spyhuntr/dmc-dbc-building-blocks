
import dash
from dash import callback, Output, Input, State, MATCH, html, ctx, dcc
import dash_mantine_components as dmc
import utils as u

dash.register_page(__name__, path='/tabs', title='Home')
prefix = 'examples/tabs/'


layout = dmc.LoadingOverlay([dmc.Grid(
    children=[
        dmc.Col(
            dcc.Link(
                id='tabs-back-btn',
                href="/",
                children=[
                    dmc.Button("< Back to all categories", variant="outline")
                ])
        ),
        dmc.Col(
            dmc.Title(f"Tabs", order=1)
        ),
        dmc.Col(
            id="tabs-sample-container",
            children=[]
        )
    ])])


@callback(
    Output('tabs-sample-container', 'children'),
    [Input('url', 'pathname'),
     Input('tabs-sample-container', 'children')]
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
                                    card_info['card_heading'], card_info['user'], card_info['deps']),
                                dmc.Col(
                                    dmc.Switch(
                                        id={
                                            "type": "tabs-code-switch",
                                            "index": key
                                        },
                                        size="xl",
                                        onLabel="Code",
                                        offLabel="Preview"
                                    ), span='auto',  style={"marginTop": "-21px"}),
                            ], gutter=0, grow=True, justify='space-around')
                    ]),

                html.Div(
                    id={
                        "type": "tabs-rendering",
                        "index": key
                    },
                    children=[]
                )
            ]
        )

        children.append(new_sample)

    return children


@callback(
    Output({'type': 'tabs-rendering', 'index': MATCH}, 'children'),
    [Input('url', 'pathname'),
     Input({'type': 'tabs-code-switch', 'index': MATCH}, 'checked')],
    State({'type': 'tabs-code-switch', 'index': MATCH}, 'id')
)
def state_change(_, switch, id):

    card_dict = u.get_example_files(prefix)

    py_file = None
    css_file = None
    img_file = None
    for name in card_dict[id['index']]['file'].namelist():

        if name.endswith('py'):
            py_file = card_dict[id['index']]['file'].read(name).decode('utf-8')

        if name.endswith('css'):
            css_file = card_dict[id['index']]['file'].read(
                name).decode('utf-8')

    img_file = 'https://dmc-dbc-building-blocks.s3.amazonaws.com/examples/tabs/images/' + \
        card_dict[id['index']]['image']

    if switch:
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
        return dmc.Center(dmc.Image(src=img_file, style={'minWidth': '70%', 'maxWidth': '70%'}), p='xl')
