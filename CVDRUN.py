# cook your dish here
for i in range(int(input())):
    a=list(map(int,input().split()))
    n=a[0]
    k=a[1]
    x=a[2]
    y=a[3]
    
    visitedcity=[x]
    
    while(True):
        nextcity=(x+k)%n
        if nextcity==y:
            print('YES')
            break
        if nextcity in visitedcity:
            print('NO')
            break
        else:
            visitedcity.append(nextcity)
            x=nextcity
            