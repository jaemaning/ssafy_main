import sys
input = sys.stdin.readline

def cal(N):
    total = 0
    avg = 0
    avg_2 = 0
    man = 0
    cnt = 0
    percent = []

    for i in range(N):

        T = input().split()
        if int(T[0]) >= 1 and int(T[0]) <= 1000:  
            man = T[0]
            for i in range(1, len(T)):
                if not(int(T[i]) >= 0 and int(T[i]) <= 100):
                    return False
                else:
                    total += int(T[i])
            
            avg = total / int(man) 

            for i in range(1, len(T)):
                if avg < int(T[i]):
                    cnt += 1

            avg_2 = cnt / int(man) * 100
            percent.append(round(float(avg_2), 3))

        total = 0
        avg = 0
        man = 0
        cnt = 0
        avg_2 = 0

    for i in range(N):
        print(str("%.3f" %percent[i]) + "%")
        # print(f'{percent[i]}%')

cal(N = int(input()))
