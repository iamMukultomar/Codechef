def ncr(n, r, p): 
    # initialize numerator 
    # and denominator 
    num = den = 1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den,  
            p - 2, p)) % p 
            
            
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    maxv=a.count(max(a))
    #print(maxv)
    G=ncr(maxv,maxv//2,1000000007)
    if maxv%2!=0:
        print((2**n)%1000000007)
    
    
    #print(G)
    else:
        print(((2**n)-(2**(n-maxv))*G)%1000000007)