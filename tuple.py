from random import randint
def addition2test(a,b,p,q):
	k1=p-a
	k2=q-b
	if(k1==k2):
		return True
	return False

def addition3test(a,b,c,p,q,r):
	k1=p-a
	k2=q-b
	k3=r-c
	if(k1==k2 and k2==k3 and k1==k3):
		return True
	return False


def multi3test(a,b,c,p,q,r):
	if(a==0 or b==0 or c==0):
		return False
	v1=p//a
	v2=q//b
	v3=r//c
	if(v1==v2 and v2==v3 and v1==v3):
		if(a*v1==p and b*v2==q and c*v3==r):
			return True
		else:
			return False
	return False



def mult2test(a,b,p,q):
	if(a==0 or b==0):
		return False
	v1=p//a
	v2=q//b

	if(v1==v2):
		if(a*v1==p and b*v2==q):
			return True
		else:
			return False
	return False

def addy2multall(a,b,c,p,q,r):
	if(p==q):
		return False
	else:
		d=(a*q-p*b)/(p-q)
		if(a+d==0 and b+d!=0):
			k=q//(b+d)
		elif(a+d!=0):
			k=p//(a+d)
		else:
			return False
		if(p==k*(a+d) and q==k*(b+d) and r==k*c):
			return True
	return False
def add2mul2(a,b,c,p,q,r):
	if(r==0):
		return False
	else:
		d=(p*c-a*r)//r
		if(a+d==0):
			return False
		else:
			k=p//(a+d)
			if(k*(a+d)==p and (b+d)==q and k*c==r):
				return True
	return False

def add3mul2(a,b,c,p,q,r):

	if(p!=q):
		d=(a*q-p*b)//(p-q)
		if(a+d==0 and (b+d)!=0):
			k=q//(b+d)
		elif(a+d!=0):
			k=p//(a+d)
		else:
			return False
		if(k*(a+d)==p and k*(b+d)==q and (c+d)==r):
			return True
	return False

def add3mul3(a,b,c,p,q,r):
	if(p!=q):
		d=(a*q-p*b)//(p-q)
		if(a+d==0 and (b+d)!=0):
			k=q//(b+d)
		elif(a+d!=0):
			k=p//(a+d)
		else:
			return False
		if(k*(a+d)==p and k*(b+d)==q and k*(c+d)==r):
			return True
	return False

def mul2addall(a,b,c,p,q,r):
	d=r-c
	if(a!=0 or b!=0):
		if(a!=0):
			k=(p-d)//a
		else:
			k=(p-d)//b
		if(p==k*a+d and q==k*b+d and r==c+d):
			return True

		
	else:
		return False
	return False

def mul2add2(a,b,c,p,q,r):
	d=r-c
	if(a!=0):
		k=(p-d)//a
		if(p==k*a+d and q==k*b and r==c+d):
			return True


	return False
def mul3add2(a,b,c,p,q,r):
	if(a!=b):

		k=(p-q)//(a-b)
		d=p-k*a
		#print(d,k)
		if(p==k*a+d and q==k*b+d and r==k*c):
			return True

	return False



def mul3add3(a,b,c,p,q,r):
	if(a!=b):

		k=(p-q)//(a-b)
		d=p-k*a
		if(p==k*a+d and q==k*b+d and r==k*c+d):
			return True

	return False

def add2add2(a,b,c,p,q,r):
	d2=r-c
	d1=p-a-d2
	if(a+d1+d2==p and q==b+d1 and r==c+d2):
		return True
	else:
		return False

def mul2mul2(a,b,c,p,q,r):
	if(c==0 or b==0):
		return False
	else:
		k1=r//c
		k2=q//b
		if(k1*k2*a==p and k2*b==q and k1*c==r):
			return True
	return False
#outF = open("output.txt", "w")
for _ in range(int(input())):

	a,b,c=list(map(int,input().split()))
	p,q,r=list(map(int,input().split()))
		
	# if(_==614):
	# 	print(a,b,c)
	# 	print(p,q,r)
	# 	break
	# a,b,c=-3 ,-3, -2
		

	# p,q,r=2 ,0, 2
	if(a==p and b==q and c==r):
		print(0)
		
	elif((a==p and b==q) or (b==q and c==r) or (a==p and c==r)):
		print(1)
		
	elif((mult2test(a,b,p,q) and c==r) or (mult2test(a,c,p,r) and b==q) or (mult2test(b,c,q,r) and a==p)):
		print(1)
		
	elif(multi3test(a,b,c,p,q,r)):
		print(1)
		
	elif((addition2test(a,b,p,q) and c==r) or (addition2test(a,c,p,r) and b==q) or (addition2test(b,c,q,r) and a==p)):
		print(1)
		
	elif(addition3test(a,b,c,p,q,r)):
		print(1)
		
	elif(a==p or b==q or c==r):
		print(2)
		
	elif(addition2test(a,b,p,q) or addition2test(b,c,q,r) or addition2test(a,c,p,r)):
		print(2)
		
	elif(mult2test(a,b,p,q) or mult2test(b,c,q,r) or mult2test(a,c,p,r)):
		print(2)
		
	elif(addy2multall(a,b,c,p,q,r) or addy2multall(b,c,a,q,r,p) or addy2multall(c,a,b,r,p,q)):
		print(2)
		
	elif(add2mul2(a,b,c,p,q,r) or add2mul2(b,a,c,q,p,r) or add2mul2(c,b,a,r,q,p) or add2mul2(b,c,a,q,r,p) or add2mul2(a,c,b,p,r,q) or add2mul2(c,a,b,r,p,q)):
		print(2)
		
	elif(add3mul3(a,b,c,p,q,r) or add3mul3(b,c,a,q,r,p) or add3mul3(c,a,b,r,p,q)):
		print(2)
		
	elif(add3mul2(a,b,c,p,q,r) or add3mul2(b,c,a,q,r,p) or add3mul2(c,a,b,r,p,q)):
		print(2)
		
	elif(add2add2(a,b,c,p,q,r) or add2add2(b,a,c,q,p,r) or add2add2(c,b,a,r,q,p) or add2add2(b,c,a,q,r,p) or add2add2(a,c,b,p,r,q) or add2add2(c,a,b,r,p,q)):
		print(2)
		
	elif(mul2addall(a,b,c,p,q,r) or mul2addall(b,c,a,q,r,p) or mul2addall(c,a,b,r,p,q)):
		print(2)
		
	elif(mul2add2(a,b,c,p,q,r) or mul2add2(b,a,c,q,p,r) or mul2add2(c,b,a,r,q,p) or mul2add2(b,c,a,q,r,p) or mul2add2(a,c,b,p,r,q) or mul2add2(c,a,b,r,p,q)):
		print(2)
		
	elif(mul3add3(a,b,c,p,q,r) or mul3add3(b,c,a,q,r,p) or mul3add3(c,a,b,r,p,q)):
		print(2)
		
		
	elif(mul3add2(a,b,c,p,q,r) or mul3add2(b,c,a,q,r,p) or mul3add2(c,a,b,r,p,q)):

		print(2)
		
	elif(mul2mul2(a,b,c,p,q,r) or mul2mul2(b,a,c,q,p,r) or mul2mul2(c,b,a,r,q,p) or mul2mul2(b,c,a,q,r,p) or mul2mul2(a,c,b,p,r,q) or mul2mul2(c,a,b,r,p,q)):
		print(2)
		
	else:
		print(3)