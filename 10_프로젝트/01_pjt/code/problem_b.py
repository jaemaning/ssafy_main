import json
from pprint import pprint


def movie_info(movie, genres):
    genres_ids = movie.get("genre_ids")
    genre_list = []

    for genre_id in genres_ids:
        for genre in genres:
            if genre["id"] == genre_id:
                genre_list.append(genre["name"])

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
