
try:
    num = int(input("숫자를 입력해주세요"))
    print(num)
    print(10/num)
except Exception:  ## 상위 예외 (valueerror, zerodivision error 다 포함)
    print("에러발생")    
except ValueError:
    print("숫자만 입력하세요")
except ZeroDivisionError:
    print("0으로 나눌수는 없습니다.")
