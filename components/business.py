from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd

def render(app: Dash, sakibase) -> html.Div:
    # @app.callback(
    #     Output(ids.BAR_CHART, "children"),
    #     [
    #         Input(ids.NATION_DROPDOWN, "value"),
    #     ],
    # )

    # create business plot
    sakibase_grouped = sakibase.groupby("history")
    # one liner to pull Pee as well as Pee and Poop into a histogram
    data_pee = pd.concat([sakibase_grouped.get_group(value) for value in ["Pee", "Pee and Poop"]]).groupby("date").count().reset_index()
    fig = px.bar(data_pee, x='date', y='history', title="Business")

    return html.Div(
        dcc.Graph(figure=fig),
        className="app-div",
        id=ids.BUSINESS_CHART
    )
