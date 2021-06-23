
import dash
import dash_core_components as dcc
import dash_html_components as html
from numpy import left_shift, right_shift
import plotly.graph_objs as go
import pandas as pd
import datetime


# 外部のスタイルシートを受け取る
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('assets/data.csv')

# date型に変更
import datetime

datetime.datetime.strptime(df['date'][44],'%Y/%m/%d').date()

dates = []
for _date in df['date']:
    date = datetime.datetime.strptime(_date,'%Y/%m/%d').date()
    dates.append(date)

# 受講生の数
n_subscribers = df['subscribers'].values

n_reviews = df['reviews'].values

# 受講生の差分
diff_subscribers = df['subscribers'].diff().values

# レビューの差分
diff_reviews = df['reviews'].diff().values

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div(children=[
    html.H2(children='Pythonによるwebスクレイピング〜アプリケーション編〜'),
    html.Div(children=[
        dcc.Graph(
            id='subscriber_grph',
            figure={
                'data': [
                    go.Scatter(
                        x=dates,
                        y=n_subscribers,
                        mode='lines+markers',
                        name='受講生総数',
                        opacity=0.7,
                        yaxis='y1'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_subscribers,
                        name='受講生の増加人数',
                        yaxis='y2'
                    )
                ],
                'layout': go.Layout(
                    title='受講生総数の推移',
                    xaxis=dict(title='date'),
                    yaxis=dict(title='受講生総数', side='left', showgrid=False,
                        range=[2500, max(n_subscribers)+ 100]),
                    yaxis2=dict(title='増加人数', side='right', overlaying='y', showgrid=False,
                        range=[0,max(diff_subscribers[1:])+ 100]), 
                    margin=dict(l=200, r=200,t=100)
                )
            }
        ),
        dcc.Graph(
            id='reviews_grph',
            figure={
                'data': [
                    go.Scatter(
                        x=dates,
                        y=n_reviews,
                        mode='lines+markers',
                        name='レビュー総数',
                        opacity=0.7,
                        yaxis='y1'
                    ),
                    go.Bar(
                        x=dates,
                        y=diff_reviews,
                        name='レビューの増加数',
                        yaxis='y2'
                    )
                ],
                'layout': go.Layout(
                    title='レビュー総数の推移',
                    xaxis=dict(title='date'),
                    yaxis=dict(title='レビューの総数', side='left', showgrid=False,
                        range=[200, max(n_reviews)+ 100]),
                    yaxis2=dict(title='増加数', side='right', overlaying='y', showgrid=False,
                        range=[0,max(diff_reviews[1:])+ 10]), 
                    margin=dict(l=200, r=200,t=100)
                )
            }
        )
    ])
],style={
    'textAlign': 'center',
    'width': '1200px',
    'margin': '0 auto'
})

#アプリケーションの立ち上げ
if __name__ == '__main__':
    app.run_server(debug=True)