# 학습한 내용, 어려웠던 부분, 새로 배운 것들 및 느낀 점 등을 상세히 기록
<br />

## 학습한 내용

- json 파일 형태로 저장된 파일을 python 을 이용해 자료를 활용하는 법을 학습하였습니다.
- python 에서 dictionary 형태와 json 파일 형태가 유사한 점을 이용해 json 라이브러리만 활용을 잘한다면 쉽게 이용 가능한 점이 좋았습니다.
- fstring 을 활용하여 데이터 이름이 바뀌었을때 접근 하는 방법을 학습하였습니다.
- string 자료 slicing 하는 방법을 학습하였습니다.

<br />

## 어려웠던 부분

- 크게 어려운 부분은 없었지만, json 파일이 익숙하지는 않아 json 파일을 불러오고 자유자제로 활용하는 부분이 어려웠습니다.

<br />

## 새로 배운 것들 

- json 라이브러리를 활용하는 것을 배웠습니다.
- python dictionary 자료구조를 활용하여 데이터를 추출해 내는것들을 새롭게 배웠습니다.

<br />

## 느낀 점

- python 자료 구조를 자유자제로 다루기 위해서 연습이 더 필요할거같고 dictionary 자료 구조 형태를 좀 더 공부하여야 할거같고, web 에서 자료를 주고받는 형태인 json 자료형태를 추가로 공부해야겠다고 느꼈습니다.

<br />

> problem_a.py

```
import json
from pprint import pprint


def movie_info(movie):
    new_dict = {
        "id": movie.get("id"),
        "title": movie.get("title"),
        "poster_path": movie.get("poster_path"),
        "vote_average": movie.get("vote_average"),
        "overview": movie.get("overview"),
        "genre_ids": movie.get("genre_ids")
    }

    return new_dict
    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
```

비교적 간단하게 풀린코드로 new_dict 로 새로운 딕셔너리를 만들고 그 안에서 json 파일을 읽어와 바로 제가 원하는 dictionary 를 구성 하였습니다.

<br /><br />

> problem_b.py
```
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

```
movie.json 파일에서 genre_ids 값을 가져온뒤, genre_ids 값이 여러개일수 있으므로 for문으로 genre.json 파일 탐색합니다. 이후 같은 id를 가질경우 값을 genre_list에 어펜드하였고 new_dict 를 재구섣하였습니다.

<br /><br />

> problem_c.py
```
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
```
problem_b.py 를 모듈화하여 problem_c.py 에서 import 하여 재사용하였습니다.

<br /><br />

> problem_d.py

```
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
```
1. movies 에서 for 문을 돌며 각 movie 의 movie_id를 추출하여 해당 값을 f-string을 이용해 movies 폴더 안에 있는 각 파일들을 열어줍니다.

2. 이후 각 json 파일 안에 'title' / 'revenue' 값들을 찾아옵니다.

3. max_result 에 가장 높은 revenue 작품의 이름만을 저장하여 리턴합니다.

<br /><br />

> problem_e.py
```
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

```
1. movies 에서 for 문을 돌며 각 movie 의 movie_id를 추출하여 해당 값을 f-string을 이용해 movies 폴더 안에 있는 각 파일들을 열어줍니다.

2. 이후 각 json 파일 안에 'title' / 'realease_date' 값들을 찾아옵니다.

3. realease_date 의 5,6번쨰 인덱스 값이 12이면(12월 작품) movie data의 title 값(영화제목)을 저장하여 리턴합니다.

<br /><br />

> problem_f.py
```
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
```
- 1900s 개봉작 중 많은 수입을 올린 영화 순위
    1. movies 에서 각 movie의 movie_id를 추출 하여 movies 폴더에서 각 파일을 엽니다.
    2. 이후 각 파일 안에 production_companies 값을 찾아옵니다.
    3. release_date 앞에 2글자를 뽑아 "19" 이면 (1900s) 영화이면 영화 제목과 수익을 result에 어펜드 시킵니다.
    4. 수익을 기준으로 내림차순 정렬후 리턴

<br />

- 배급한 영화가 많은 순으로 배급사 정렬하기.
    1. movies 에서 각 movie의 movie_id를 추출 하여 movies 폴더에서 각 파일을 엽니다.
    2. 이후 각 파일 안에 production_companies 값을 찾아옵니다.
    3. production_companies 값이 리스트로 여러개 일 수도 있으므로 for 문으로 탐색합니다.
    4. 제작사 company 값이 이미 result에 저장되어 있으면 다른 리스트에 어펜드시킵니다.
    5. 이후 영화 제작사마다 얼마나 많은 영화를 제작했는지 카운팅합니다.
    6. 제작 수를 내림차순 정렬 후 리턴합니다.
