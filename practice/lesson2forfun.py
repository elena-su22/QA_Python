
mark1 = str(input('Введите марку: Лада или Иномарка'))
year1 = int(input('Введите год выпуска: '))
prob1 = int(input('Введите пробег: '))
sost1 = str(input('Введите состояние: Новый или Б/у'))
if mark1 == 'Лада':
    mark1 = 1
elif mark1 == 'Иномарка':
    mark1 = 2
else:
    mark1 = 0
    print('Данные марки введены неверно')
if year1 > 2020:
    year1 = 4
elif year1 > 2015:
    year1 = 3
elif year1 > 2010:
    year1 = 2
elif year1 > 2005:
    year1 = 1
else:
    year1 = 0
    print('Машины старше 20 лет не принимаются')
if prob1 > 50000:
    prob1 = 1
elif prob1 <= 50000 and prob1 >= 0 :
    prob1 = 2
else:
    prob1 = 0
    print('Данные пробега введены неверно')
if sost1 == 'Б/у':
    sost1 = 1
elif sost1 == 'Новый':
    sost1 = 2
else:
    sost1 = 0
    print('Данные состояния введены неверно')
listauto1 = [mark1, year1, prob1, sost1]
sumauto1 = 0
for koef in listauto1:
    if koef == 0:
        print('Продажа машины невозможна')
        break
    else:
        sumauto1 += koef
#print (sumauto1)
if sumauto1 >= 10:
    print ('Цена автомобиля 200000')
elif sumauto1 > 8:
    print ('Цена автомобиля 150000')
elif sumauto1 > 6:
    print ('Цена автомобиля 100000')
elif sumauto1 > 4:
    print ('Цена автомобиля 100000')
elif sumauto1 > 2:
    print ('Цена автомобиля 75000')
elif sumauto1 > 0:
    print ('Цена автомобиля 50000')


# не работает пока внесение данных в лист через цикл, надо разобраться как через цикл for создать список
mark2 = 0
year2 = 0
prob2 = 0
sost2 = 0
list2 = [mark2, year2, prob2, sost2]
for element2 in list2:
    element2 = input('Введите данные: марку, год выпуска, пробег, состояние автомобиля')
print(list2)

