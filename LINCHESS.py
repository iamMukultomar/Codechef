# cook your dish here
t=int(input())
for i in range(t):
    n,k=list(map(int,input().strip().split()))
    a=list(map(int,input().strip().split()))
    maxi=-1
    a.sort()
    for i in a:
        if k%i==0:
            maxi=i
    print(maxi)