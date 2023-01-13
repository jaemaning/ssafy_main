# path : 경로
# selected : 지금까지 들른 고객의 집 번호 체크
# i번 고객의 집을 들른 경우 selected[i] 가 True임.
def dfs(path, selected):
    global answer
    # 고객 수 N 만큼 다 골랐다면
    if len(path) == N:
        # 회사에서 시작
        x = comp[0]
        y = comp[1]

        # 비용
        length = 0

        for nx, ny in path:
            # 고객 집 다 들렀다가
            length += abs(x-nx) + abs(y-ny)
            # 현재 위치 최신화
            x = nx
            y = ny

        # 집도 가야지
        length += abs(x-home[0]) + abs(y-home[1])
        # 최소값
        answer = min(length, answer)
        # 돌아가기
        return

    for i in range(N):
        # i번 고객의 집을 들른적이 없다면
        if not selected[i]:
            # 들른 상태로 다음 고객의 집 고르러 ㄱㄱ
            selected[i] = True
            path.append(customers[i])
            dfs(path,selected)

            # 들른 상태로 계산을 끝냈으니 다음 계산을 위해 들르지 않았다고 되돌리기
            path.pop()
            selected[i] = False   

T = int(input())

customers = []
N = 0
answer = 9999999999
for tc in range(1,T+1):
    # 최소값이 목표이므로 적당히 큰 값으로 초기화
    answer = 9999999999
    # 고객 수
    N = int(input())
    # 좌표 정보
    locations = list(map(int, input().split()))
    # 회사
    comp = [locations[0] , locations[1]]
    # 집
    home = [locations[2] , locations[3]]
    # 고객
    customers = [[locations[i], locations[i+1]] for i in range(4,2*N+4,2)]

    dfs([],[False] * N)
    print(f"#{tc} {answer}")