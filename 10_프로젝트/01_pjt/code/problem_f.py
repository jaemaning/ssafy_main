'''
제공된 영화 데이터를 사용하여 내가 원하는 데이터를 추출하고
나만의 데이터 구조를 만들어봅니다.
•예시
•90년대 개봉작 중 많은 수입을 올린 영화 순위
•배급한 영화가 많은 순으로 배급사 정렬하기
'''

import json

### 90s 개봉작 중 많은 수입을 올린 영화 rank

def rank90_movies(movies):

    result = []
    
    
    for idx in range(len(movies)):
        # movies 에서 각 movie의 movie_id를 추출 하여 movies 폴더에서 각 파일을 엽니다.
        movie_id = movies[idx].get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
        movie_dict = json.load(movie_json)

        # 이후 각 파일 안에 title / realease_date 값을 찾아옵니다.
        title = movie_dict.get("title")
        release_date = movie_dict.get("release_date")
        revenue = movie_dict.get("revenue")

        # release_date 앞에 2글자를 뽑아 "19" 이면 (1900s) 영화이면 영화 제목과 수익을 result에 어펜드
        if release_date[:2] == "19" :
            result.append({"제목" : title,"수익" : revenue})
        
    # 수익을 기준으로 내림차순 정렬후 리턴
    result = sorted(result, key=lambda x : x["수익"], reverse=True)

    return result


### 배급한 영화가 많은 순으로 배급사 정렬하기.

def count_production_companies(movies):

    result = []
    count_list = []

    for idx in range(len(movies)):
        # movies 에서 각 movie의 movie_id를 추출 하여 movies 폴더에서 각 파일을 엽니다.
        movie_id = movies[idx].get('id')
        movie_json = open(f'data/movies/{movie_id}.json', encoding='utf-8')
        movie_dict = json.load(movie_json)

        # 이후 각 파일 안에 production_companies 값을 찾아옵니다.
        production_companies = movie_dict.get("production_companies")

        # production_companies 값이 리스트로 여러개 일 수도 있으므로 for 문으로 탐색
        for company in production_companies:
            # 제작사 company 값이 이미 result에 저장되어 있으면 따로 저장.
            if company["name"] in result :
                count_list.append(company["name"])
            else :
                result.append(company["name"])

    new_result = []

    # 이후 영화 제작사마다 얼마나 많은 영화를 제작했는지 카운팅.
    for company_name in result:
        counting_movie = count_list.count(company_name)
        new_result.append([company_name,counting_movie+1])

    # 제작 수를 내림차순 정렬 후 리턴
    return sorted(new_result, key=lambda x : x[1],reverse=True)



    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(rank90_movies(movies_list),end="\n\n")
    print(count_production_companies(movies_list))