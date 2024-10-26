from dash import html
import dash_mantine_components as dmc

head = dmc.AppShellHeader(
    p="sm",
    mb="1rem",
    children=[
        dmc.Grid([
            dmc.GridCol([
                dmc.Group([
                    html.Div([
                        dmc.Image(
                            src="/assets/logo.png"
                    )], style={'width': 50}),
                    dmc.Text(
                        "Dash Mantine & Dash Bootstrap Building Blocks",
                        size="xl",
                        c="dimmed"
                    )
                ], visibleFrom="md"),
                dmc.Text(
                    "DMC & DBC",
                    size="xl",
                    hiddenFrom="md",
                    c="dimmed"
                )
            ],
            span='auto'),
            dmc.GridCol(
                dmc.Group([
                    dmc.Anchor(
                        dmc.Avatar(
                            src="/assets/mantine.png"
                        ),
                        href="https://www.dash-mantine-components.com/",
                        target='_blank'
                    ),
                    dmc.Anchor(
                        dmc.Avatar(
                            src="/assets/plotly.png"
                        ),
                        href="https://dash.plotly.com/dash-ag-grid",
                        target='_blank'
                    ),
                        dmc.Menu(
                            [
                                dmc.MenuTarget(
                                    dmc.Avatar(
                                        src="/assets/dbc.png",
                                    style={'cursor': 'pointer'}),
                                ),
                                dmc.MenuDropdown(
                                    [
                                        dmc.MenuItem(
                                            "Docs",
                                            href="https://dash-bootstrap-components.opensource.faculty.ai",
                                            target="_blank"
                                        ),
                                        dmc.MenuItem(
                                            "Theme Explorer",
                                            href="https://hellodash.pythonanywhere.com/",
                                            target="_blank"
                                        )
                                    ]
                                ),
                            ]
                        )
                ], gap='xs', mt='6px'), span='content', p=0, pr='2rem'
            )
        ])
    ])