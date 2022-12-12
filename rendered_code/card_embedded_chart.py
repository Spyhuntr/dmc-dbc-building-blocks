from dash import html, Dash, dcc, Input, Output, callback
import dash_mantine_components as dmc
import pandas as pd
import plotly.express as px
from datetime import datetime

app = Dash(__name__)

app.layout = dmc.Grid([
    dmc.Col([
        dmc.Paper([
            dcc.Location(id='url', refresh=False),
            dmc.Group([
                html.Div([
                    dmc.Title(id='tot-inv-title', order=5),
                    dmc.Title(id='tot-inv', order=1)
                ], style={'position': 'relative', 'z-index': '999'}),
                dcc.Graph(
                    id='tot-spark',
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
    [Output('tot-inv', 'children'),
     Output('tot-spark', 'figure'),
     Output('tot-inv-title', 'children')],
    Input('url', 'pathname')
)
def update_page(url):

    area_df = pd.DataFrame({
        'x': [20, 18, 489, 675, 1776],
        'y': [4, 25, 281, 600, 1900]
    }, index=[1990, 1997, 2003, 2009, 2014])

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

    kpi_val = f'42'

    now = datetime.now()
    tot_inv_title = now.strftime('%m/%d/%Y')

    return kpi_val, fig, tot_inv_title


if __name__ == '__main__':
    app.run_server(
        debug=True
    )