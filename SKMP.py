n=int(input())
for z in range(n):
    a =list(input())    
    b=list(input())    
    for i in b:
        a.remove(i)
    a=sorted(a)
    
    p1,p2="",""
    c1,c2,d1,d2=list(),list(),list(),list()
    for i in a:
     if i<b[0]:
         c1.append(i)
     else: 
         c2.append(i)
        
    p1=''.join(c1)+''.join(b)+''.join(c2)
    for i in a:
        if i<=b[0]:
            d1.append(i)
        else:
            d2.append(i)
    p2=''.join(d1)+''.join(b)+''.join(d2)
    print(min(p1,p2))
        
     
    