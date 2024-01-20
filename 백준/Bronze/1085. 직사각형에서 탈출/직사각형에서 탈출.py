# 입력 받기
x, y, w, h = map(int, input().split())

# 네 방향 중 최소 거리 계산
min_distance = min(x, y, w - x, h - y)

# 결과 출력
print(min_distance)
