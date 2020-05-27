import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_bi_tr_grams = pd.read_csv(DATA_PATH.joinpath("bi_tri_grams_2.csv"))
entity_rec = pd.read_csv(DATA_PATH.joinpath("Entity_rec2.csv"))
lexical_disp = pd.read_csv(DATA_PATH.joinpath("lexical_dispersion2.csv"))

# df_bi_tr_grams = pd.read_csv("bi_tri_grams_1.csv")
# entity_rec = pd.read_csv("Entity_rec1.csv")


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Extractive Summary - The Governance of AI"),
                                    html.Br([]),
                                    html.P(
                                        "But some firms acknowledged that, incorrectly used, AI and ML techniques could give rise to new, complex risk types - and that could imply new challenges for boards and management. Nevertheless, promoting the right outcomes, even if framed as principle-based expectations, will require appropriate, up-to-date systems and controls across the three lines of defence to ensure an appropriate control environment throughout the firm. Either way, the transition to greater AI/ML-centric ways of working is a significant undertaking with major risks and costs arising from changes in processes, systems, technology, data handling/management, third-party outsourcing and skills. As the rate of introduction of AI/ML in financial services looks set to increase, so too does the extent of execution risk that boards will need to oversee and mitigate. For example, how would you know which issues are a function of poor design – the manufacturer’s fault if you have bought an ‘off the shelf’ technology product – or poor implementation –which could demonstrate incompetence or a lack of clear understanding from the firm’s management.",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Bigrams & Trigrams"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_bi_tr_grams)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Key words",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        14,
                                                        20,
                                                        20,
                                                        22,
                                                        24,
                                                    ],
                                                    y=[
                                                        'ML',
                                                        'AI/ML',
                                                        'data',
                                                        'AI',
                                                        "firms",
                                                    ],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Word frequency",
                                                    orientation='h',
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                hovermode="closest",
                                                legend={
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 0,
                                                    "b": 10,
                                                    "l": 35,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=330,
                                                xaxis={
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                },
                                                yaxis={
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Lexical Dispersion",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=lexical_disp['position'],
                                                    y=lexical_disp['word'],
                                                    line={"color": "#97151c"},
                                                    mode="markers",
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                title="",
                                                font={"family": "Raleway", "size": 10},
                                                height=160,
                                                width=340,
                                                hovermode="closest",
                                                margin={
                                                    "r": 20,
                                                    "t": 0,
                                                    "b": 20,
                                                    "l": 50,
                                                },
                                                xaxis={
                                                    "autorange": True,
                                                    "linecolor": "rgb(0, 0, 0)",
                                                    "showgrid": False,
                                                    "showline": True,
                                                    "title": "Word Offset",
                                                    "type": "linear",
                                                    'automargin': True,
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                                    "showgrid": True,
                                                    "type": "category",
                                                    'categoryorder':'array',
                                                    'categoryarray':['ML', 'data', 'AI', 'firms']
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Entity Recognition",
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(entity_rec)),
                                ],
                                className="six columns",
                            )
                        ],
                        className="row ",
                    ),
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )
