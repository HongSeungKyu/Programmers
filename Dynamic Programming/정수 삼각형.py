def solution(triangle):
    t_h = len(triangle)
    t_w = [ [0 for _ in range(layer+1)] for layer in range(t_h) ]

    t_w[0][0] = triangle[0][0]
    for layer in range(1, t_h):        
        for room in range(layer+1):
            if room == 0:
                    t_w[layer][room] = triangle[layer][room] + t_w[layer-1][room]
            elif room == layer:
                    t_w[layer][room] = triangle[layer][room] + t_w[layer-1][room-1]
            else: 
                    t_w[layer][room] = triangle[layer][room] + max(t_w[layer-1][room-1], t_w[layer-1][room])
    print(t_w)
    return max(t_w[t_h-1])