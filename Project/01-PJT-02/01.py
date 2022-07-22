import requests


def popular_count():
    URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '37bb8661afe2c868dfe6c3aa758dff3a',
        'language': 'ko-KR'
    }
    response = requests.get(URL + path, params=params).json()
    
    return len(response.get('results'))


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20