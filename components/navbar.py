from dash import html
import dash_mantine_components as dmc

head = dmc.Header(
    height=60,
    p="sm",
    mb="1rem",
    children=[
        dmc.Grid([
            dmc.Col([
                dmc.MediaQuery([
                    dmc.Group([
                        dmc.Image(
                            src="/assets/logo.png", width=50
                        ),
                        dmc.Text(
                            "Dash Mantine & Dash Bootstrap Building Blocks",
                            size="xl",
                            color="gray",
                        )], p=0, m=0)
                ], smallerThan='md', styles={'display': 'none'}),
                dmc.MediaQuery([
                    dmc.Text(
                        "DMC & DBC",
                        size="xl",
                        color="gray",
                    )
                ], largerThan='md', styles={'display': 'none'})],
                span=10, lg=10, md=10, sm=11, xs=11, p='sm'),
            dmc.Col([
                dmc.MediaQuery([
                    dmc.Group([
                        dmc.Anchor(
                            dmc.Avatar(
                                src="/assets/mantine.png"
                            ),
                            href="https://www.dash-mantine-components.com/",
                            pl='1rem',
                            target='_blank'
                        ),
                        dmc.Menu(
                            [
                                dmc.MenuTarget(dmc.ActionIcon(
                                    dmc.Avatar(src="/assets/dbc.png"))),
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
                    ], mt='6px')
                ], smallerThan='md', styles={'display': 'none'}),
                dmc.MediaQuery([
                    dmc.Menu(
                        [
                            dmc.MenuTarget(dmc.ActionIcon(
                                html.I(className='fas fa-bars fa-2x fa-fw'))),
                            dmc.MenuDropdown(
                                [
                                    dmc.MenuItem(
                                        "Dash Mantine Components",
                                        icon=dmc.Avatar(
                                            src="/assets/mantine.png",
                                            size='sm'
                                        ),
                                        href="https://www.dash-mantine-components.com/",
                                        target="_blank"
                                    ),
                                    dmc.MenuDivider(),
                                    dmc.MenuItem(
                                        "Dash Bootstrap Components",
                                        icon=dmc.Avatar(
                                            src="/assets/dbc.png",
                                            size='sm'
                                        ),
                                        href="https://dash-bootstrap-components.opensource.faculty.ai",
                                        target="_blank"
                                    ),
                                    dmc.MenuItem(
                                        "Dash Bootstrap Theme Explorer",
                                        icon=dmc.Avatar(
                                            src="/assets/dbc.png",
                                            size='sm'
                                        ),
                                        href="https://hellodash.pythonanywhere.com/",
                                        target="_blank"
                                    ),
                                ]
                            ),
                        ], style={'paddingTop': '0.7rem'}
                    ),
                ], largerThan='md', styles={'display': 'none'})
            ], span=2, lg=2, md=2, sm=1, xs=1, p=0)
        ])
    ])
