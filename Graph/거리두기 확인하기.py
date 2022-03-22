def solution(places):
    answer = []
    for room in places:
        answer.append(checkAdj(room))        
    return answer


def checkAdj(room):
    dir1 = [(1,0), (0,1)] 
    dir2 = [(2,0), (0,2), (1,1), (-1,1)] # dc, dr => 우우, 하하, 우하, 좌하
    pplIn2 = [ [(1,0)], [(0,1)], [(1,0),(0,1)], [(-1,0),(0,1)] ]

    for r in range(5):
        for c in range(5):
            if room[r][c]=="P":
                # 거리 1인 곳에 사람 있는지 확인
                for dc, dr in dir1:        
                    nc, nr = c+dc, r+dr
                    if nc>=5 or nr>=5:
                        continue
                    # 사람 있으면 실패
                    if room[nr][nc] == "P":
                        return 0
                # 거리 2인 곳에 사람 있는지 확인
                for d in range(4):
                    dc, dr = dir2[d]
                    nc, nr = c+dc, r+dr
                    if nc>=5 or nr>=5 or nc<0 or nr<0:
                        continue
                    if room[nr][nc] == "P":
                        for xc, xr in pplIn2[d]:
                            if room[r+xr][c+xc]!='X':
                                return 0
    return 1