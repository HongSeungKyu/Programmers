def solution(n):
    answer = []
    def hanoi(n,start,end):
        if n==0:
            return
        else:
            middle = 6-start-end
        hanoi(n-1,start,middle)
        answer.append([start,end])
        hanoi(n-1,middle,end)
    hanoi(n,1,3)
    return answer