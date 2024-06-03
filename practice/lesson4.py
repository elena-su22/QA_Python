#1
list1 = [1, 2, 3, 4, 5, -3, 6, 7]
for i in list1:
    if i < 0:
        print(i)
        break
else:
    print('нет отриц чисел')

#2

for i in range(1, 11):
    if i == 5 or i == 6:
        continue
    print(i)

# range отдельный класс, в лист записывается для получения последовательности так:
# list2 = list(range(1,11))
# print(list2)
# print(type(list2))
 
list_1 = ['a','b','c']
list_2 = [1,2,3]
list3 = list(zip(list_1, list_2))
print(list3)
for item1, item2 in zip(list_1,list_2):
    print(item1,item2)

#3
listtest = [75, 90, 85, 60, 95]
listprog = [80, 70, 90, 85, 75]
for it, ip in zip(listtest, listprog):
    if it > 80 and ip > 80:
        print('студент', int(listtest.index(it))+1, 'получил оценки', it, ip)

#1
v1 = int(input('Введите число: '))
sum = 0
for i in range(1, v1+1):
    sum += i
print(sum)
#2
v2 = int(input('Введите число: '))
listtestnum = [1, 3, 5, 7, 9, 11, 13]
for i in listtestnum:
    if v2 == i:
        print('число есть в списке')
else:
        print('числа нет в списке')

#
v3 = 10
v4 = 15
copyv3 = []
copyv4 = []
while len(copyv3) < 5 and len(copyv4) < 5:
    copyv3.append(v3)
    copyv4.append(v4)
    print('резервные копии v3', copyv3, ', резервные копии v4', copyv4,)
n=1
for v, vv in zip(copyv3, copyv4):
    print('копия v3 номер', copyv3.index(v)+n, 'создана:', v)
    print('копия v4 номер', copyv4.index(vv)+n, 'создана:', vv)
    n +=1
print('общее число копий v3 =', len(copyv3))
print('общее число копий v4 =', len(copyv4))

