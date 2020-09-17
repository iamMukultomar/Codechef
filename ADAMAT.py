for _ in range(int(input())):
    n=int(input())
    dp=[]
    for i in range(n):
        dp.append(list(map(int,input().split())))
    ans=0
    for i in range(n-1,0,-1):
        if dp[i][i-1]+1!=dp[i][i]:
            ans+=1
            l=i+1
            for j in range(l):
                for k in range(j,l):
                    tem=dp[k][j]
                    dp[k][j]=dp[j][k]
                    dp[j][k]=tem
    print(ans)