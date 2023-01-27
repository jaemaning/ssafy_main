import sys
input = sys.stdin.readline

N = int(input())
count = 0

for i in range(N):
    A = list(map(int,input().split()))
    score_mean = (sum(A)-A[0])/(len(A)-1)
    for x in range(1,len(A)):
        if A[x] > score_mean:
            count = count + 1
    B = (count/A[0])*100
    print(str("%.3f" %B) + "%")
    count = 0