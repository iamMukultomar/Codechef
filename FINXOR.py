tc=int(input())
a=[]
t=1
a.append(t)
for i in range(1,21):
    a.append(2*t)
    t*=2
for _ in range(tc):
    n=int(input())
    print(1," ",a[20])
    sumi=int(input())
    sumi=sumi-(a[20]*n)
    xo=0
    if sumi%2!=0:
        xo+=1
    for i in range(1,20):
        fsum=sumi+(a[i]*n)
        print(1," ",a[i])
        gsum=int(input())
        if((fsum-gsum)/(a[i]*2))%2!=0:
            xo=xo+a[i]
            
    print(2," ",xo,"\n")
    output=int(input())
    