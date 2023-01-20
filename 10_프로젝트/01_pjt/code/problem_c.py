import json
from pprint import pprint


def movie_info(movies, genres):

    movies_list = []

    for idx in range(len(movies)) :

        genres_ids = movies[idx].get("genre_ids")
        genre_list = []

        for genre_id in genres_ids:
            for genre in genres:
                if genre["id"] == genre_id:
                    genre_list.append(genre["name"])

        new_dict = {
            "id": movies[idx].get("id"),
            "title": movies[idx].get("title"),
            "poster_path": movies[idx].get("poster_path"),
            "vote_average": movies[idx].get("vote_average"),
            "overview": movies[idx].get("overview"),
            "genre_names": genre_list
        }

        movies_list.append(new_dict)

    
    return movies_list
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))