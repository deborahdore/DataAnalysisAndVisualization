import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash, html, dash_table, dcc, callback, Output, Input

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container([
    dbc.Row([
        html.Div(children="My App",
                 className="text-primary text-center fs-3"
                 )
    ]),

    dbc.Row([
        dbc.RadioItems(options=[{'label': x, 'value': x} for x in ['pop', 'lifeExp', 'gdpPercap']],
                       value='lifeExp',
                       id='controls-and-radio-item',
                       inline=True
                       )
    ]),

    dbc.Row([
        dbc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=10)
        ], width=6),

        dbc.Col([
            dcc.Graph(figure={}, id='controls-and-graph')
        ], width=6)
    ])
], fluid=True)


@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig


if __name__ == '__main__':
    app.run(debug=True)
