import pygame

pygame.init()
screenv = pygame.display.set_mode((960,540)) ## для создания окна без рамки screenv = pygame.display.set_mode((960,540), flags=pygame.NOFRAME))
pygame.display.set_caption('Заголовок дисплея')
x = True
while x == True:
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = False
            pygame.quit()
        
