import random
import math

# v1 = random.randint(1,10)
# v2 = 0
# for i in range(5):
#     v2 = int(input('Введите число: '))
#     if v1 == v2:
#         print('Вы угадали!')
#         break
#     elif v1 > v2:
#         print('Ваше число меньше загаданного')
#     else:
#         print('Ваше число больше загаданного')

# list1 = list(input('Введите несколько элементов: '))
# random.shuffle(list1)
# print(list1)

# v1 = int(input('Введите число: '))
# v2 = int(input('Введите число: '))
# v3 = random.randint(v1,v2)
# print(v3)

# dice1 = random.randint(1,6)
# print(dice1)

# coin1 = ['Орел','Решка']
# tossacoin = random.choice(coin1)
# print(tossacoin)

# box = [2,2,2,2,2,2,2,1]
# random.shuffle(box)
# sum1 = box[0] + box[1]+ box[2] + box[3]
# sum2 = box[4] + box[5]+ box[4] + box[5]
# if sum1 < sum2:
#     sum3 = box[0] + box[1]
#     sum4 = box[2] + box[3]
#     if sum3 < sum4:
#         if box[0] < box[1]:
#             print('Вы нашли фальшивую монету! Когда вы вытаскивали монеты из сундука фальшивка была первой')
#         else:
#             print('Вы нашли фальшивую монету! Когда вы вытаскивали монеты из сундука фальшивка была второй')
#     else:
#         if box[2] < box[3]:
#             print('Вы нашли фальшивую монету! Когда вы вытаскивали монеты из сундука фальшивка была третьей')
#         else:
#             print('Вы нашли фальшивую монету! Когда вы вытаскивали монеты из сундука фальшивка была четвертой')
# else:
#     sum3 = box[4] + box[5]
#     sum4 = box[6] + box[7]
#     if sum3 < sum4:
#         if box[4] < box[5]:
#             print('Вы нашли фальшивую монету! Когда вы вытаскивали монеты из сундука фальшивка была пятой')
#         else:
#             print('Вы нашли фальшивую монету! Когда вы вытаскивали монеты из сундука фальшивка была шестой')
#     else:
#         if box[6] < box[7]:
#             print('Вы нашли фальшивую монету! Когда вы вытаскивали монеты из сундука фальшивка была седьмой')
#         else:
#             print('Вы нашли фальшивую монету! Когда вы вытаскивали монеты из сундука фальшивка была восьмой')
# print(box)

file1 = open(r'C:\Users\AttekPC\Desktop\lesson6tx.txt', 'w')
file1.write("""За ночь долина остыла, а на рассвете стало совсем холодно.
Они шли по насыпи, ступая по сгнившим шпалам между ржавыми рельсами,
и Рэдрик смотрел, как блестят на кожаной куртке Артура Барбриджа
капельки сгустившегося тумана.
Мальчишка шагал легко, весело, словно не было позади томительной ночи,
нервного напряжения, от которого до сих пор тряслась каждая жилка,
двух жутких часов на мокрой макушке плешивого холма,
которые они провели в мучительном полусне, прижавшись друг к другу
спинами для тепла, пережидая поток зеленки, обтекавшей холм и
исчезавшей в овраге.""""")
file1.close()
file1 = open(r'C:\Users\AttekPC\Desktop\lesson6tx.txt', 'r')
print(file1.read())
file1.close()
file1 = open(r'C:\Users\AttekPC\Desktop\lesson6tx.txt', 'r')
line1 = file1.readlines()
for i in line1:
    if line1.index(i) % 2 == 0:
        print(i)
file1.close()
file1 = open(r'C:\Users\AttekPC\Desktop\lesson6tx.txt', 'r')
line1 = file1.readlines()
for i in line1:
    if 'Рэдрик' in i:
        print('Найден в следущей строке')
        print(i)
file1.close()
