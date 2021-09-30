import dash
import pandas as pd
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('./input/dataset/aam_orders.csv')
animations = {
    'Bar': px.bar(
        df, x="Provider", y="Units", color="Type", 
        animation_frame="Month", animation_group="Units", 
        range_y=[0,310]),
}

app = dash.Dash(__name__)

app.layout = html.Div([
    html.P("Select an animation:"),
    dcc.RadioItems(
        id='selection',
        options=[{'label': x, 'value': x} for x in animations],
        value='Bar'
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"), 
    [Input("selection", "value")])
def display_animated_graph(s):
    return animations[s]

app.run_server(debug=True)