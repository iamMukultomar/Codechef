# cook your dish here
n=int(input())
for i in range(n):
    a,b=list(map(int,input().strip().split()))
    if(a//9==b//9 or b//9<a//9):
        if(b%9==0):
            print("1",b//9)
        else:
            print("1",b//9+1)
    else:
        if(a%9==0):
            print("0",a//9)
        else:
            print("0",a//9+1)
        