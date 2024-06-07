import random

hero = {'hp':3,'int':1,'might':5, 'damage':1}
heroitem = {}
shadow = {'hp':1, 'might':3, 'damage':1}

def shadowfight(hero,shadow,heroitem):
    baseshadowmight = shadow['might']
    x = True
    while x:
        if shadow['hp'] == 0:
            print('Тень исчезла')
            x = False
            return [hero,heroitem]
        else:
            dice1 = random.randint(1,6)
            if dice1<=shadow['might']:
                print('Тень атаковала! Вы ранены.')
                shadow['might'] = baseshadowmight
                hero['hp'] -=shadow['damage']
            else:
                print('Тень атаковала, но промахнулась!')
            if hero['hp'] <= 0:
                print('Вы мертвы! Игра окончена.')
                x = False
                return [hero,heroitem]
            choiceaction = int(input('Тень зловеще колеблется перед вашим взором! Действуйте!\n 1.Атаковать\n 2.Атаковать осторожно\n 3.Попытаться уклониться от следущей атаки'))
            if choiceaction == 1:
                dice1 = random.randint(1,6)
                if dice1<=hero['might']:
                    if dice1<=3:
                        shadow['hp'] -=hero['damage']
                        print('Вы ранили тень.')
                    else:
                        print('Ваш выстрел пролетел сквозь тень! Кажется, она стала нематериальной.')
                else:
                    print('Вы промахнулись.')
            elif choiceaction == 2:
                shadow['might'] = shadow['might'] - 2
                hero['might'] = hero['might'] - 1
                dice1 = random.randint(1,6)
                if dice1<=hero['might']:
                    if dice1<=3:
                        shadow['hp'] -=hero['damage']
                        print('Вы ранили тень.')
                    else:
                        print('Ваш выстрел пролетел сквозь тень! Кажется, она стала нематериальной.')
                else:
                    print('Вы промахнулись.')
                hero['might'] = hero['might'] + 1
            elif choiceaction == 3:
                shadow['might'] = shadow['might'] - 3



res = shadowfight(hero,shadow,heroitem)
print(res)