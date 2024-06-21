import pygame
import sys 

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('C:\\Users\\AttekPC\\Desktop\\game\\smoke1.jpg') #чтобы работало вставь другое изображение 'C:\\Users\\AttekPC\\Desktop\\game\\smoke1.jpg'
background = pygame.transform.scale(background, (screen_width, screen_height))



rooms = [
    {
        "description": "Вы ступаете в заброшенный храм, окружённый густым лесом. Тень от высоких деревьев падает на мраморные колонны, покрытые мхом и плесенью. Вы чувствуете холодный ветерок, который проникает через щели в стенах храма, и слышите тихие шелест листьев, словно шепот древних существ.",
        "actions": ["Подойти к одному из алтарей и попытаться прочитать древний текст", "Исследовать стены зала в поисках каких-либо тайных дверей", "Попытаться уйти"]
    },
    {
        "description": "",
        "actions": [""]
    },
    {
        "description": "",
        "actions": [""]
    }
]

current_room = 0

def render_text(text, font_size, color=(255, 255, 255)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def draw_room(room_index):
    screen.blit(background, (0, 0))
    room_desc, room_rect = render_text(rooms[room_index]["description"], 24)
    room_rect.topleft = (20, 20)
    screen.blit(room_desc, room_rect)
    

    action_positions = []
    for i, action in enumerate(rooms[room_index]["actions"]):
        action_text, action_rect = render_text(action, 24)
        action_rect.topleft = (20, 80 + 30 * i)
        screen.blit(action_text, action_rect)
        action_positions.append(action_rect)
    
    return action_positions

####
def get_new_room(current_room, action):
    if action == "Подойти к одному из алтарей и попытаться прочитать древний текст":
        return (current_room + 1) % len(rooms)
    elif action == "Исследовать стены зала в поисках каких-либо тайных дверей":
        return (current_room - 1) % len(rooms)
 
 ####


pygame.display.set_caption("КАК СДЕЛАТЬ НОРМАЛЬЫНЙ ПЕРЕНОС СТРОКИИИИИИ?!>_<")

running = True

action_positions = draw_room(current_room)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            for i, rect in enumerate(action_positions):
                if rect.collidepoint(mouse_pos):
                    selected_action = rooms[current_room]["actions"][i]
                    current_room = get_new_room(current_room, selected_action)
                    action_positions = draw_room(current_room)

    pygame.display.update()
    

pygame.quit()
