import pygame

width, height = 600, 800
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
    #pygame.draw.rect(screen, 'white', pygame.Rect(0, 0, width-200, height))
    pygame.draw.rect(screen, 'black', pygame.Rect(0, 0, width, height))
    pygame.draw.rect(screen, 'white', pygame.Rect(width//4, height//8, 2*width//4, height//8))
    pygame.draw.rect(screen, 'white', pygame.Rect(width // 4, 3*height // 8, 2 * width // 4, height // 8))
    pygame.display.update()
    clock.tick(60)
pygame.quit()
