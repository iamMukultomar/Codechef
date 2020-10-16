# cook your dish here
for i in range(int(input())):
    n,q=map(int,input().split())
    a=list(map(int,input().split()))
    tquery=0
    flag=True
    for i in range(1,n+1):
        tquery+=a[i-1]
        if tquery<i*q:
            print(i)
            flag=False
            break
        
    if flag==True:
        print((tquery//q)+1)
    