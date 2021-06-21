
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
app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'Tokyo', 'value': 'TKO'},
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
        value='TKO'
    ),
    
    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        id='demo-multi-dropdown',
        options=[
            {'label': 'Tokyo', 'value': 'TKO'},
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
        value=['TKO','NYC'],
        multi=True
    ),
    
    html.Label('Radio-Items'),
    dcc.RadioItems(
        id='demo-radio-button',
        options=[
            {'label': 'Tokyo', 'value': 'TKO'},
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
        value='TKO'
        
    ),
    
    html.Label('Checkboxes'),
    dcc.Checklist(
        id='demo-check-list',
        options=[
            {'label': 'Tokyo', 'value': 'TKO'},
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
        value=['TKO', 'NYC']
        
    ),
    html.Label('Text Input'),
    dcc.Input(value='New York City', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=1,
        max=5,
        marks={i: 'label{}'.format(i) for i in range(1,6)},
        value=0
    ),

    # カラムを分ける
], style={'columnCount': 3})

#アプリケーションの立ち上げ
if __name__ == '__main__':
    app.run_server(debug=True)
