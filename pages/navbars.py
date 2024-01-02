
import dash
from dash import callback, Output, Input, State, MATCH, html, ctx, dcc
import dash_mantine_components as dmc
import utils as u

dash.register_page(__name__, path='/navbars', title='Home')
prefix = 'examples/navbars/'


layout = dmc.LoadingOverlay([dmc.Grid(
    children=[
        dmc.Col(
            dcc.Link(
                id='navbars-back-btn',
                href="../",
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
    ])])


@callback(
    Output('navbars-sample-container', 'children'),
    Input('navbars-sample-container', 'children')
)
def build_layout(children):

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
                                    dmc.Switch(
                                        id={
                                            "type": "navbars-code-switch",
                                            "index": key
                                        },
                                        size="xl",
                                        onLabel="Code",
                                        offLabel="Preview",
                                    style={"marginTop": "-0.2rem", 'marginRight':'0.5rem'}),
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
    Input({'type': 'navbars-code-switch', 'index': MATCH}, 'checked'),
    State({'type': 'navbars-code-switch', 'index': MATCH}, 'id')
)
def state_change(switch, id):

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

    img_file = 'https://dmc-dbc-building-blocks.s3.amazonaws.com/examples/navbars/images/' + \
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
                        "Add to ./assets/style.css in your app", size='xs', color='grey')], p='xs'),
                    dmc.Prism(
                        language='css',
                        children=css_file,
                        style={'border': '1px solid #ececec'}
                    )], span=6)
            ], gutter=0)
        ])
    else:
        return dmc.Center(dmc.Image(src=img_file, sx={'width': 'auto !important'}), p='xl')
