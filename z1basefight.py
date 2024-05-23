import random

hero1 = {'hp':3,'int':1,'might':5, 'damage':1}
beast1 = {'hp':3,'might':4,'damage':1}
heroitem1 = {'Нелегальные стимуляторы': 2, 'Осколочная граната':2, 'Кейс с вакциной':10}

def fight(hero = hero1, beast = beast1):
    def realfight():
        herohp = hero['hp']
        x = True
        while True:
            if beast['hp'] == 2:
                dice1 = random.randint(1,6)
                if dice1<=2:
                    print('Раненный зверь проявляет осторожность и отступает')
                    x = False
                    return hero['hp']-herohp
            elif beast['hp'] == 1:
                dice1 = random.randint(1,6)
                if dice1<=4:
                    print('Тяжело раненный зверь в ужасе бежит')
                    x = False
                    return hero['hp']-herohp
            elif beast['hp'] == 0:
                print('Зверь мертв')
                x = False
                return hero['hp']-herohp
            else:
                dice1 = random.randint(1,6)
                if dice1<=beast['might']:
                    print('Зверь атаковал! Вы ранены')
                    beast['might'] = 5
                    herohp -=1
                else:
                    print('Зверь атаковал, но промахнулся!')
                if herohp == 0:
                    print('Вы мертвы! Игра окончена')
                    x = False
                    return 10
                choiceaction = int(input('Зверь оскалил зубы и рычит! Действуйте!\n 1.Атаковать\n 2.Атаковать осторожно\n 3.Попытаться уклониться от следущей атаки'))
                if choiceaction == 1:
                    dice1 = random.randint(1,6)
                    if dice1<=hero['might']:
                        beast['hp'] -=1
                        print('Вы ранили зверя')
                    else:
                        print('Вы промахнулись')
                elif choiceaction == 2:
                    beast['might'] = beast['might'] - 1
                    hero['might'] = hero['might'] - 1
                    dice1 = random.randint(1,6)
                    if dice1<=hero['might']:
                        beast['hp'] -=1
                        print('Вы ранили зверя')
                    else:
                        print('Вы промахнулись')
                    hero['might'] = hero['might'] + 1
                elif choiceaction == 3:
                    beast['might'] = beast['might'] - 2
    fightway = int(input('Вы слышите приближение зверя!\n Выберете что вы хотите делать:\n 1.Бежать\n 2.Скрытно обойти зверя\n 3.Напасть первым\n 4.Использовать вещи из инвертаря'))
    if fightway == 2:
        print('Вы пытаетесь спрятаться')
        dice1 = random.randint(1,6)
        if dice1<=hero['int']:
            print('Вы сумели скрытно обойти зверя')
            return 0
        else:
            print('Скрыться не удалось! Начинается бой!')
            return realfight()
    elif fightway == 1:
        print('Вы пытаетесь бежать')
        dice1 = random.randint(1,6)
        if dice1<=3:
            print('Вы сбежали от зверя')
            ####счетчик времени +
            return 0
        else:
            print('Сбежать не удалось! Начинается бой!')
            return realfight()
    elif fightway == 3:
        print('Недожидаясь появления зверя вы быстро атакуете')
        dice1 = random.randint(1,6)
        if dice1<=hero['might']:
            beast['hp'] -=1
            print('Вы ранили зверя')
        else:
            print('Вы промахнулись')
        print('Начинается бой!')
        return realfight()
    elif fightway == 4:
        choiceitem = input(f'Вы судрожно ищете в своих карманах что-то полезное.\nУ вас есть: {list(heroitem1.keys())}\nЧто из этого вы хотите использовать?')
        print(f'Вы судрожно ищете в своих карманах что-то полезное.\nУ вас есть: {list(heroitem1.keys())}\nЧто из этого вы хотите использовать?')
        if choiceitem == 'Нелегальные стимуляторы':
            print('1')

        return 0
    
hero1['hp'] = hero1['hp'] - fight()
print('hp', hero1['hp'])