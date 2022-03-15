import heapq
def solution(jobs):
    n = len(jobs)
    heapq.heapify(jobs)
    current = 0
    total = 0
    waiting = []
    s,c = heapq.heappop(jobs)
    heapq.heappush(waiting,[c,s])
    
    while waiting:
        cost,start = heapq.heappop(waiting)
        if start>=current:
            current = start+cost
            total += cost
        else:
            current += cost
            total +=  current - start
        
        while jobs:
            if jobs[0][0]<=current:
                heapq.heappush(waiting,[jobs[0][1],jobs[0][0]])
                heapq.heappop(jobs)
            else:
                if not waiting:
                    heapq.heappush(waiting,[jobs[0][1],jobs[0][0]])
                    heapq.heappop(jobs)
                break
    return total//n