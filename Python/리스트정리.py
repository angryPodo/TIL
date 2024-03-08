import random

def drawing_integers(lb,ub,trials):
    list1=[]
    for _ in range(trials):
        list1.append(random.randint(lb,ub))
    return list1
        
def average_integers(list2):
    return sum(list2)/len(list2)

def count_integers(l):
    total = []
    for i in range(min(l),max(l)+1):
        total.append((i,l.count(i)))
    return total


New1 = drawing_integers(1,19,10)

print(New1,"\n")
print(average_integers(New1),"\n")
print(count_integers(New1),"\n")


