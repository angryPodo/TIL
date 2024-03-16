myWord = input().upper()
freq = {} # 알파벳에 따른 빈도를 구하기 위해 dict사용

for c in myWord:
    if c in freq:
        freq[c] += 1 #재등장한 문자 +1
    else:
        freq[c] = 1 #처음 등장한 문자는 1
        
maxFreq = max(freq.values()) #max()로 벨류리스트의 최댓값
maxChar = []

for k,v in freq.items(): # 키,벨류 대입
    if v == maxFreq:# 빈도가 최대일때
        maxChar.append(k)# 그때의 키를 추가(중복고려)
        
if len(maxChar)==1:
    print(maxChar[0])
else:
    print('?')