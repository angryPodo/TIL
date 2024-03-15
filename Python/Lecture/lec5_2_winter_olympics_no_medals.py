countries = [ "Australia", "Austria", "Belarus", "Canada", "China", "Croatia", "Czech Republic", "Finland", "France", "Germany", "Great Britain", "Italy", "Japan", "Kazakhstan", "Latvia", "Netherlands", "Norway", "Poland", "Russia", "Slovakia", "Slovenia", "South Korea", "Sweden", "Switzerland", "Ukraine", "United States" ]
gold = [0, 4, 5, 10, 3, 0, 2, 1, 4, 8, 1, 0, 1, 
        0, 0, 8, 11, 4, 13, 1, 2, 3, 2, 6, 1, 9]
silver = [ 2, 8, 0, 10, 4, 1, 4, 3, 4, 6, 1, 2, 4, 0, 
           2, 7, 5, 1, 11, 0, 2, 3, 7, 3, 0, 7]
bronze = [ 1, 5, 1, 5, 2, 0, 2, 1, 7, 5, 2, 6, 3, 1, 
           2, 9, 10, 1, 9, 0, 4, 2, 6, 2, 1, 12]


medal=[(0, 2, 1, 'Australia'), (4, 8, 5, 'Austria'), (5, 0, 1, 'Belarus'), (10, 10, 5, 'Canada'), (3, 4, 2, 'China'), (0, 1, 0, 'Croatia'), (2, 4, 2, 'Czech Republic'), (1, 3, 1, 'Finland'), (4, 4, 7, 'France'), (8, 6, 5, 'Germany'), (1, 1, 2, 'Great Britain'), (0, 2, 6, 'Italy'), (1, 4, 3, 'Japan'), (0, 0, 1, 'Kazakhstan'), (0, 2, 2, 'Latvia'), (8, 7, 9, 'Netherlands'), (11, 5, 10, 'Norway'), (4, 1, 1, 'Poland'), (13, 11, 9, 'Russia'), (1, 0, 0, 'Slovakia'), (2, 2, 4, 'Slovenia'), (3, 3, 2, 'South Korea'), (2, 7, 6, 'Sweden'), (6, 3, 2, 'Switzerland'), (1, 0, 1, 'Ukraine'), (9, 7, 12, 'United States')]

for item in medal:
  print(sum(item[0:3]),item[-1:])

#def no_medals(countries, a1, b1):
#  result = []
#  for i in range(len(countries)):
 #   if a1[i] == 0 and b1[i] == 0:
  #    result.append(countries[i])
  #return result

#only_gold = no_medals(countries, silver, bronze)
#only_silver = no_medals(countries, gold, bronze)
#only_bronze = no_medals(countries, gold, silver)

#only_one = only_gold + only_silver + only_bronze

#print (only_one)