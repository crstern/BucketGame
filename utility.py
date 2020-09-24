from variables import *
from bucket import *
from plum import *
from random import randint

bucket_pos_x = 380
bucket_pos_y = 800

plum_pos_x = 100
plum_pos_y = 100

plum_list = []
bucket = Bucket()


def draw():
    screen.blit(background_surface, (0,0))
    screen.blit(bucket_surface, (bucket_pos_x, bucket_pos_y))

    spawn_plums()

    move_plum()

def spawn_plums():
    plum_pos_x = randint(100, 680)
    screen.blit(plum_surface, (plum_pos_x, plum_pos_y))



def move_plum():
    global plum_pos_y
    plum_pos_y += 1

    if plum_pos_y > 1200:
        plum_pos_y = 0


