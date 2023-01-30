n, m = map(int,input().split())
arr = [i for i in range(1,n+1)]

result = []

def comb(arr, m):

    answer = ""

    if len(result) == m :
        for i in result:
            answer += str(i) + " "
        print(answer)
        return

    start = arr.index(result[-1])+1 if result else 0
    for i in range(start,len(arr)):
        result.append(arr[i])
        comb(arr,m)
        result.pop()

comb(arr, m)