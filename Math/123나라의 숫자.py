def solution(n):
    answer = ''
    while n>0:
        n,mod = divmod(n,3)
        if mod==0:
            mod = 4
            n -= 1
        answer += str(mod)
    return answer[::-1]