def solution(w,h):
    if w==h:
        return w*h-w
    else:
        a,b,c = w,h,0
        while b != 0:
            c = a%b
            a = b
            b = c
        gcd = a
        return w*h - (w+h-gcd)