import pygame

pygame.init()

plum_surface = pygame.image.load('assets/pruna.png')
plum_surface = pygame.transform.scale(plum_surface, (100, 100))

bucket_surface = pygame.image.load('assets/galeata1.png')
bucket_surface = pygame.transform.scale(bucket_surface, (100, 100))


background_surface = pygame.image.load('assets/background.jpg')
background_surface = pygame.transform.scale(background_surface, (720, 1280))

frame_rate = 90
screen_size = (720, 1280)



screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


clock.tick(frame_rate)


