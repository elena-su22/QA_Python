import random

choice = int(input('Введите количество игроков (1 или 2): '))
if choice == 1:
    listforrandom = [1,2,3,4,5,6,7,8,9]
    listfor4 = []
    numrandom = 0
    for i in range(4):
        numrandom = random.choice(listforrandom)
        listfor4.append(numrandom)
        listforrandom.remove(numrandom)
    v1 = int(''.join(map(str, listfor4)))
elif choice == 2:
    v1 = int(input('Введите число из 4х неповторящихся цифр от 1 до 9: '))
    for i in range(10):
        print('*****')
else:
    print('Введено неверное число игроков')
    v1 = 0
trytoget = 1
v2 = 0
while v1 != v2:
    v2 = int(input('Введите число из 4х неповторящихся цифр от 1 до 9: '))
    if v1 != v2 and trytoget == 10:
        print('LOSE')
        break
    elif v1 == v2:
        print('WIN')
        break
    else:
        strV1 = str(v1)
        strV2 = str(v2)
        listV1 = []
        for i1 in strV1:
            listV1.append(int(i1))
        scoreofget = 0
        scoreofalmostget = 0
        for i1, i2 in zip(strV1, strV2):
            if i1 == i2:
                scoreofget +=1
            elif int(i2) in listV1:
                scoreofalmostget +=1
        print(f'Вы угадали верно {scoreofget} цифр в числе на своей позиции')
        print(f'Вы угадали верно {scoreofalmostget} цифр которые есть в числе, но стоят не на своей позиции')
        trytoget +=1




#вывод рандомных чисел
# import random
# lst = list(range(0, 9+1))
# random.shuffle(lst)
# print(type(lst))
# print(lst)



#
# testlist1 = []
# testofv1number = True
# while testofv1number:
#     print(1)
#     for i in strV1:
#         if int(i) in testlist1:
#             print('Цифры в числе повторяются')
#             testofv1number = False
#         else:
#             testlist1.append(int(i))
#