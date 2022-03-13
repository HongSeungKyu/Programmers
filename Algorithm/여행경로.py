from collections import deque

def solution(tickets):
    answer = []
    graph = dict() # 인접 리스트
    length = 0     # 티켓 개수

    for ticket in tickets:
        length += 1
        src, dst = ticket

        if graph.get(src) == None:
            graph[src] = []
        if dst not in graph[src]:
            graph[src].append(dst)

    q = deque()
    new_tickets = list(tickets) # 아직 사용하지 않은 항공권 리스트
    # (경로, 사용한 티켓 수, 중복 확인용 리스트)
    q.append((["ICN"], 0, new_tickets))
    while q:
        route, cnt, temp_tickets = q.popleft()
        src = route[-1]
        if cnt == length: # 항공권 모두 사용
            answer.append(route)

        if graph.get(src) == None:  # 경로를 잘못 짜서 다음 항공으로 가는 티켓이 없으면 경로 폐기
            continue

        # 현재 src에서 사용할 수 있는 항공권 확인
        for dst in graph[src]:
            if [src, dst] not in temp_tickets: # 이미 사용한 항공권이면 패스
                continue

            temp_tickets.remove([src, dst]) # 사용 -> 보유한 항공권 리스트에서 제거
            q.append((route + [dst], cnt+1, list(temp_tickets)))
            temp_tickets.append([src, dst]) # 다음 반복문에서 사용해야 하므로 다시 추가

    answer.sort()
    return answer[0]