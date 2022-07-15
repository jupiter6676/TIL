# 06. JSON 데이터 활용 - 영화 다중 정보 활용
# 영화 데이터 movies.json와 genres.json을  활용하여 필요한 정보로만 구성된 리스트를 출력하시오.
# 코드는 선언된 함수 내에 작성하며, 결과 딕셔너리를 반환합니다.
# JSON으로 가져온 데이터가 함수의 인자로 전달됩니다.

# 전체 영화 정보는 평점 높은 20개의 영화 데이터입니다.
# 개별 영화 데이터는 id, title, vote_average, overview, genre_names로 구성된 딕셔너리입니다.
# genre_names는 각 장르 정보를 값으로 가집니다.
# genre_ids를 장르 번호에 맞는 name 값으로 대체합니다.


import json
from pprint import pprint
from operator import itemgetter


# movies, genres: list
def movie_info(movies, genres):
    # 별점이 높은 순서대로, 리스트 속 딕셔너리 정렬
    movies_sorted_by_vote = sorted(movies, key=itemgetter('vote_average'), reverse=True)
    
    info = dict()
    movies_info_list = list()
    
    # 정렬된 리스트 속 딕셔너리 탐색
    for m in movies_sorted_by_vote:
        genre_ids = m.get('genre_ids')  # [18, 80]
        genre_names = list()

        # id에 따른 장르 이름 리스트 반환
        for id in genre_ids:
            for g in genres:
                if id == g.get('id'):
                    genre_names.append(g.get('name'))

        # 영화마다 필요한 정보 담기
        info = {
            'genre_names': genre_names,
            'id': m.get('id'),
            'overview': m.get('overview'),
            'title': m.get('title'),
            'vote_average': m.get('vote_average')
        }

        # 영화 정보들이 담긴 딕셔너리를 리스트에 추가
        movies_info_list.append(info)
    
    return movies_info_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))