import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_bi_tr_grams = pd.read_csv(DATA_PATH.joinpath("bi_tri_grams_3.csv"))
entity_rec = pd.read_csv(DATA_PATH.joinpath("Entity_rec3.csv"))
lexical_disp = pd.read_csv(DATA_PATH.joinpath("lexical_dispersion3.csv"))

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
                                    html.H5("Extractive Summary - Supervisor-centred automation"),
                                    html.Br([]),
                                    html.P(
                                        "At the extreme, there is the “pull” model of data collection, implicitly described in the example I used in the introduction to these remarks - in which regulators would be able to pull data, at any level of granularity, directly from firms’ systems in real time, with no intervention on the part of firms. A more strategic approach, however, is likely to prove necessary to make a reality of a longer-term goal of embedding technology at the heart of how prudential risks are supervised – that is, not simply identifying applications in supervision that would benefit from technology, but fundamentally re-engineering the way we work. Providing answers to the questions I have outlined in the preceding remarks will help us to know how far we might, in time, go in introducing technology into supervision, and provide a road map for the future of how prudential supervision could be done. For example, by more consistently applying meta-data and tabs to not just the rule book, but also the related library of supervisory expectations, it would become easier and quicker for a more or less intelligent search engine to find and collect together all the relevant and related pieces of regulatory and supervisory text. Gradually over time, advances in technology and modelling techniques should – I believe – make more possible the type of flexible desk-top simulations of banks’ balance sheets imagined in my example - just as an earlier generation of technology enabled, some  years ago, quick-fire desk-top simulations of the effect of shocks on the macro economy: but there remain significant technical and practical challenges to overcome.",
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
                                                        15,
                                                        17,
                                                        22,
                                                        24,
                                                        28,
                                                    ],
                                                    y=[
                                                        'way',
                                                        'supervision',
                                                        'firms',
                                                        'technology',
                                                        "data",
                                                    ],
                                                    orientation='h',
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Word frequency",
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
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
                                                    "l": 50,
                                                },
                                                showlegend=True,
                                                title="",
                                                width=330,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
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
                                                    'categoryarray':['way', 'supervision', 'firms', 'technology', 'data'],
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
