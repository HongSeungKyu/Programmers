from collections import defaultdict
def solution(n, edge):
    answer = [0 for _ in range(n)]
    graph = defaultdict(list)
    visited = [False for _ in range(n)]
    queue = [1]
    answer[0] = 1
    visited[0] = True
    for a,b in edge:
        graph[a].append(b)
        graph[b].append(a)
    while queue:
        
        node = queue.pop(0)
        for n in graph[node]:
            if visited[n-1]:
                continue
            queue.append(n)
            visited[n-1] = True
            answer[n-1] = answer[node-1]+1
        
    
    return answer.count(max(answer))