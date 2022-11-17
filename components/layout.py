from dash import Dash, dcc, html
from dash.dependencies import Input, Output
from . import business, today

def create_layout(app: Dash, sakibase) -> html.Div:
    return html.Div(
        className="",
        children=[
            html.H3(
                app.title,
                className="p-3 bg-dark text-white"
            ),
            html.Div(
                className="",
                children=[
                    today.render(app, sakibase),
                    business.render(app, sakibase)
                ],
            ),
        ],
    )


