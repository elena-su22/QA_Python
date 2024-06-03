#my_str = 'hello, world'
#print(my_str[-6:-1])
#my_str = 'hello, world'
#print(my_str[:-6:-1])
#my_str = 'hello, world'
#print(my_str[:-7:-2])
#print(my_str[:-2:-7])


#str1 = 'Привет, человек, меня зовут Кот'
#print (len(str1))
#print (str1[17:])
#str1 = str1.replace ('Кот', 'кот')
#print(str1)

#str2 = str(input())
#print (len(str2))
#print (str2[17:])
#str2 = str2.replace ('Кот', 'кот')
#print(str2)


#v1 = str(input('введите v1'))
#v2 = str(input('введите v2'))
#v2 = v2[::-1]
#if v1 == v2 :
 #   print(True)
#else:
 #   print(False)


#v1 = str(input('введите v1'))
#v2 = str(input('введите v2'))
#list1 = sorted (v1)
#list2 = sorted (v2)
#if list1 == list2 :
    #print(True)
#else:
    #print(False)

# также как и блок выше - решение задачи с анаграммой, но верхний мой работает, а нижний записывался на память после объяснения и не работает
#v1 = str(input('введите v1'))
#v2 = str(input('введите v2'))
#def func1 (v1, v2):
 #   w1 = set(v1)
  #  w2 = set(v2)
 #   if w1 == w2:
#return True


v1 = int(input('введите v1'))
v1 = v1%2
if v1 == 0:
    print ('четное')
else:
    print ('нечетное')


v1 = str(input('введите v1'))
list1 = list(v1)
list1 = list1.sort()
v2 = str(input('введите v2'))
list2 = list(v2)
list2 = list2.sort()
def func1 (list1, list2):
    if list1 == list2:
        return True
    else:
        return False