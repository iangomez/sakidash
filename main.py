from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from components.layout import create_layout
from load_transform_data import load_data, transform

DATA_PATH = r"C:\Users\ianni\git\SakiBase\sakibase_archive.csv"

def main() -> None:

    # load and transform data
    sakibase = load_data(DATA_PATH)
    sakibase = transform(sakibase)

    # set up dash
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "SakiDash"
    app.layout = create_layout(app, sakibase)
    app.run_server(debug=True)


if __name__ == "__main__":
    main()