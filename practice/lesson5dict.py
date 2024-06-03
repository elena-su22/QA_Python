# словари, начали новый док файл с лекцией
# str1 = str(input('слово '))
# list1 = []
# dict1 = {}
# for i in str1:
#     if i in list1:
#         dict1[i] = dict1[i]+1
#     else:
#         list1.append(i)
#         dict1[i] = 1
# print(dict1)
#другой вариант в одну строку

#вывод рандомных чисел
# import random
# lst = list(range(0, 9+1))
# random.shuffle(lst)
# print(type(lst))
# print(lst)

# 1
dictintuple = {'a':1,'b':2,'c':3,'d':4}
listfortuple = []
for i,ii in dictintuple.items():
    newtuple = (i, ii)
    listfortuple.append(newtuple)
print(listfortuple)

#2

workdict = {}
for i in range(5):
    k1 = str(input('Name: '))
    v1 = int(input('Hours: '))
    workdict[k1] = v1
print(workdict)
