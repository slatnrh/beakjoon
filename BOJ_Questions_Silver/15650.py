import sys
input = sys.stdin.readline

# dfs: M과 배열의 길이가 같을 때 출력하는 구조, 1부터 시작하여 배열의 길이가 맞으면 출력 후 마지막 값만 pop
def dfs(start):
    if len(arr) == M:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(start, N+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()

N, M = map(int, input().split())
arr = list()
dfs(1)