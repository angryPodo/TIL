print("환전금액\t기준엔화\t총엔화")
won = [500000, 1100000]
peryen = [9.0, 9.05, 9.07,9.08, 9.09,9.1, 9.11,9.12, 9.13, 9.14, 9.15, 9.16, 9.17,9.18, 9.19, 9.2, 9.25, 9.3]

for i in range(len(won)):
    for j in range(len(peryen)):
        totalyen = won[i] // peryen[j]
        if i == 0:
            print(won[i], "\t\t", peryen[j], "\t\t", totalyen, "엔")
        else:
            print(won[i], "\t", peryen[j], "\t\t", totalyen, "엔")

# 손해 메시지 출력
for j in range(len(peryen)):
    totalyen_0 = won[0] // peryen[j]
    totalyen_1 = won[1] // peryen[j]
    
    if totalyen_0 < 54500:
        print(f"손해 보는느낌의 엔화는 {round(peryen[j]*100)}임. (500,000원 기준)")
    if totalyen_1 < 120000:
        print(f"손해 보는느낌의 엔화는 {round(peryen[j]*100)}임. (1,100,000원 기준)")
