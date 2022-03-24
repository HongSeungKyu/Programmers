from collections import defaultdict
import heapq
def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    dic = defaultdict(int)
    for u,v,w in road:
        graph[u].append((v,w))
        graph[v].append((u,w))
    for i in range(1,N+1):
        dic[i] = float("INF")
    Q = [(0,1)]
    visited = []
    while Q:
        cur_cost,node = heapq.heappop(Q)
        if node in visited:
            continue
        if cur_cost<=K:
            dic[node] = min(dic[node],cur_cost)
            visited.append(node)
            for v,w in graph[node]:
                heapq.heappush(Q,(cur_cost+w,v))
                
    for key in dic.keys():
        if dic[key]!=float("INF"):
            answer += 1
    
    return answer