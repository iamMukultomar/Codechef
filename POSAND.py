# cook your dish here
for i in range(int(input())):
    n=int(input())
    a=[2,3,1]
    if n==1:
        print(1)
    elif n==2:
        print(-1)
    elif n==3:
        print(*a)
    elif n&(n-1)==0:
        print(-1)
    else:
        print(*a,end=' ')
        i=4
        while(i<=n):
            if(i&(i-1)==0):
                print(i+1,end=' ')
                print(i,end=' ')
                i+=2
            else:
                print(i,end=' ')
                i+=1
        #for i in a:
         #   print(i,Eof=' ')
        print()