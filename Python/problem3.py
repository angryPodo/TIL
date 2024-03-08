Num_to_Eng = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

def datacat2(strList):
    lengthcount = {}
    for word in strList:
        length = len(word)
        if length in lengthcount:
            lengthcount[length] += 1
        else:
            lengthcount[length] = 1
    result_dict = {k: Num_to_Eng[v] for k, v in lengthcount.items()}
    return result_dict

print(datacat2(['car', 'sun', 'son', 'dive', 'love', 'finalexam', 'python']))
print(datacat2(['information','superficial','great','nice','goodluck','happy']))

