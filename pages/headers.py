
import dash
from dash import callback, Output, Input, State, MATCH, html, dcc
import dash_mantine_components as dmc
import utils as u

dash.register_page(__name__, path='/headers', title='Headers')
prefix = 'examples/headers/'

examples = u.get_example_files(prefix)

layout = dmc.Grid(
    children=[
        dmc.GridCol(
            dcc.Link(
                id='headers_back_btn',
                href="/",
                children=[
                    dmc.Button("< Back to all categories", variant="outline")
                ])
        ),
        dmc.GridCol(
            dmc.Title("Headers", order=1)
        ),
        dmc.GridCol(
            id="headers-sample-container",
            children=[]
        )
    ])


@callback(
    Output('headers-sample-container', 'children'),
    Input('headers-sample-container', 'children')
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
                                    "type": "headers-code-switch",
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
    Input({'type': 'headers-code-switch', 'index': MATCH}, 'checked'),
    State({'type': 'headers-code-switch', 'index': MATCH}, 'id')
)
def build_examples(switch, id):

    filename = examples[id['index']]['file'].namelist()[0]

    if switch:

        if filename.endswith(('py', 'css')):
            return dmc.CodeHighlight(
                language='python',
                code=examples[id['index']]['file'].read(filename).decode('utf-8')
            )

    else:
        
        image_file = u.get_example_image('headers', examples[id['index']]['image'])

        return dmc.Center(html.Img(src=f'data:image/png;base64,{image_file}'), p='xl')
