import re
def solution(n):
    n = n.lower()
    two = re.compile('[=+,#/?:^$@*~&%!(\)[\]<\>{\}]')
    n = re.sub(two,'',n)
    n = re.sub('[.][.]*','.',n)
    
    n = n.strip('.')
    if n=='':
        n = "a"
    if len(n)>=16:
        n = n[:15]
        n = n.strip('.')
    if len(n)<=3:
        n += n[-1] * (3-len(n))
    return n