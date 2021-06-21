
import dash
import dash_core_components as dcc
import dash_html_components as html

# 外部のスタイルシートを受け取る
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': 'black',
    'text': 'white'
}

# アプリのレイアウト 要素が3つに分かれている(h1, div, graph)
app.layout = html.Div(children=[
    html.H1(
        children='Hello World',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'background': colors['background']
        }

        ),

    html.Div(
        children='''
        Dash: A web application framework for Python.
        ''',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'background': colors['background']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ["ryo", "takumi", "tsuyoshi"], 'y': [7, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': ["ryo", "takumi", "tsuyoshi"], 'y': [7, 4, 5], 'type': 'bar', 'name': 'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }

            }
        }
    )
])

#アプリケーションの立ち上げ
if __name__ == '__main__':
    app.run_server(debug=True)
