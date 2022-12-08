from dash import html, Dash, dcc, Input, Output, callback
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px

app = Dash(__name__)

app.layout = dmc.Grid([
    dmc.Col([
        dmc.Paper([
            dcc.Location(id='url', refresh=False),
            dmc.Group([
                html.Div([
                    dmc.Title(order=5, children='11/23/2022'),
                    dmc.Title(order=1, children='42')
                ], style={'position': 'relative', 'z-index': '999'}),
                dcc.Graph(
                    id='spark',
                    config={
                        'displayModeBar': False,
                        'staticPlot': True
                    },
                    responsive=True,
                    style={'height': 60, 'margin': '-1rem'})
            ], direction='column', grow=True)
        ], shadow="xl", p="md", withBorder=True, style={'margin-bottom': "1rem"})
    ], span=6)
])


@callback(
    Output('spark', 'figure'),
    Input('url', 'pathname')
)
def update_page(url):

    area_df = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 3, 5, 7]
    })

    fig = px.area(
        area_df,
        x="x", y="y",
        template='simple_white',
        log_y=True
    )

    fig.update_yaxes(visible=False),
    fig.update_xaxes(visible=False),
    fig.update_traces(
        line={'color': 'rgba(31, 119, 180, 0.2)'},
        fillcolor='rgba(31, 119, 180, 0.2)'
    ),
    fig.update_layout(
        margin={'t': 0, 'l': 0, 'b': 0, 'r': 0}
    )

    return fig


if __name__ == '__main__':
    app.run_server(
        debug=True,
    )