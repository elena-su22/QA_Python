import random
from z2basefight1_2 import fight

locname1 = 'forest'
locname2 = 'swamp'
locname3 = 'plain'
hero1 = {'hp':3,'int':1,'might':5, 'damage':1}
heroitem1 = {'Нелегальные стимуляторы': 1, 'Осколочная граната':1, 'Кейс с вакциной':10}
beastlist = [{'name':'beast1','hp':3,'might':4,'damage':1},{'name':'beast2','hp':4,'might':2,'damage':1},{'name':'beast3','hp':2,'might':5,'damage':1}]
dangerbeastlist =[{'name':'bigbeast','hp':6,'might':4,'damage':1},{'name':'strongbeast','hp':4,'might':4,'damage':2},{'name':'fastbeast','hp':4,'might':4,'damage':1}]
littlehurtlist = ['Проклятье! Вы спотыкаетесь о выступающий из земли корень и падаете.\nПотянутая ладыжка ноет от боли, но вы заставляете себя подолжать двигаться','Вы стремительно бежите через густой подлесок, решительно прорываясь сквозь сплетения ветвей встречающиеся на вашем пути.\nВнезапно быстрая тень мелькает перед вашим лицом и вспышка боли пронзает плечо.\nКажется, в спешке вы потревожили какое-то животное']
eventlistforest = ['Храм','Бурелом','Бурелом','Безопасно','Безопасно','Безопасно','Бой','Бой','Бой','Бой']
eventlistswamp = ['Храм','Трясина','Трясина','Трясина','Трясина','Безопасно','Безопасно','Безопасно','Бой','Бой']
eventlistplain = ['Храм','Безопасно','Безопасно','Опасный бой','Опасный бой','Опасный бой','Бой','Бой','Бой','Бой']

def location(locname=locname1,eventlistx = eventlistforest, hero=hero1):
    print('Продвигаясь дальше вы оказываетесь под густой сенью леса. Ветви над вами плотно сплетены и почти не пропускают свет. Вокруг слышны многоголосые переклички птиц и стрекот насекомых. Это место кажется потным жизни.\nНеумолимо утекающее время на дисплее хранилища призывает вас поторопиться, но бежать через густой лес может быть опасно. Что делать?\n 1. Бежать\n 2. Идти осторожно') if locname == 'forest' else None
    print('Перед вами простирается болото. Редкие кривые деревца виднеются вдали. Земля вокруг покрыта мхом к короткой травой. Дорога кажется безопасной, но вы знаете, что это ощущение обманчиво. Придется двигаться осторожно.') if locname == 'swamp' else None
    print('Насколько хватает взгляда вы видите покрытую высокой травой равнину. Вокруг клубится туман, скрадывая ваше окружение. Что это там, вдалеке? Небольшие заросли кустов? Или там притаился зверь? Чтож, по крайней мере вы можете двигаться быстро!') if locname == 'plain' else None
    speedchoice1 = int(input('Выбор'))
    if speedchoice1 ==1:
        print('Нельзя терять ни минуты! Вы бежите')
        heroitem1['Кейс с вакциной']-=1
        ### время на общем таймере +1
        if random.randint(1,6)>hero['might'] and locname == 'forest':
            print(random.choice(littlehurtlist))
            hero['hp']-=1
    elif speedchoice1 ==2:
        print('Вы не собираетесь рисковать покалечиться из-за спешки.\nВы никому не поможете, если не доберетесь до города живым.')
        heroitem1['Кейс с вакциной']-=2
        ### время на общем таймере +2
    for i in range(3):
        event = random.choice(eventlistx)
        print(event)
        eventlistx.remove(event)
        if event == 'Храм':
            print('Храм')
            #import Temple_of_the_dark_v_0
            ###temple(def)
            continue
        elif event == 'Бурелом' or event=='Трясина':
            speedchoice2 = int(input('Перед вами непроходимый бурелом. Деревья здесь повалены и переплетены между собой так плотно, что кажется нет никакой надежды пробраться. Что делать?\n 1. Пытаться пробраться\n 2. Обойти бурелом')) if locname == 'forest' else None
            speedchoice2 = 2 if locname == 'swamp' else None 
            print('Почва под вашими ногами влажно чавкает. Все чаще и глубже вы проваливаетесь во влажный топкий мох. Наконец, вы выходите к зыбкому, покрытому ряской и тиной участку, преодолеть который нет никакой надежды. Придется идти в обход.') if locname == 'swamp' else None
            if speedchoice2 ==1:
                print('Нельзя терять ни минуты! Вы пытаетесь пробраться между стволами деревьев')
                if random.randint(1,6)>hero['might']+2:
                    hero['hp']-=1
                    print('Вы протискиваетесь сквозь завал с трудом и выбираетесь в другой стороны полностью исцарапанным и с растянутым плечом')
                    continue
                else:
                    print('Вы протискиваетесь сквозь завал с трудом, но выбираетесь с дугой стороны относительно целым')
                    continue
            elif speedchoice2 ==2:
                print('Вы не собираетесь рисковать покалечиться из-за спешки.\nВы никому не поможете, если не сумеете добраться до города живым.')
                heroitem1['Кейс с вакциной']-=1
                ### время на общем таймере +1
                continue
        elif event == 'Безопасно':
            print('Вы продвигаетесь через густой лес внимательно прислушиваясь и напряженно сжимая в руке бластер, но кажется здесь нет ничего, что могло бы представлять для вас угрозу.')
            continue
        elif event == 'Бой':
            beastx = random.choice(beastlist)
            fight(hero,beastx)
            continue  
        elif event == 'Опасный бой':
            beastx = random.choice(dangerbeastlist)
            fight(hero,beastx)
            continue  



#location(locname1,eventlistforest,hero1)






            