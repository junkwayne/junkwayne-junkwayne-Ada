a = 5
b ="5"
print(a == b)


def diff_21(n):
	if n <=21:
		return 21-n
	else:
		return (n-21)*2

print(diff_21(25))


def first(a,b):
	a = 25
	return a + b

def second (a,c):
	c = a
	return c*2

a = 5
b = 10
c = 15

a = first (5,10) # a = 35
c = second (a,c) # c = 70

print (c)

print(99 !="99")