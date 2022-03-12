parents = dict()
rank = dict()
def find(node):
    if parents[node] != node:
        parents[node] = find(parents[node])
    return parents[node]

def union(s,e):
    start = find(s)
    end = find(e)
    if rank[start]>rank[end]:
        parents[end] = start
    else:
        parents[start] = end
        if rank[start]==rank[end]:
            rank[end]+=1

def solution(n, computers):
    answer = 0
    for i in range(n):
        parents[i] = i
        rank[i] = 0

    for i in range(n):
        for k in range(n):
            if i==k:
                continue
            if computers[i][k] == 1 and parents[i]!=parents[k]:
                union(i,k)

    answer = {find(v): k for k, v in parents.items()}
    return len(answer)