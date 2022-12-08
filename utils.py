
import dash_mantine_components as dmc
from dash import html


def build_code(code):
    return dmc.Code([code], block=True, style={"fontSize": "13px"})


def card_hdr(title: str, user: str, code_key: int):

    link = dmc.Anchor(
        href=f"https://github.com/{user}",
        children=['@' + user],
        size="xs",
        ml="-0.7rem",
        style={'color': 'rgb(134, 142, 150)'})

    return dmc.Col(
        children=[
            dmc.Group([
                dmc.Text(
                    title,
                    size="xl"
                ),
                dmc.Text(
                    'Made by',
                    size="xs"
                ),
                link,
]
            )], span=10)
