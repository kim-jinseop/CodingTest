# 입력 처리
T = int(input())
for _ in range(T):
    N = int(input())

    # 0과 1 출력 횟수 배열 초기화
    zero_count = [1, 0] + [0] * (N - 1)
    one_count = [0, 1] + [0] * (N - 1)

    # 피보나치 수열 계산
    for i in range(2, N + 1):
        zero_count[i] = zero_count[i - 1] + zero_count[i - 2]
        one_count[i] = one_count[i - 1] + one_count[i - 2]

    print(zero_count[N], one_count[N])
