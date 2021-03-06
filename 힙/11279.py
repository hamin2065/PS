# https://www.acmicpc.net/problem/11279
# 최대 힙

from sys import stdin
import heapq

heap = []

n = int(stdin.readline().strip())
for i in range(n) : 
    num = int(stdin.readline().strip())
    if num == 0 : 
        if len(heap) == 0 : 
            print(0)
        else : 
            print(-heapq.heappop(heap))
    else : 
        heapq.heappush(heap,-num)