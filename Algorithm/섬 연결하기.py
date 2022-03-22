def solution(n, costs):
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        x = find(x)
        y = find(y)
        if x<y:
            parent[y] = x
        else:
            parent[x] = y
    answer = 0
    costs = sorted(costs,key=lambda x:x[2])
    parent = {}
    for i in range(n):
        parent[i] = i 
    
    for a,b,c in costs:
        if find(a)!=find(b):
            union(a,b)
            answer += c
    return answer