import requests
import random
import string

# def urlchek(url1):
#     chek = requests.get(url1)
#     status = chek.status_code
#     if status == 200:
#         return True
#     else:
#         return False
    
# print(urlchek('https://easysmarthub.ru/'))

# def generationpass(passlen):
#     all_symbols = string.ascii_uppercase + string.digits + string.punctuation + string.ascii_lowercase
#     result = ''.join(random.choice(all_symbols) for _ in range(passlen))
#     return result
# num = random.randint(8,32)
# print(generationpass(num))

# def numsum(int1):
#     int1 = str(int1)
#     sumnum = 0
#     for i in int1:
#         sumnum = sumnum+int(i)
#     return sumnum
# print(numsum(234))

# with open(r'C:\Users\AttekPC\Desktop\lesson6tx.txt', 'r') as file1:
#     len1 = len(file1.readlines())
#     randnum = random.randint(0,len1-1)
#     # line1 = file1.readlines()
#     # # for i in line1:
#     # #     if line1.index(i) == randnum:
#     # #         print(i)
# file1 = open(r'C:\Users\AttekPC\Desktop\lesson6tx.txt', 'r')
# line1 = file1.readlines()
# for i in line1:
#     if line1.index(i) == randnum:
#         print(i)
# file1.close()

joke_template = [
    'Почему {} катится вниз?',
    'Потому что {} смеятся над ним!',
    'Кто {} в книгах?',
    'Кто {}?',
    'Что сказал {} ему {} когда они встретились ?'
]
joke_elements = [
    'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
    'водитель','улитка'
]
# for i in joke_template:
#     score=0
#     for x in i:
#         if x == {}:
#             score = +1
#     if score == 1:
#         joke = i.format(random.choice(joke_elements))
#         print(joke)
#     else:
#         joke = i.format(random.choice(joke_elements),random.choice(joke_elements))
#         print(joke)
for i in joke_template:
    joke = i.format(*random.sample(joke_elements,i.count('{}')))
    print(joke)


