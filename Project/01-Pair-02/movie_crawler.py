import os
from urllib.parse import urlparse
from urllib.request import urlopen
import django
import re
import requests
from bs4 import BeautifulSoup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pair_pjt.settings')
django.setup()

from reviews.models import Movie

url = 'https://movie.naver.com/movie/running/current.naver'

req = urlopen(url)
byte_data = req.read()

# html 파싱
text_data = byte_data.decode("utf-8")
html = BeautifulSoup(text_data, 'html.parser')

# 상영중 영화 주 정보 30개 element 수집(li 태그 30개 수집)
movie_list = html.select('div[class="lst_wrap"] > ul[class="lst_detail_t1"] > li', limit=30)

# a 태그의 href 속성 수집(url)
base_url = 'https://movie.naver.com'
urls = []
for li in movie_list:
    a_tag = li.select_one('div[class="thumb"] > a')
    urls.append(base_url + a_tag.get('href'))


# 영화 사이트 이동 : 영화 제목과 줄거리 저장
def get_movie_data(url):
    # url 요청
    request = urlopen(url)
    byte_data = request.read()
    # 디코딩
    text_data = byte_data.decode("utf-8")
    # html 파싱
    html = BeautifulSoup(text_data, 'html.parser')
    soup = html.find("div", class_="poster")
    # tag & 내용 수집
    title = html.select_one('div[class="mv_info"] > h3[class="h_movie"] > a').string
    summary = html.select_one('div[class="story_area"] > p').text
    img = soup.find('img')["src"]


    # dictionary로 저장
    context = {
        'title':title,
        'summary':summary,
        'img':img[:-15],
    }

    return context




def add_data():
    result =[]

    # 자료 수집 함수 실행
    for url in urls:
        tmp = get_movie_data(url)
        # 만들어진 dic를 리스트에 저장
        result.append(tmp)

    # DB에 저장
    for item in result:
        Movie(title=item['title'],
              img=item['img'],
              summary=item['summary'],).save()

    return result

# DB 저장 함수 강제 실행(임시로 실행)
add_data()