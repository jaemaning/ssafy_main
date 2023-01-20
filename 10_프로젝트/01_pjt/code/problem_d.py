import json

def max_revenue(movies):

    result = []

    for idx in range(len(movies)):
        # movies 에서 각 movie의 movie_id를 추출 하여 movies 폴더에서 각 파일을 엽니다.
        movie_id = movies[idx].get('id') 
        movie_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
        movie_dict = json.load(movie_json)

        # 이후 각 파일 안에 title / revenue 값을 찾아옵니다.
        title = movie_dict.get("title")
        revenue = movie_dict.get("revenue")
        result.append((title,revenue))

        # 이후 max_result 에 최고 revenue인 작품의 이름을 저장하여 리턴합니다.
        max_result = sorted(result,key=lambda x : x[1])[-1]

    return max_result[0]
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))