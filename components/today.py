from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
from . import ids
import pandas as pd

def render(app: Dash, sakibase) -> html.Div:    
    
    today = pd.Timestamp.today().date()
    mask = (sakibase['time'].dt.date == today)
    df_today = sakibase[mask]

    return html.Div(
        "test",
        id=ids.TODAY_GLANCE,
        className="app-div"
    )
