import pygame

pygame.init()
screenv = pygame.display.set_mode((960,540)) ## для создания окна без рамки screenv = pygame.display.set_mode((960,540), flags=pygame.NOFRAME))
pygame.display.set_caption('Заголовок дисплея')
iconv = pygame.image.load('C:\\Users\\AttekPC\\Desktop\\game\\imageforstart\\rupee_icon.png')
pygame.display.set_icon(iconv)
color1 = (180, 150, 250)
square1 = pygame.Surface((175,50))
square1.fill((192, 192, 192))
font1 = pygame.font.Font(None,40)
text1 = font1.render('Надпись', False,(70, 70, 70))
object1 = pygame.image.load('C:\\Users\\AttekPC\\Desktop\\game\\imageforstart\\rupee_icon.png')
x = True
while x == True:
    pygame.display.update()
    screenv.fill(color1)
    screenv.blit(square1, (50,50))
    pygame.draw.rect(screenv,(192, 192, 192),(50,150,175,50)) ## pygame.draw.форма(rect-прямоугольник)(где-экран,(код цвета), (х(растояние от вертикальной границы экрана слева), (х(растояние от горизонтальной границы экрана сверху), х(размер вертикально),х(размер горизонтально))))
    #screenv.blit(text1,(50,50))
    square1.blit(text1,(0,0)) ## то же что в предыдущей строке, но там на экране, а тут на квадрате
    screenv.blit(object1,(250,10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            x = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color1 = (255, 250, 205)
        
