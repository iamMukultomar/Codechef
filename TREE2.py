# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    d=[-1]
    for i in range(len(a)):
        if a[i]!=d[-1] and a[i]!=0:
            d.append(a[i])
    print(len(d)-1)
