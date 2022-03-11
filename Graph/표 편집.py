class Node:
    def __init__(self):
        self.removed = False
        self.prev = None
        self.next = None
def solution(n, k, cmd):
    nodeArr = [Node() for _ in range(n)]
    for i in range(1,n):
        nodeArr[i-1].next = nodeArr[i]
        nodeArr[i].prev = nodeArr[i-1]
    
    curr = nodeArr[k]
    stack = []

    for str in cmd:
        if str[0] == "U":
            x = int(str[2:])
            for _ in range(x):
                curr = curr.prev
        elif str[0] == "D":
            x = int(str[2:])
            for _ in range(x):
                curr = curr.next
        elif str[0] == "C":
            stack.append(curr)
            curr.removed = True
            up = curr.prev
            down = curr.next
            if up:
                up.next = down
            if down:
                down.prev = up
                curr = down
            else:
                curr = up
        else:
            node = stack.pop()
            node.removed = False
            up = node.prev
            down = node.next
            if up:
                up.next = node
            if down:
                down.prev = node
    answer = ''
    for i in range(n):
        if nodeArr[i].removed:
            answer += "X"
        else:
            answer += "O"
    return answer
#print(solution(8,5,["D 2","C","U 3","C","D 2","C","U 2","Z","Z"]))
print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
temp = [1,2,3]
temp.insert(1,4)


