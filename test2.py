import pygame

pygame.init()
screenv = pygame.display.set_mode((960,540))
x = True
while x == True:
    pygame.display.update()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
          vel_y = vel_y - 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = False
            pygame.quit()
        
