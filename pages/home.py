
import dash
from dash import html
import dash_mantine_components as dmc

dash.register_page(__name__, path='/', title='Home')

layout = dmc.Grid(
    children=[
        dmc.Col([
            dmc.Paper(
                children=[
                    dmc.Anchor(
                        href="/app_cards",
                        children=[
                            html.Div(
                                dmc.Image(
                                    src="/assets/cards-light.svg",
                                ), className='card-hdr'
                            ),
                            dmc.Text(
                                "Application Cards",
                                pt="md",
                                pl="md"
                            ),
                            dmc.Text(
                                "2 Component",
                                size="xs",
                                pl="md",
                                pb="md",
                                color="#868e96"
                            )
                        ],
                        variant="text"
                    )],
                shadow="xl",
                withBorder=True,
                radius="md",
                style={"overflow": "hidden"}
            )], span=3),
       dmc.Col([
            dmc.Paper(
                children=[
                    dmc.Anchor(
                        href="/navbars",
                        children=[
                            html.Div(
                                dmc.Image(
                                    src="/assets/navbars-light.svg",
                                ), className='card-hdr'
                            ),
                            dmc.Text(
                                "Navbars",
                                pt="md",
                                pl="md"
                            ),
                            dmc.Text(
                                "1 Component",
                                size="xs",
                                pl="md",
                                pb="md",
                                color="#868e96"
                            )
                        ],
                        variant="text"
                    )],
                shadow="xl",
                withBorder=True,
                radius="md",
                style={"overflow": "hidden"}
            )], span=3)
    ])
