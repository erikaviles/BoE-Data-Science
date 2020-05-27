import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()


df_bi_tr_grams = pd.read_csv(DATA_PATH.joinpath("bi_tri_grams_1.csv"))
entity_rec = pd.read_csv(DATA_PATH.joinpath("Entity_rec1.csv"))
lexical_disp = pd.read_csv(DATA_PATH.joinpath("lexical_dispersion1.csv"))

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
                                    html.H5("Extractive Summary - Cyborg Supervision"),
                                    html.Br([]),
                                    html.P(
                                        "So – along the same lines pursued by law firms for example – one big win is the ability to produce structured data from a range of sources, the analysis of which traditionally required significant manual effort. For example, while ML models could alter banks’ trading and retail businesses – enabling them to make better decisions more quickly – the opacity, however, of these models may also make them more difficult for humans to understand. At the macroeconomic level, changes in technology, including AI, could, over time, profoundly affect the nature of the financial services consumed and may result inchanges to the structure of the financial services industry. A typical problem faced by supervisors, for example, is the ‘needle-in-a-haystack’ problem: if something is going wrong in a firm, it can be necessary to find out who in the firm made relevant decisions, based on what information, and why the checks and balances of the firm – the board, and second and third lines of defence – did not work. To achieve complex supervisory outcomes – which often require significant, multi-year remediation by firms – boards and senior management of firms have to understand the context and rationale for what we are trying to achieve, as well as what we would deem to be a successful outcome.",
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
                                                        11,
                                                        12,
                                                        12,
                                                        20,
                                                        27,
                                                    ],
                                                    y=[
                                                        'supervisory',
                                                        'ML',
                                                        'machine',
                                                        'firms',
                                                        "data",
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
                                                    "l": 50,
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
                                                    'categoryarray':['supervisory', 'ML', 'machine', 'firms', 'data']
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
