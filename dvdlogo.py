import pygame

size = 800, 600
pygame.init()
display = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

x, y = 20, 20
side_length = 60
speed_x, speed_y = 3, 7

while True:
    display.fill((128, 128, 128))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if x < 0 or x + side_length > size[0]:
        speed_x *= -1
    if y < 0 or y + side_length > size[1]:
        speed_y *= -1
    x += speed_x
    y += speed_y
    pygame.draw.rect(display, (255, 255, 64), (x, y, side_length, side_length))
    pygame.display.flip()
    clock.tick(60)
