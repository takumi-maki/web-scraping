import re
import requests
from bs4 import BeautifulSoup

from assets.database import db_session
from assets.models import Data

import datetime

def get_udemy_info():
    url = 'https://scraping-for-beginner.herokuapp.com/udemy'

    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    # 名前を取得
    name = soup.select('.card-title')[0].string

    # 受講者数
    n_subscribers = soup.select('.subscribers')[0].string
    n_subscribers = int(n_subscribers.split('：')[1])

    # レビュー数
    n_reviews = soup.select('.reviews')[0].string
    n_reviews = int(n_reviews.split('：')[1])

    results = {
        'name': name,
        'n_subscribers': n_subscribers,
        'n_reviews': n_reviews
    }
    return  results

def write_data():
    # 新規データの読み込み
    _results = get_udemy_info()

    # 今日の日付、受講者数、レビュー数を取得
    date = datetime.date.today()
    subscribers = _results['n_subscribers']
    reviews = _results['n_reviews']

    row = Data(date=date, subscribers=subscribers, reviews=reviews)
    
    db_session.add(row)
    db_session.commit()


if __name__ == "__main__":
    write_data()