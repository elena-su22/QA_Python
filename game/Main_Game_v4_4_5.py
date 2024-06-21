import pygame
import random
from z2locationAll1_5 import location
from z2basefight1_5 import fight
from z2startlocation1_5 import startloc

hero = {'hp':3,'int':1,'might':5, 'damage':1}
heroitestart = {'Титул':'Никто'}
#heroitem = {'Нелегальные стимуляторы': 1, 'Осколочная граната':1, 'Кейс с вакциной':10}
locforest ={'locID':1,'locname':'forest','eventlist':['Храм','Бурелом','Бурелом','Безопасно','Безопасно','Безопасно','Бой','Бой','Бой','Бой']}
locplain ={'locID':2,'locname':'plain','eventlist':['Храм','Безопасно','Безопасно','Опасный бой','Опасный бой','Опасный бой','Бой','Бой','Бой','Бой']}
locswamp ={'locID':3,'locname':'swamp','eventlist':['Храм','Трясина','Трясина','Трясина','Трясина','Безопасно','Безопасно','Безопасно','Бой','Бой']}
loctypes = [locswamp,locplain,locforest]
beastlist = [{'name':'beast1','hp':3,'might':4,'damage':1},{'name':'beast2','hp':4,'might':2,'damage':1},{'name':'beast3','hp':2,'might':5,'damage':1}]
dangerbeastlist =[{'name':'bigbeast','hp':6,'might':4,'damage':1},{'name':'strongbeast','hp':4,'might':4,'damage':2},{'name':'fastbeast','hp':4,'might':4,'damage':1}]
littlehurtlist = ['Проклятье! Вы спотыкаетесь о выступающий из земли корень и падаете.\nПотянутая ладыжка ноет от боли, но вы заставляете себя подолжать двигаться','Вы стремительно бежите через густой подлесок, решительно прорываясь сквозь сплетения ветвей встречающиеся на вашем пути.\nВнезапно быстрая тень мелькает перед вашим лицом и вспышка боли пронзает плечо.\nКажется, в спешке вы потревожили какое-то животное']


GRID_SIZE = 12
CELL_SIZE = 40
INFO_AREA_HEIGHT = CELL_SIZE * 5  

FOG_COLOR = (169, 169, 169)
COLORS = {
    '0': (0, 255, 0), #start,end,swamp,field,forest
    '1': (255, 0, 0),
    '2': (102, 51, 0),
    '3': (0, 255, 255),
    '4': (34, 139, 34),      
}

images = {
    '0': pygame.image.load('D:\Studypython24\Studypython24042024\game\\deadship1.jpg'),
    '1': pygame.image.load('D:\Studypython24\Studypython24042024\game\\fin.jpg'),
    '2': pygame.image.load('D:\Studypython24\Studypython24042024\game\\swamp1.jpg'),
    '3': pygame.image.load('D:\Studypython24\Studypython24042024\game\\plain1.jpg'),
    '4': pygame.image.load('D:\Studypython24\Studypython24042024\game\\tropicforest1.jpg'),
 }

def create_grid():
    locations = ['2', '3', '4']
    grid = [[random.choice(locations) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    def get_random_position():
        return random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)
    start = get_random_position()
    while True:
        end = get_random_position()
        if (start[0] - end[0] >= 6 or end[0] - start[0] >= 6) or (start[1] - end[1] >= 6 or end[1] - start[1] >= 6):
            break
    grid[start[0]][start[1]] = '0'
    grid[end[0]][end[1]] = '1'
    return grid, start
def draw_grid(screen, grid, visibility):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            color = COLORS[grid[y][x]] if visibility[y][x] else FOG_COLOR
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, color, rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

def location_display(screen, cell_type, images): 
    if cell_type in images:
        screen.blit(images[cell_type], (0, GRID_SIZE * CELL_SIZE))

def transition_to_scene(i):
    print(f'Текущая локация: {i}')
    print(type (i))
    print("Переход на локацию")
    if int(i)==0:
        heroitem = startloc(hero,heroitestart)
        print(heroitem)
        return heroitem
    if int(i)!=0:
        heroitem = {}
        location(int(i),loctypes,hero,heroitem,beastlist,dangerbeastlist)
        print(hero)
        return hero
 
####как мы делаем события?? фон после перехода всегда одинаковый?
            
def main():
    pygame.init()
    screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE+INFO_AREA_HEIGHT))
    pygame.display.set_caption("Туман")
    font = pygame.font.SysFont(None, 36)
    grid, player_pos = create_grid()
    visibility = [[False] * GRID_SIZE for _ in range(GRID_SIZE)]
    visibility[player_pos[0]][player_pos[1]] = True
    running = True
    # clock = pygame.time.Clock() #### 
    text_rect = pygame.Rect(100, GRID_SIZE * CELL_SIZE + 10, 200, 170)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                new_position = list(player_pos)
                if event.key == pygame.K_UP:
                    new_position[0] = max(0, player_pos[0] - 1)
                if event.key == pygame.K_DOWN:
                    new_position[0] = min(GRID_SIZE - 1, player_pos[0] + 1)
                if event.key == pygame.K_LEFT:
                    new_position[1] = max(0, player_pos[1] - 1)
                if event.key == pygame.K_RIGHT:
                    new_position[1] = min(GRID_SIZE - 1, player_pos[1] + 1)
                if new_position != player_pos:
                    player_pos = list(new_position)
                    visibility[player_pos[0]][player_pos[1]] = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_rect.collidepoint(event.pos):
                    transition_to_scene(grid[player_pos[0]][player_pos[1]])
        screen.fill((0, 0, 0))
        draw_grid(screen, grid, visibility)
        location_display(screen, grid[player_pos[0]][player_pos[1]], images)
        text_surface = font.render('Перейти', True, (255, 255, 255))
        screen.blit(text_surface, text_rect.center)
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()