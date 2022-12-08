from dash import html, Dash, dcc
import dash_mantine_components as dmc

app = Dash(__name__,
           external_stylesheets=[
               'https://use.fontawesome.com/releases/v5.8.1/css/all.css'
           ]
           )

app.layout = html.Div([
    dmc.MediaQuery([dmc.Navbar(
        fixed=True,
        width={"base": 250},
        height="100%",
        style={"top": 0},
        children=[
            dmc.Group(
                direction="column",
                grow=True,
                spacing="xl",
                children=[
                    dmc.List(
                        center=True,
                        children=[
                            dmc.ListItem(
                                dcc.Link('Home', href='/'),
                                icon=[
                                    html.I(className='fas fa-home fa-fw fa-lg')],
                                class_name='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('Data', href='/analytics'),
                                icon=[
                                    html.I(className='fas fa-chart-bar fa-fw fa-lg')],
                                class_name='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('Map', href='/map'),
                                icon=[
                                    html.I(className='fas fa-map fa-fw fa-lg')],
                                class_name='nav-list-items'),

                            dmc.ListItem(
                                dcc.Link('More Maps',
                                         href='/distro'),
                                icon=[
                                    html.I(className='fas fa-map-marker fa-fw fa-lg')],
                                class_name='nav-list-items'),
                        ])
                ])
        ])], smallerThan="md", styles={'display': 'none'}),
    dmc.MediaQuery([dmc.Navbar(
        fixed=True,
        width={"base": 60},
        height="100%",
        style={"top": 0},
        children=[
            dmc.List(
                center=True,
                children=[
                    dmc.ListItem(
                        dcc.Link(
                            html.I(className='fas fa-home fa-fw fa-lg'), href='/'),
                        class_name='nav-list-items'
                    ),
                    dmc.ListItem(
                        dcc.Link(
                            html.I(className='fas fa-chart-bar fa-fw fa-lg'), href='/'),
                        class_name='nav-list-items'
                    ),
                    dmc.ListItem(
                        dcc.Link(
                            html.I(className='fas fa-map fa-fw fa-lg'), href='/'),
                        class_name='nav-list-items'
                    ),
                    dmc.ListItem(
                        dcc.Link(
                            html.I(className='fas fa-map-marker fa-fw fa-lg'), href='/'),
                        class_name='nav-list-items'
                    )
                ])
        ])], largerThan="md", styles={'display': 'none'})
])

if __name__ == '__main__':
    app.run_server(
        host='0.0.0.0',
        port=8050,
        debug=True,
        dev_tools_props_check=True
    )



#Uncomment and add the following code into your style.css file
# body, .mantine-Header-root {
#     background-color: #f2f4f6 !important;
# } 

#  .mantine-Navbar-root {
#     background-color: #1f2937!important;
# }

# .mantine-Anchor-root {
#     color: #fff!important;
# }
# .nav-list-items {
#     padding: 1rem;
#     color: #fff!important;
#     text-decoration: none;
#     list-style: none;
# }

# .nav-list-items:hover {
#     color: #f2f4f6!important;
#     background-color: #374151!important;
# }

# .mantine-Navbar-root a:-webkit-any-link{
#     text-decoration: none;
#     color: #f2f4f6 !important;
# }

# .mantine-Navbar-root ::marker{
#     display: none;
# }