import sys
input = sys.stdin.readline


tc = int(input().strip())

for _ in range(tc):

    n = int(input().strip())
    tp_dict = {}

    for _ in range(n):

        name, tp = input().strip().split()
        if not tp_dict.get(tp) :
            tp_dict[tp] = 1
        else:
            tp_dict[tp] += 1

    result = 1
    for length in tp_dict.values():
        result *= length+1

    print(result-1)
    
    # print(tplist)

# check_list = [False for _ in range(len(nlist))] 

# def comb(arr,n):
#     global result
#     result = []

#     def generate(choice):

#         if len(choice) == n :
#             result.append(choice[:])
#             return result

#         start = arr.index(choice[-1]) + 1 if choice else 0
#         for i in range(start,len(arr)):
#             choice.append(arr[i])
#             generate(choice)
#             choice.pop()

#     generate([])

#     return result

# print(comb([1,1,3,4,5],3))



# def combination(arr, r):
#     # 1.
#     arr = sorted(arr)

#     # 2.
#     def generate(chosen):
#         if len(chosen) == r:
#             print(chosen)
#             return

#     	# 3.
#         start = arr.index(chosen[-1]) + 1 if chosen else 0
#         for nxt in range(start, len(arr)):
#             chosen.append(arr[nxt])
#             generate(chosen)
#             chosen.pop()
#     generate([])


# combination('ABCDE', 2)
# combination([1, 2, 3, 4, 5], 3)



