def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    for problem in problems :
        max_alp = max(problem[0], max_alp)
        max_cop = max(problem[1], max_cop)
    
    # 시작 알고력이 max알고력보다 크거나, 시작 코딩력이 max코딩력보다 클때 런타임 레어
    alp = min(max_alp, alp)
    cop = min(max_cop, cop)
    
    dp = [[int(1e9)] * (max_cop+1) for _ in range(max_alp+1)]
    dp[alp][cop] = 0
    
    for i in range(alp, max_alp+1) :
        for j in range(cop, max_cop+1) :
            # 1시간
            if i<max_alp :
                dp[i+1][j] = min(dp[i+1][j], dp[i][j]+1)
            if j<max_cop :
                dp[i][j+1] = min(dp[i][j+1], dp[i][j]+1)
            
            # 문제해결
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
                if i>=alp_req and j>=cop_req :
                    next_apl = min(max_alp, i+alp_rwd)
                    next_cop = min(max_cop, j+cop_rwd)
                    
                    dp[next_apl][next_cop] = min(dp[next_apl][next_cop], dp[i][j]+cost)
                    
    return dp[max_alp][max_cop]