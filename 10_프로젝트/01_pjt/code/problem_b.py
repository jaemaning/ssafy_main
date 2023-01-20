import json
from pprint import pprint


def movie_info(movie, genres):
    genres_ids = movie.get("genre_ids")  # movie.json 파일에서 genre_ids 값을 가져옴
    genre_list = []

    # genre_ids 값이 여러개일수 있으므로 for문으로 genre.json 파일 탐색
    for genre_id in genres_ids: 
        for genre in genres:
            if genre["id"] == genre_id: # 같은 id를 가질경우 값을 genre_list에 어펜드
                genre_list.append(genre["name"])

    # new_dict 재구성
    new_dict = {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "poster_path": movie.get("poster_path"),
        "vote_average": movie.get("vote_average"),
        "overview": movie.get("overview"),
        "genre_names": genre_list
    }

    return new_dict
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
