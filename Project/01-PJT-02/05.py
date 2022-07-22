import requests
from pprint import pprint


def credits(title):
    # 영화 제목으로 검색
    URL = 'https://api.themoviedb.org/3'
    path_s = '/search/movie'
    params_s = {
        'api_key': '37bb8661afe2c868dfe6c3aa758dff3a',
        'language': 'ko-KR',
        'query': title
    }
    response_s = requests.get(URL + path_s, params=params_s).json()
    
    # [1] 영화 id 가져오기
    movies = response_s.get('results')

    # 만약 검색된 영화가 없으면, 함수 종료
    if not movies:  return

    movie_id = movies[0].get('id')  # 영화 하나만

    # [2] 크레딧
    path_c = f'/movie/{movie_id}/credits'
    params_c = {
        'api_key': '37bb8661afe2c868dfe6c3aa758dff3a',
        'language': 'ko-KR'
    }
    response_c = requests.get(URL + path_c, params=params_c).json()

    casts = list()
    for cast in response_c.get('cast'):
        if cast.get('cast_id') < 10:
            casts.append(cast.get('name'))

    crew = list()
    for c in response_c.get('crew'):
        if c.get('department') == 'Directing':
            crew.append(c.get('name'))

    credits_info = dict()
    credits_info['cast'] = casts
    credits_info['crew'] = crew

    return credits_info


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
