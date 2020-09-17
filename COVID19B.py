# cook your dish here
import math
import operator as op
from functools import reduce

def comb(n, r):
    if n<r:
        return 0
    r = min(r, n-r)
    num = reduce(op.mul, range(n, n-r, -1), 1)
    den = reduce(op.mul, range(1, r+1), 1)
    return num // den 
    
    
for _ in range(int(input())):
    n=int(input())
    ans=0
    sm=n*(n+1)//2
    mod=0
    nm1=(math.sqrt(1+2*((n*n)+n))-1)/2
    nm2=int(nm1)
    sm2=(nm2*(nm2+1))/2
    dff=(sm/2)-(sm2)
    if(dff>nm2-1):
        mod=dff-nm2
        
    
    if(dff==0 ):
        also=comb(nm2,2)
        
        also+=comb(n-nm2,2)
        
        
    if(sm%2!=0):
        print(0)
    else:
        if int(nm1)==nm1:
            print(n-int(nm1)+also-int(mod))
            
        else:
            print(n-int(nm1)-int(mod))
            
            
    