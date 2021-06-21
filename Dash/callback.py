
import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

# 外部のスタイルシートを受け取る
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Input(id='input-div', value='initial value', type='text'),
    html.Div(id='output-div')
])
# input_valueが変化あるたびに、output-divのchildrenに反映される
@app.callback(
    Output(component_id='output-div', component_property='children'),
    [Input(component_id='input-div', component_property='value')]
)
def update(input_value):
    return 'You entered {}'.format(input_value)

#アプリケーションの立ち上げ
if __name__ == '__main__':
    app.run_server(debug=True)
