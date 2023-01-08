# DMC / DBC Building Blocks

#### This page is designed to be a collection of front end building blocks built in either [Dash Mantine Components](https://www.dash-mantine-components.com/) and [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) to plug and play into everyone's dash applications. 



## Contributors Guide
Thank you for contributing to the community supported `Dash Mantine & Dash Bootstrap Building Blocks` project!

## What are building blocks?
Building blocks are small UI components that are part of an app. These building blocks are not a full app but rather can be added into an existing app to enhance the UI/UX experience of your dash application.

## Code Review Checklist

### Basic Requirements
- [ ] Runs error free when added to an app running the latest version of dash, dash-bootstrap-components and/or dash-mantine-components.
- [ ] Has no errors in the browser's developer console
- [ ] Is a minimal example that only includes code necessary to display the building block
- [ ] Layout is responsive - i.e. is functional and looks nice in various browser window sizes
- [ ] Any required data is self-contained in the app or uses an external data source such as in [Plotly's repo (https://github.com/plotly/datasets).


### Style guide (suggestions only)

- [ ] Code is formatted with black

Naming conventions
- [ ] Uses descriptive variable names
- [ ] Uses python standard snake_case  variable names  ie `submit_button`
- [ ] In the `style` prop, uses camel case: ie `style={"textAlign": "center"}`


Concise code
- [ ] Uses concise syntax available in Dash>=2.0
For example use `dcc.Dropdown(df.columns)` rather than `dcc.Dropdown(options = [{'label':c, 'value':c} for c in df.columns]`
- [ ] Does not put callback `Input()`s `Output()`s or `State()`s in a list
- [ ] Does not include props that are set to the defaults for the component.  For example,  it's not necessary to include `multi=False` in the `dcc.Dropdown`.  Check the reference section of the docs to see the defaults for the components.
- [ ] Does not include unused imports
- [ ] Uses Minimal comments - only those necessary to describe "why" rather than just describing what the code does.
- [ ] Uses f-strings rather than `.format()`


In apps using `dash-bootstrap-components`:
- [ ] Uses `className` prop whenever possible instead of the  `style` prop. For example:  `className="bg-primary"` rather than `style={"backgroundColor": "blue"}`
- [ ] Uses `dbc.Container` as the outer container of the app rather than `html.Div`

In apps using both `dash-bootstrap-component`and `dash-mantine-components`
- [ ] Uses one library as the primary library and only uses the secondary library where necessary. 
