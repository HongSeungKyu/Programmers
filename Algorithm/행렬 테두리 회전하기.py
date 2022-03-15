from collections import deque
def solution(r, c, q):
    
    m = [[c*i+j for j in range(1,c+1)] for i in range(r)]
    
    arr_min = []
    for a,b,c,d in q:
        i = a-1
        j = b-1
        end = (c,d)
        queue = deque()
        while True:
            if len(queue)==0:
                queue.append(m[i][j])
                min = m[i][j]
            else:
                queue.append(m[i][j])
                if m[i][j]<min:
                    min = m[i][j]
                m[i][j] = queue.popleft()
            if i==a-1 and j<d-1:
                j+=1
            elif i<c-1 and j==d-1:
                i+=1
            elif i==c-1 and j>b-1:
                j-=1
            elif i>a-1 and j==b-1:
                i-=1
            if (i==a-1) and (j==b-1):
                break

        m[i][j] = queue.popleft()
        arr_min.append(min)
    return arr_min