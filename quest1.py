import random

hero1 = {'hp':3,'int':1,'might':5}
beast1 = {'hp':3,'damage':1}

def fight(hero = hero1, beast = beast1):
    def realfight():
        herohp = hero['hp']
        while True:
            print('thp',herohp )
            if beast['hp'] == 2:
                dice1 = random.randint(1,6)
                if dice1<=2:
                    print('Зверь бежал')
                    return hero['hp']-herohp
            elif beast['hp'] == 1:
                dice1 = random.randint(1,6)
                if dice1<=4:
                    print('Зверь бежал')
                    return hero['hp']-herohp
            elif beast['hp'] == 0:
                print('Зверь мертв')
                return hero['hp']-herohp
            else:
                dice1 = random.randint(1,6)
                if dice1<=5:
                    print('Зверь атаковал! Вы ранены')
                    herohp -=1
                else:
                    print('Зверь атаковал, но промахнулся!')
                if herohp == 0:
                    print('Вы мертвы! Игра окончена')
                    return -1
                dice1 = random.randint(1,6)
                if dice1<=hero['might']:
                    beast['hp'] -=1
                    print('Вы ранили зверя')
    fightway = int(input('Вы слышите приближение зверя!\n Выберете что вы хотите делать:\n 1.Бежать\n 2.Скрытно обойти зверя\n 3.Напасть первым'))
    if fightway == 2:
        dice1 = random.randint(1,6)
        if dice1<=hero['int']:
            print('Вы сумели скрытно обойти зверя')
            return 0
        else:
            print('бой')
            return realfight()
    elif fightway == 1:
        dice1 = random.randint(1,6)
        if dice1<=3:
            print('Вы сбежали от зверя')
            ####счетчик времени +
            return 0
        else:
            print('бой')
            return realfight()
    elif fightway == 3:
        dice1 = random.randint(1,6)
        if dice1<=hero['might']:
            beast['hp'] -=1
            print('Вы ранили зверя')
        print('бой')
        return realfight()
print('hp', hero1['hp'])
hero1['hp'] = hero1['hp'] - fight()
print('hp', hero1['hp'])