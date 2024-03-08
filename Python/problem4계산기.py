#감점 1개

x = input("a?")
y = input("b?")
a= int(x)
b = int(y)

def add(a,b):
    val = a+b
    return val

def mul(a,b):
    mut = a*b
    return mut

def div(a,b):
    if b==0:
        dive=0
    else:
        dive = (a/b) #감점
    return dive

def pow(a,b):
    res = a**b
    return res

c1 = add(a,b)
c2 = mul(a,b)
c3 = div(a,b)
c4 = pow(a,b)
print(c1)
print(c2)
print(c3)
print(c4)

