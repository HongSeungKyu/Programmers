def solution(s):
    answer = 10000
    if len(s)<=1:
        return 1
    for i in range(1,len(s)//2+1):
        word = ''
        k = 0
        count = 1
        while k<len(s):
            if s[k:k+i]==s[k+i:k+i+i]:
                count += 1
            elif count<=1:
                word += s[k:k+i]
            else:
                word += str(count)+s[k:k+i]
                count = 1
            k += i
        answer = min(answer,len(word))
    
    return answer