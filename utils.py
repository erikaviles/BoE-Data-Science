import dash_html_components as html
import dash_core_components as dcc


def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div(
        [
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("pra.jpg"),
                        className="logo",
                    ),
                    html.A(
                        html.Button("By Erik Aviles", id="learn-more-button"),
                        href="https://www.linkedin.com/in/erik-aviles/",
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Speech Analysis")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Full View",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
        ],
        className="row",
    )
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Cyborg Supervision",
                href="/dash-financial-report/doc1",
                className="tab first",
            ),
            dcc.Link(
                "The governance of AI",
                href="/dash-financial-report/doc2",
                className="tab",
            ),
            dcc.Link(
                "Supervisor-centred automation",
                href="/dash-financial-report/doc3",
                className="tab",
            ),
        ],
        className="row all-tabs",
    )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]], style={'padding-left': '10px'}))
        table.append(html.Tr(html_row))
    return table
