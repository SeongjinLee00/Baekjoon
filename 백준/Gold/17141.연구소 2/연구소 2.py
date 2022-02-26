## 실험용으로 친구 코드를 제출합니다

from itertools import combinations
from collections import deque

# 입력 받기
N, M = map(int, input().split())
array_original = [list(map(int, input().split())) for _ in range(N)]

# 벽만 남긴 2차원 리스트 초기화
array_only_wall = [[0]*N for _ in range(N)]

# bfs 탐색을 위한 리스트
dr, dc = [1,-1,0,0], [0,0,1,-1]

# 바이러스 위치를 담을 리스트
virus_pos = []

# 벽을 제외한 영역의 크기
area = 0

# 연구소 전체 영역을 순회
for r in range(N):
    for c in range(N):
        # 바이러스 위치 담기
        if array_original[r][c] == 2:
            virus_pos.append((r, c))
        # 벽이 아닌 칸이라면, 영역의 크기 1 증가 밑 array_only_wall -1로 초기화
        if array_original[r][c] != 1:
            area += 1
            array_only_wall[r][c] = -1
        # 벽이라면, array_only_wall '-'로 초기화
        if array_original[r][c] == 1:
            array_only_wall[r][c] = '-'

# 바이러스를 놓을 수 있는 모든 경우 생성
test_cases = combinations(virus_pos, M)

# bfs 함수 구현
def bfs(case):
    # 덱 생성
    q = deque([])

    # 초기 바이러스 위치(r,c)와 시간(t)을 덱에 담기
    # 초기 바이러스이므로 시간은 0 
    for item in case:
        q.append((item[0],item[1],0))
        visited[item[0]][item[1]] = True
    
    # 연구소를 바이러스로 꽉 채우는 데에 걸리는 시간
    t_max = 0
    # 연구소를 채운 바이러스의 개수
    virus_cnt = M

    # 덱이 유지될 때 까지 반복
    while q:
        # 현재 위치 밑 시간
        r, c, t = q.popleft()
        # 상하좌우 네 방향 탐색
        for i in range(4):
            # 탐색할 칸
            rr, cc = r+dr[i], c+dc[i]
            # 만약 탐색할 칸이 연구소의 범위를 넘어가지 않는다면
            if 0<=rr<N and 0<=cc<N:
                # 만약 탐색할 칸을 방문한 적이 없고, 그 칸이 벽이 아니라면
                if not visited[rr][cc] and array[rr][cc] != '-':
                    # 해당 칸을 그 칸에 도달하는데 걸리는 시간으로 초기화
                    array[rr][cc] = t + 1
                    # 해당 칸을 덱에 추가
                    q.append((rr,cc,t+1))
                    # visited 값 True로 변경
                    visited[rr][cc] = True
                    # 시간 갱신
                    t_max = max(t_max, t+1)
                    # 바이러수 개수 추가
                    virus_cnt += 1
    # 최종적으로 걸리는 시간과 바이러스의 개수 리턴
    return t_max, virus_cnt

# 정답을 저장할 변수
t_min = 10**9

# 바이러스를 놓을 수 있는 모든 경우를 순회
for case in test_cases:
    # 각 케이스별로 연구소 배열 초기와
    # *중요* 반드시 deepcopy 사용
    array = [item[:] for item in array_only_wall]
    # bfs를 위해 방문한 칸인지 판단하기 위한 visited 리스트 초기화
    visited = [[False]*N for _ in range(N)]
    # bfs 수행
    t, virus_cnt = bfs(case)

    # 만약 virus_cnt가 area와 같지 않다면, 바이러스가 퍼지지 않은 곳이 존재하므로
    # 원하는 케이스가 아니기 때문에 무시
    if virus_cnt != area:
        continue
    # 정답 갱신
    t_min = min(t_min, t)

# t_min이 한 번이라도 갱신 되었다면, t_min 출력, 그렇지 않다면 
# 바이러스를 가득 채울 수 있는 경우가 없으므로 -1 출력
if t_min == 10**9:
    print(-1)
else:
    print(t_min)