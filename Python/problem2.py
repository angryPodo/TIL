L = ['car',6,2,7.5,'banana','car',6,5]
L2 = ['cat','cat','cat','dog','dog',3,3,3]

def datacat(l):
    first_list = []
    for i in l:
       first_list.append((i,l.count(i)))
    remove_list = set(first_list)
    final_list = list(remove_list)
    return final_list



print(datacat(L))
print(datacat(L2))





