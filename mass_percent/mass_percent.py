# 실습 6-2

def mass_percent():
    sw_per_all = 0
    sw_amount_all = 0
    tmp = 0
    result_check = 1

    for _ in range(5):
        try:
            sw_per, *sw_amount = input(f"{_+1}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ").split()
            if sw_per.lower() == "done" :
                break

            sw_per = int(sw_per[:-1])
            sw_amount = int(sw_amount[0][:-1])
            tmp += sw_per*sw_amount
            sw_amount_all += sw_amount
            sw_per_all = tmp / sw_amount_all
        except:
            print("잘못 입력하셨습니다.")
            result_check = 0
            break
    else:
        Done = input("Done 을 입력하세요.")

    if result_check :
        print(f"{round(sw_per_all,2)}% {sw_amount_all}g")

# 15 200 10 300 12 500