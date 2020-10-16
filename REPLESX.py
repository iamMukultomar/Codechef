
def index(a,n,x,p):
    mini = 100000000
    minp=0
    for i in range(n):
        if(a[i] == x):
            if(abs(p-i) < mini):
                mini = abs(p-i);
                minp = i;
    return minp;
    
    
def mai():
    n,x,p,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    ind=index(a,n,x,p)
    count=0
    if a[ind]!=x:
        a[k-1]=x
        a.sort()
        count+=1
    if(a[p-1] == x):
        print(0+count)
        return
    if(p <k and a[p-1] <x):
        print(-1)
        return
    if(p >k and a[p-1] >x):
        print(-1)
        return
    ind = index(a,n,x,p)+1
    print(abs(p-ind)+count)
    
    
for i in range(int(input())):
    mai()
    #print()
    
    

