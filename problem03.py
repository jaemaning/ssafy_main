def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    if user_data["id"] and user_data["password"] : ## user_data 딕셔너리에 id값과 password값이 둘다 존재하니?
        return True
    else :
        return False


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True