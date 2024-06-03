#list1 = [1, 3, 11, 7, 9, 5]
#print(sum(list1))
#print(max(list1))
#print(min(list1))
#print(len(list1))
#list1 = sorted(list1)
#print(list1)
#list1.reverse()
#print(list1)
#print(sorted(list1, reverse=True))
#list2 = [2, 4, 6, 8, 10]
#list3 = list1 + list2
#print(list3)

#действия выполняются изнутри наружу
#list4 = [1, 1, 2, 3, 4, 4, 4]
#listuniq4 = list(set(list4))
#print(listuniq4)
# Это то же самое, как если бы я перевела лист в множество, а потом обратно в лист
#set4 = set (list4)
#print(set4)
#listuniq4 = list(set4)
#print (listuniq4)

import re

# поиск пересечений между списками: 1. через функцию сравнения множеств, 2. через перебор в цикле for   
# list5 = [1, 2, 3, 4, 5]
# list6 = [2, 4, 6, 8, 10]
# set5 = set(list5)
# set6 = set(list6)
# setunion = set5.intersection(set6)
# listunion = list(setunion)
# print(listunion)

# list7 = []
# for v in list5:
#     if v in list6:
#         list7.append(v)
# print(list7)

# range (start, stop, range)
#for i in range(2,21,2):
#    print(i)
# for i in range(2,11,2):
#     print(i)

# list8 = list(range(1,11))
# for i in list8:            #better for i in range(1,11): whithout making list
#     if i % 2 == 0:
#         print(i)

# 1
# listthings = ['chiken', 'beef', 'pork', 'lamb', 'turkey']
# listprice = [100, 200, 300, 400, 500]
# sum = 0
# dict1 = {'chiken':100, 'beef':200, 'pork':300, 'lamb':400, 'turkey':500}
# for t, p in dict1.items():
#     sum += p
# if sum > 1000:
#     finalsum = sum*90/100
# else:
#     finalsum = sum
# print(finalsum)


# sum2 = 0
# list10 = list(input('chiken/beef/pork/lamb/turkey'))
# for t, p in dict1.items():
#     if t in list10:
#         sum2 += p
# if sum2 > 1000:
#     finalsum2 = sum2*90/100
# else:
#     finalsum2 = sum2
# print(finalsum2)

text = "There are many variants of Lorem Ipsum, but most of them do not always have acceptable modifications, for example, humorous inserts or words that do not even remotely resemble Latin. If you need Lorem Ipsum for a serious project, you probably don't want some joke hidden in the middle of a paragraph. Also, all other well-known Lorem Ipsum generators use the same text, which they simply repeat until they reach the desired volume."
textwithoutpunct = re.sub(r'[^\w\s]', '', text)
listtext1 = textwithoutpunct.split()
# settext2 = set(listtext1)
# for i in settext2:
#     print(i)
#     print(listtext1.count(i))


    


