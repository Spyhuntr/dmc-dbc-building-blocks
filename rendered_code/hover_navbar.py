import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.MATERIA, dbc.icons.FONT_AWESOME],
)


sidebar = html.Div(
    [
        html.Div(
            [
                html.H2("Auto ML", style={"color": "white"}),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [html.I(className="fas fa-home me-2"), html.Span("Dashboard")],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-calendar-alt me-2"),
                        html.Span("Projects"),
                    ],
                    href="/projects",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fas fa-envelope-open-text me-2"),
                        html.Span("Datasets"),
                    ],
                    href="/datasets",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)

app.layout = html.Div(
    [
        sidebar,
        html.Div(
            [
                dash.page_container
            ],
            className="content",
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)



#Uncomment and add the following code into your style.css file
# /* This creates a skinny side bar fixed to the left of the page */
# .sidebar {
#   position: fixed;
#   top: 0;
#   left: 0;
#   bottom: 0;
#   width: 5rem;
#   padding: 2rem 1rem;
#   background-color: #cbd3dd;
#   z-index: 1050;
#   transition: width 0.1s ease-in-out;
# }

# /* when the user hovers on the sidebar, expand it */
# .sidebar:hover {
#   width: 16rem;
# }

# /* make sure the contents of the navlink don't wrap when navbar collapses */
# .sidebar .nav-link {
#   width: 100%;
#   overflow: hidden;
#   white-space: nowrap;
# }

# /* fix the width of the icons */
# .sidebar .nav-link i {
#   width: 1rem;
# }

# /* hide the navlink labels by default */
# .sidebar .nav-link span {
#   visibility: hidden;
#   opacity: 1;
#   transition: opacity 0.1s ease-in-out;
# }

# /* when the sidebar is hovered, reveal the labels */
# .sidebar:hover .nav-link span {
#   visibility: visible;
#   opacity: 1;
#   color: black;
# }

# /* container for the sidebar header. make sure the contents don't wrap when
#  * the sidebar is collapsed.
#  */
# .sidebar-header {
#   display: flex;
#   justify-content: left;
#   align-items: center;
#   overflow: hidden;
#   white-space: nowrap;
# }

# /* position the header relative to the logo and hide by default */
# .sidebar-header h2 {
#   opacity: 0;
#   margin-left: 1rem;
#   margin-bottom: 0;
#   transition: opacity 0.1s ease-in-out;
# }

# /* reveal the header when the sidebar is toggled */
# .sidebar:hover .sidebar-header h2 {
#   opacity: 1;
# }

# /* position the content relative to the collapsed sidebar */
# .content {
#   margin-left: 7rem;
#   margin-right: 2rem;
#   padding: 2rem 1rem;
# }