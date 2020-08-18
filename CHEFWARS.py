n=int(input())
for i in range(n):
    k,a=list(map(int,input().strip().split()))
    while(True):
        k=k-a
        a=a//2
        if a==0 and k>0:
           print(0)
           break
        elif k<=0:
           print(1)
           break