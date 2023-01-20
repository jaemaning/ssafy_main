import json
import problem_b
from pprint import pprint


def movie_info(movies, genres):

    movies_list = []

    # problem_b 에서 쓴 코드를 모듈화 하여 재사용
    for movie in movies :

        new_dict = problem_b.movie_info(movie, genres)

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