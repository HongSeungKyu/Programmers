import datetime

d = datetime.timedelta(15,33.020,minutes=10,hours=3)
#print(d-datetime.timedelta(15,0.01,minutes=10,hours=3))

def solution(lines):
    answer = []
    if len(lines)==1:
        return 1
    else:
        starts = []
        ends = []
        for l in lines:
            string = l.split(' ')
            day = int(string[0].split('-')[2])
            h,m,s = map(float,string[1].split(':'))
            d = datetime.timedelta(seconds=s,minutes=m,hours=h,days=day)
            
            starts.append(d-datetime.timedelta(seconds=float(string[2][:-1])-0.001))
            ends.append(d)
    
    for i in sorted(starts+ends):
        cnt = 0
        time = i+datetime.timedelta(seconds=0.999)
        for j in range(len(starts)):
            
            if starts[j]>time or i>ends[j]:
                continue
            cnt += 1
        answer.append(cnt)
    return max(answer)
lines = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]
print(solution(lines))