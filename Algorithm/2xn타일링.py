def solution(n):
    total = [1,2]
    for i in range(2,n):
        total.append((total[i-2]+total[i-1])%1000000007)
    return total[-1]%1000000007