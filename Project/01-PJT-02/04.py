import requests
from pprint import pprint


def recommendation(title):
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

    # [2] 추천 영화
    params_r = {
        'api_key': '37bb8661afe2c868dfe6c3aa758dff3a',
        'language': 'ko-KR'
    }

    recommended_movies = list()

    path_r = f'/movie/{movie_id}/recommendations'
    response_r = requests.get(URL + path_r, params=params_r).json()

    movie_info = response_r.get('results')  # 추천 영화의 정보
    
    for item in movie_info: # 정보 중 영화 제목만 가져오기
        title = item.get('title')
        recommended_movies.append(title)

    return recommended_movies


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
