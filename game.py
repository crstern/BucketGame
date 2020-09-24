from utility import *
from sys import exit



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    draw()
    pygame.display.update()
    clock.tick(frame_rate)
