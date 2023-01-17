from collections import deque
from itertools import permutations

t = int(input())

for test_case in range(t):
    n = int(input())
    nlist = deque(map(int,input().split()))


    company = []
    home = []
    xlist = []
    ylist = []
    for i in range(2):
        company.append(nlist.popleft())
    
    for i in range(2):
        home.append(nlist.popleft())

    mlist = []
    for i in range(len(nlist)//2):
        mlist.append([nlist.popleft(),nlist.popleft()])


    perm_list = list(permutations(mlist,len(mlist)))
    
    dists = []
    
    for xy in perm_list:
        pre = company
        dist = 0

        for x,y in xy:
            dist+=abs(pre[0]-x)
            dist+=abs(pre[1]-y)
            pre=[x,y]
        
        dist+=abs(pre[0]-home[0])
        dist+=abs(pre[1]-home[1])
        dists.append(dist)

    print(f"#{test_case+1} {min(dists)}")