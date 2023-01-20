import json


def max_revenue(movies):

    result = []

    for idx in range(len(movies)):
        movie_id = movies[idx].get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
        movie_dict = json.load(movie_json)

        title = movie_dict.get("title")
        revenue = movie_dict.get("revenue")
        result.append((title,revenue))

        max_result = sorted(result,key=lambda x : x[1])[-1]

    return max_result[0]
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))