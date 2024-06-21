import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load('C:\\Users\\AttekPC\\Desktop\\game\\smoke1.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


font = pygame.font.Font(None, 28)

def render_line(line, pos, speed):
    for i in range(len(line)):
        rendered_text = font.render(line[:i+1], True, WHITE)
        screen.blit(rendered_text, pos)
        pygame.display.update()
        pygame.time.delay(speed)
        
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.WINDOWFOCUSLOST or event.type == pygame.ACTIVEEVENT and not pygame.display.get_active():
                
                while not pygame.display.get_active():
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        pygame.time.delay(100)

    return rendered_text


def display_text(text, pos, speed=1):
    screen.blit(background, (0, 0))
    if isinstance(text, list):
        for line in text:
            text_surf = font.render(line, True, WHITE)
            for i in range(len(line)):
                screen.blit(font.render(line[:i+1], True, WHITE), pos)
                pygame.display.update()
                pygame.time.delay(speed)
            pos = (pos[0], pos[1] + 40)  # Перемещаем на новую строку
    else:
        text_surf = font.render(text, True, WHITE)
        for i in range(len(text)):
            screen.blit(font.render(text[:i+1], True, WHITE), pos)
            pygame.display.update()
            pygame.time.delay(speed)
    return text_surf

def leave_temple():
    if random.choice([True, False]):
        display_text("Своим невежеством вы разневали бога", (50, 300))
        pygame.time.delay(1500)


        battle()
    else:
        display_text("Вы покинули храм", (50, 300))
        pygame.time.delay(1500)

        start()

def battle():
    display_text("Началось сражение...", (50, 400))


def start():
    screen.fill(BLACK)

    text = [
        "Когда вы подходите к полуразрушенным вратам храма,",
        "чувствуете, как холодный ветер пронизывает воздух,",
        "принося с собой зловещий шепот.", 
        "Стены древнего строения увиты мрачной темной лианой,",
        "а каменные гаргульи, покрытые мхом," ,
        "словно следят за каждым вашим шагом." ,
        "С каждым вдохом воздух становится более тяжелым,",
        "пропитанным невыразимым страхом.",
        "Входя в храм, вы ощущаете леденящий ужас,",
        "будто бы кто-то или что-то наблюдает за вами из тьмы.",
    ]

    display_text(text, (100, 10))

    # Отображаем кнопки
    leave_button = font.render("Попытаться покинуть храм", True, WHITE)
    enter_button = font.render("Идти вглубь", True, WHITE)
    screen.blit(leave_button, (WIDTH//2, HEIGHT//1.1))
    screen.blit(enter_button, (WIDTH//4, HEIGHT//1.1))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if leave_button.get_rect(topleft=(WIDTH//2, HEIGHT//1.1)).collidepoint(mouse_pos):
                    screen.fill(BLACK)
                    leave_temple()
                elif enter_button.get_rect(topleft=(WIDTH//4, HEIGHT//1.1)).collidepoint(mouse_pos):
                    screen.fill(BLACK)
                    Main_hall()

def Main_hall():
    screen.fill(BLACK)

    text = [
        "Вы входите в главный зал храма.",
        "Величественное помещение окутано мистической атмосферой,", 
        "стены из черного камня украшены древними барельефами,",
        "пытаясь всмотреться вы начинаете ощущать на себе взгляд",
        "тьма сгущается, а в душе появляются сомнения",
        "пока вы не готовы принять эту тьму...",       
    ]
    #тут надо какие-нибудь условия бахнуть, чтобы пройти проверку бога. Глобалочка с репутацией
    text2 = [
        "Немного прийдя в себя вы обращаете внимание на обелиск,",
        "От обелиска исходит едва заметный свет, освещая три разных пути,",
        "ведущих в неизвестность",      
    ]
    display_text(text, (100, 10))
    pygame.time.delay(5500)
    screen.fill(BLACK)
    display_text(text2, (100, 10))

    # Отображаем кнопки
    start_button = font.render("Вернуться к входу", True, WHITE)
    down_button = font.render("Cпуститься в тьму", True, WHITE)
    up_button = font.render("Подняться выше", True, WHITE)
    center_button = font.render("Идти вглубь", True, WHITE)
    screen.blit(start_button, (WIDTH//2, HEIGHT//1.1))
    screen.blit(down_button, (WIDTH//4, HEIGHT//1.1))
    screen.blit(up_button, (WIDTH//2, HEIGHT//1.25))
    screen.blit(center_button, (WIDTH//4, HEIGHT//1.25))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if start_button.get_rect(topleft=(WIDTH//2, HEIGHT//1.1)).collidepoint(mouse_pos):
                    screen.fill(BLACK)
                    start()
                elif down_button.get_rect(topleft=(WIDTH//4, HEIGHT//1.1)).collidepoint(mouse_pos):
                    screen.fill(BLACK)
                    altar()
                elif up_button.get_rect(topleft=(WIDTH//4, HEIGHT//1.25)).collidepoint(mouse_pos):
                    screen.fill(BLACK)
                    chest()
                elif center_button.get_rect(topleft=(WIDTH//4, HEIGHT//1.25)).collidepoint(mouse_pos):
                    screen.fill(BLACK)
                    manuscript()


def manuscript():
    screen.fill(BLACK)

    text = [
        "Пыльный манускрипт лежит на каменном пьедестале",
        "Когда вы берете его в руки,страницы издают скрипящий звук,",
        "нарушая мертвую тишину.",
        "Слова на древнем языке светятся зловещим красным огнем,",
        "а при чтении текст словно проникает в глубину вашего разума.", 
        "Вам кажется, что стены начинают дрожать,", 
        "а тени вокруг вас оживают, принимая зловещие формы.", 
        "Сердце бьется учащенно,", 
        "охватывая смесь древнего знания и невыразимого ужаса.",
    ]
    
    display_text(text, (50, 100))

    true_button = font.render("Прикоснуться к древним знаниям", True, WHITE)
    exit_button = font.render("Вернуться в основной зал", True, WHITE)
    screen.blit(true_button, (WIDTH//2, HEIGHT//1.1))
    screen.blit(exit_button, (WIDTH//4, HEIGHT//1.1))
    pygame.display.update()

    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                
                if true_button.get_rect(topleft=(WIDTH//2, HEIGHT//1.1)).collidepoint(mouse_pos):
                    screen.fill(BLACK)
                    display_text("Вы впадаете в безумие", (50, 300))
                    pygame.time.delay(3500)
                    start()
                    # Cперва проверка интл.если true = Def на открытие всех клеток тумана/выхода, false =безумие
                    # пока заглушка
                elif exit.get_rect(topleft=(WIDTH//4, HEIGHT//1.1)).collidepoint(mouse_pos):
                    screen.fill(BLACK)
                    display_text("Тьма обращает на вас внимание", (50, 300))
                    pygame.time.delay(3500) # def шанс встретить сильного монстра на игровом поле + 1.1
                    start()

def chest():
    screen.fill(BLACK)

    text = [
        "Вы обнаруживаете старый деревянный сундук, покрытый слоями пыли и паутины.",
        "При прикосновении к нему, чувствуется дрожь, пробегающая по телу,",
        "как будто что-то внутри сопротивляется открытию.",
        "На крышке видны резные символы, почти стертые временем.",
        "Когда сундук наконец открывается, воздух наполняется зловещим шепотом.",
    ]

#Проверка на силу. Провал смерть/успех = бой
    text2 = [
        "Вы протягиваете руку к первому предмету, как вдруг сундук дергается.",
        "Крышка с грохотом захлопывается, а затем снова открывается, но уже самостоятельно.",
        "Обнажаются острые, окровавленные зубы, скрытые на внутренней стороне крышки.",
        "Сундук начинает выгибаться, как живое существо, обнажая глаз,",
        "сверлящий вас подозрительным взглядом.",
        "Вы понимаете: это вовсе не сундук...",
    ]
    display_text(text, (100, 10))
    pygame.time.delay(5500)
    screen.fill(BLACK)
    display_text(text2, (100, 10))
    pygame.time.delay(5500)
    situation = random.randint(0, 1)
    if situation == 0:
        display_text("бой", (50, 300))
        pygame.time.delay(2500)
        start()
    elif situation == 1:
        display_text("вы мертвы", (50, 300))
        pygame.time.delay(2500)
        start()
        
def altar():
    screen.fill(BLACK)

    text = [
        "Вы подходите к бросающему дрожь алтарю, стоящему в центре зала.",
        "На его поверхности высечены символы,",
        "столь древние, что ваше сердце невольно замирает.", 
        "Ощущение глубокого ужаса захватывает вас, когда видите засохшую кровь,",
        "пролитую на каменный престол.",
        "Внезапно, темные тени начинают двигаться вокруг,",
        "а в воздухе раздается эхом громкий шепот неизвестного языка.",
        "Вы чувствуете, как что-то поворачивается внутри алтаря,",
        "и время останавливается.", 
        "Присутствие зла становится невыносимо ощутимым,", 
        "и каждый вздох наполняется отчаянием.",
    ]

    #2 проверки - 2 диалога
    #1 проверка интеллект. Провал - безумие = смерть. 
    #2 проверка на силу. Сзади появляется верховный жрец и толкает нас на алтарь. Провал = мгновенная смерть. Успех = бой

    display_text(text, (100, 10))
    pygame.time.delay(5500)
    screen.fill(BLACK)
    situation = random.randint(0, 2)
    if situation == 0:
        display_text("бой", (50, 300))
        pygame.time.delay(2500)
        start()
    elif situation == 1:
        display_text("Вы впали в безумие", (50, 300))
        pygame.time.delay(2500)
        start()
    else:
        display_text("Вас принесли в жертву богу", (50, 300))
        pygame.time.delay(5500)
        start()
        


start()
