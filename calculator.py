cnt = 0

while True:
    print("\n *** 계산기 종료 방법 n1 : 0 , n2 : 0 또는 n2 : 종료를 입력하세요 *** \n")
    try:
        if cnt == 0:
            n1 = int(input("n1:").strip())
            n2 = int(input("n2:").strip())
            cnt += 1

            if n1 == 0 and n2 == 0:
                break
            else:
                n3 = input("연산자:")

                if n3 == "+":
                    a = n1+n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                elif n3 == "-":
                    a = n1-n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                elif n3 == "/":
                    a = n1/n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                elif n3 == "*" or n3 == "x" or n3 == "X":
                    a = n1*n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                elif n3 == "**":
                    a = n1**n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                else :
                    print("\n Error: *** 정확한 사칙연산 기호를 입력하세요 *** \n")
        else:
            try:
                n2 = int(input("n2:").strip())
                n3 = input("연산자:")

                if n3 == "+":
                    a = a+n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                elif n3 == "-":
                    a = a-n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                elif n3 == "/":
                    a = a/n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                elif n3 == "*" or n3 == "x" or n3 == "X":
                    a = a*n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                elif n3 == "**":
                    a = a**n2
                    print(" ")
                    print(a)
                    print(" ")
                    

                else :
                    print("\n Error: *** 정확한 사칙연산 기호를 입력하세요 *** \n")
            except:
                break
            
    except:
        print(" ")
        print("\n Error:  *** 숫자만 입력하세요 *** \n")
        print(" ")
