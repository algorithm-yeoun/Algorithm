def solution(n, wires):
    answer = n-1
    
    def dfs(node, visited, tree):
        visited[node] = True
        count = 1
        for next_node in tree.get(node, []):
            if not visited[next_node]:
                count += dfs(next_node, visited, tree)
        return count
    
    for i in range(len(wires)):
        # 한 전선 제거
        temp_wires = wires[:i] + wires[i+1:]
        
        # 트리 생성
        tree={}
        for p, c in temp_wires:
            tree.setdefault(p, []).append(c)
            tree.setdefault(c, []).append(p)
        
        visited = [False] * (n+1)
        cnt = dfs(1, visited, tree)
        answer = min(answer, abs(2*cnt - n))
    
    return answer