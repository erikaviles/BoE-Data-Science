import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from pages import (
    doc1,
    doc2,
    doc3
)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server


# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)

# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/dash-financial-report/doc2":
        return doc2.create_layout(app)
    elif pathname == "/dash-financial-report/doc3":
        return doc3.create_layout(app)
    elif pathname == "/dash-financial-report/full-view":
        return (
            doc1.create_layout(app),
            doc2.create_layout(app),
            doc3.create_layout(app)
        )
    else:
        return doc1.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=True)
