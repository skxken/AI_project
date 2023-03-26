import sys
import time
import random

import numpy as np


def getnum(s):
    num = 0
    for i in range(len(s)):
        if '0' <= s[i] <= '9':
            num *= 10
            num += int(s[i])
    return num


if __name__ == "__main__":
    startTime = time.time()
    file = open(sys.argv[1], 'r')
    termination = 60
    if len(sys.argv) > 3:
        termination = int(sys.argv[3])
    random.seed(0)
    file.readline()
    V = getnum(file.readline())
    D = getnum(file.readline())
    Re = getnum(file.readline())
    Ne = getnum(file.readline())
    file.readline()
    C = getnum(file.readline())
    TotC = getnum(file.readline())
    # print(str(V)+" "+str(D)+" "+str(Re)+" "+str(Ne)+" "+str(C)+" "+str(TotC))
    cost = np.zeros((1000, 1000))
    cost += 1000000007
    file.readline()
    lis = list()
    for i in range(Re + Ne):
        s = file.readline()
        p = s.split()
        num = list()
        for j in range(4):
            num.append(0)
            num[j] = int(p[j])
        # print(num)
        cost[num[0]][num[1]] = num[2]
        cost[num[1]][num[0]] = num[2]
        if num[3] != 0:
            lis.append((num[0], num[1], num[3], num[2]))
    # print(lis)
    for i in range(V + 1):
        cost[i][i] = 0
    for k in range(V + 1):
        for i in range(V + 1):
            for j in range(V + 1):
                cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
    res = ""
    mincost = 1000000007
    count=0
    print(time.time()-startTime)
    while time.time() - startTime < termination - 2:
        count+=1
        q = TotC
        remain = Re
        vis = np.zeros(Re + 1)
        ans = list()
        while remain > 0:
            # print(remain)
            ansnow = list()
            capacity = C
            last = D
            while capacity > 0:
                mindis = 1000000007
                posinum = list()
                minnum = -1
                flg = 0
                for i in range(Re):
                    if lis[i][2] > capacity or vis[i] > 0:
                        continue
                    if cost[last][lis[i][0]] < cost[last][lis[i][1]]:
                        if cost[last][lis[i][0]] <= cost[D][lis[i][0]]:
                            if cost[last][lis[i][0]] < mindis:
                                mindis = cost[last][lis[i][0]]
                                posinum.clear()
                                posinum.append(i)
                            elif cost[last][lis[i][0]] == mindis:
                                posinum.append(i)
                    else:
                        if cost[last][lis[i][1]] <= cost[D][lis[i][1]]:
                            if cost[last][lis[i][1]] < mindis:
                                mindis = cost[last][lis[i][1]]
                                posinum.clear()
                                posinum.append(i)
                            elif cost[last][lis[i][1]] == mindis:
                                posinum.append(i)
                if len(posinum) != 0:
                    k=random.randint(1, len(posinum)) - 1
                    #print(k)
                    minnum = posinum[k]
                if cost[last][lis[minnum][1]] < cost[last][lis[minnum][0]]:
                    flg = 1
                r = random.randint(1, 100)
                if r <= 2:
                    cnt = 0
                    for i in range(Re):
                        if lis[i][2] <= capacity and vis[i] == 0 and (
                                cost[last][lis[i][0]] <= cost[D][lis[i][0]] or cost[last][lis[i][1]] <=
                                cost[D][lis[i][1]]):
                            cnt += 1
                    if cnt != 0:
                        r = random.randint(1, cnt)
                        for i in range(Re):
                            if lis[i][2] <= capacity and vis[i] == 0 and (
                                    cost[last][lis[i][0]] <= cost[D][lis[i][0]] or cost[last][
                                lis[i][1]] <= cost[D][
                                        lis[i][1]]):
                                r -= 1
                                if r == 0:
                                    minnum = i
                                    if cost[last][lis[i][0]] < cost[last][lis[i][1]] and cost[last][lis[i][0]] <= \
                                            cost[D][lis[i][0]] + cost[last][D]:
                                        flg = 0
                                    elif cost[last][lis[i][1]] <= cost[D][lis[i][1]]:
                                        flg = 1
                                    else:
                                        flg = 0
                if minnum == -1:
                    break
                if flg == 0:
                    q += cost[last][lis[minnum][0]]
                    ansnow.append((lis[minnum][0], lis[minnum][1]))
                    last = lis[minnum][1]
                else:
                    q += cost[last][lis[minnum][1]]
                    ansnow.append((lis[minnum][1], lis[minnum][0]))
                    last = lis[minnum][0]
                vis[minnum] = 1
                capacity -= lis[minnum][2]
                remain -= 1
            ans.append(ansnow)
            q += cost[last][D]
        s = "s "
        for i in range(len(ans)):
            s += "0,"
            for j in range(len(ans[i])):
                s += "(" + str(ans[i][j][0]) + "," + str(ans[i][j][1]) + "),"
            s += "0"
            if i != len(ans) - 1:
                s += ","
        if q < mincost:
            mincost = q
            res = s
    print(res)
    print("q " + str(int(mincost)))
    print(count)
