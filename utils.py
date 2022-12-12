
import dash_mantine_components as dmc

def card_hdr(title: str, user: str):

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


def build_contributors():

    contributors = ['snehilvj', 'tcbegley', 'AnnMarieW', 'Spyhuntr', 'Sohibjon']
    contrib_group = []
    for contributor in contributors:

        new_link = dmc.Anchor(
            dmc.Tooltip(
                label=contributor,
                withArrow=True,
                transition="pop-top-right",
                transitionDuration=300,
                children=[
                    dmc.Avatar(
                        src=f"https://github.com/{contributor}.png", radius="xl"
                    )
                ]
            ),
            href=f"https://github.com/{contributor}",
            pl='1rem',
            target='_blank'
        )

        contrib_group.append(new_link)

    return contrib_group
