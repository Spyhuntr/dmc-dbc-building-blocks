
import dash
from dash import callback, Output, Input, State, MATCH, html, dcc
import dash_mantine_components as dmc
import utils as u

dash.register_page(__name__, path='/tables', title='Tables')
prefix = 'examples/tables/'

examples = u.get_example_files(prefix)

layout = dmc.Grid(
    children=[
        dmc.GridCol(
            dcc.Link(
                id='tables-back_btn',
                href="/",
                children=[
                    dmc.Button("< Back to all categories", variant="outline")
                ])
        ),
        dmc.GridCol(
            dmc.Title(f"Tables", order=1)
        ),
        dmc.GridCol(
            id="tables-sample-container",
            children=[]
        ),
    ])


@callback(
    Output('tables-sample-container', 'children'),
    Input('tables-sample-container', 'children')
)
def build_layout(children):

    for key, card_info in enumerate(examples):

        new_sample = dmc.Card(
            withBorder=True,
            radius="md",
            mb="3rem",
            shadow='xl',
            children=[
                dmc.CardSection([
                dmc.Grid(
                    children=[
                        u.card_hdr(
                            card_info['card_heading'], card_info['user'], card_info['deps']),
                            dmc.Switch(
                                id={
                                    "type": "tables-code-switch",
                                    "index": key
                                },
                                size="xl",
                                onLabel="Code",
                                offLabel="Preview",
                            style={"marginTop": "-0.2rem", 'marginRight':'0.5rem'}),
                    ], gutter=0, grow=True, justify='space-around'),
                    ], inheritPadding=True, withBorder=True, py="xs"),

                html.Div(
                    id={
                        "type": "tables-rendering",
                        "index": key
                    },
                    children=[]
                )
            ]
        )

        children.append(new_sample)

    return children


@callback(
    Output({'type': 'tables-rendering', 'index': MATCH}, 'children'),
    Input({'type': 'tables-code-switch', 'index': MATCH}, 'checked'),
    State({'type': 'tables-code-switch', 'index': MATCH}, 'id')
)
def state_change(switch, id):

    filename = examples[id['index']]['file'].namelist()

    py_file = None
    css_file = None
    js_file = None
    for name in filename:

        if name.endswith('py'):
            py_file = examples[id['index']]['file'].read(name).decode('utf-8')

        if name.endswith('css'):
            css_file = examples[id['index']]['file'].read(name).decode('utf-8')

        if name.endswith('js'):
            js_file = examples[id['index']]['file'].read(name).decode('utf-8')


    if switch:
        return html.Div([
            dmc.Grid([
                dmc.GridCol([
                    dmc.Text("Python", p="xs"),
                    dmc.CodeHighlight(
                        language='python',
                        code=py_file,
                        style={'border': '1px solid #ececec'},
                        mr='1rem'
                    )], span=6),
                dmc.GridCol([
                    dmc.Group([
                        dmc.Text("CSS"), 
                        dmc.Text("Add to ./assets/style.css in your app", size='xs')
                    ], p='xs'),
                    dmc.CodeHighlight(
                        language='css',
                        code=css_file,
                        style={'border': '1px solid #ececec'}
                    ),
                    dmc.Group([
                        dmc.Text("JS"), 
                        dmc.Text("Add to ./assets folder in your app", size='xs')
                    ], p='xs'),
                    dmc.CodeHighlight(
                        language='js',
                        code=js_file,
                        style={'border': '1px solid #ececec'}
                    )
                ], span=6)
            ], gutter=0)
        ])
    else:
        image_file = u.get_example_image('tables', examples[id['index']]['image'])

        return dmc.Center(html.Img(src=f'data:image/png;base64,{image_file}'), p='xl')
