from math import gcd
import sys

input = sys.stdin.readline

n = int(input())
number_list = []

for i in range(n):
    m = int(input())
    number_list.append(m)

number_list.sort()

diff_list = []
gcd_list = []
result = []

if n == 2 :
    target_number = number_list[1] - number_list[0]

    for i in range(1,int(target_number**0.5)+1):
        if target_number % i == 0:
            result.append(i)
            result.append(target_number//i)
    
else:
    for i in range(1,n):
        diff_list.append(number_list[i] - number_list[i-1])

    for i in range(1,n-1):
        gcd_list.append(gcd(diff_list[i-1],diff_list[i]))


    min_val = min(gcd_list)

    for i in range(1,int(min_val**0.5)+1):
        if min_val % i == 0 :
            result.append(i)
            result.append(min_val//i)

result = list(set(result))
result.sort()

for num in result[1:]:
    print(num,end=' ')


