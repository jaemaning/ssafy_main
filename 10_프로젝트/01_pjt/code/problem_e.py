import json


def dec_movies(movies):

    result = []


    for idx in range(len(movies)):
        # movies 에서 각 movie의 movie_id를 추출 하여 movies 폴더에서 각 파일을 엽니다.
        movie_id = movies[idx].get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
        movie_dict = json.load(movie_json)

        # 이후 각 파일 안에 title / realease_date 값을 찾아옵니다.
        title = movie_dict.get("title")
        release_date = movie_dict.get("release_date")

        # realease_date 의 5,6 번째 인덱스 값이 12이면 result 에 movie data 의 title 값을 저장합니다.
        if release_date[5:7] == "12" :
            result.append(title)
        

    return result
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
