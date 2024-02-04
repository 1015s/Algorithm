info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

# Backtracking
def solution(info, edges):
    visited = [0] * len(info)
    answer = []

    def backtracking(wolf, sheep):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return
    
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    backtracking(wolf, sheep+1)
                else:
                    backtracking(wolf+1, sheep)
                visited[c] = 0

    visited[0] = 1
    backtracking(0,1)

    return max(answer)

print(solution(info, edges))

        
