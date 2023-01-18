def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    try :  # 에러가 안나니?
        if 0 <= int(user_data["id"][-1]) <= 9 :  # 신규 생성 아이디 마지막 글자가 0부터 9사이 숫자로 끝나니?
            return True
        else :
            return False
    except : # 에러가 나니?
        return False

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False