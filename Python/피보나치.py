fibo=[0,1]
fibo={0,1}
while(sum(fibo[-2:])<1000):
    i=sum(fibo[-2:])
    fibo.append(i)

print(fibo)


print(type(fibo))