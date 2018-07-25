#!/usr/bin/env python3
#from sys import exit
import sys, pygame, pygame.mixer
from pygame.locals import *
import pygame
from pygame.locals import *
from sys import exit
import random

cory_health = 3
enemy_health = 1
laser_duration = 1
laser_cooldown = .5

RED =(255, 0, 0)
BLACK=(0, 0, 0)
GREEN=(0,255,0)

WIDTH = 800
HEIGHT = 750
FPS = 50

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()



bkgrnd_img = "cory_in_the_house.png" #change name and picture
mouse_image_filename = "Good_Cory.png"
projectile_thing = "knife.png"
clock = pygame.time.Clock()
pygame.init()
pygame.mixer.init()
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom= HEIGHT - 10
        self.speedx = 0
    def update(self):
        self.rect.x += self.speedx



class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)

    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

all_sprites = pygame.sprite.Group()

screen = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
background = pygame.image.load(bkgrnd_img).convert()
pygame.display.set_caption("i dont think ur ready")
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
#pygamedisplays=pygame.display.set_mode(display_width,display_height)
clock = pygame.time.Clock()

speed = 800

############test area#############
WIDTH = 800
HEIGHT= 750



#pg.init()
#RED = pg.Color('red')
#screen = pg.display.set_mode((800, 750))
#width, height = screen.get_size()
#clock = pg.time.Clock()
#done = False

#sides = ['top', 'bottom', 'left', 'right']
#weights = [width, width, height, height]


##################################
screen.blit(background, (0,0))
p = player()

for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
while True:
    clock.tick(FPS)
    change_y = 0
    for event in pygame.event.get(): #goes through stored pygame events(?)
        if event.type == pygame.QUIT: #checks if user presses x button
            exit()

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        break
############test##############
#    side = random.choices(sides, weights)[0]

#    if side == 'top':
#            y = 0
#            x = random.randrange(width-4)
#    elif side == 'bottom':
#            y = height-400
#            x = random.randrange(width-4)
#    elif side == 'left':
#            x = 0
#            y = random.randrange(height-4)
#    elif side == 'right':
#            x = width-400
#            y = random.randrange(height-4)
#
#            pg.draw.rect(screen, RED, (x, y, 40, 40))
#            pg.display.flip()
#



    screen.fill(BLACK)
    all_sprites.draw(screen)

#mouse follow code
    x, y = pygame.mouse.get_pos()
    x -= mouse_cursor.get_width()/2
    y -= mouse_cursor.get_height()/2
    screen.blit(mouse_cursor, (x, y))

    if(event.type == pygame.MOUSEBUTTONDOWN):
        #print("The mouse was clicked")
        x, y = pygame.mouse.get_pos()
        x -= mouse_cursor.get_width()/2
        y -= mouse_cursor.get_height()/2
        screen.blit(mouse_cursor, (x, y))
        screen.blit(pygame.image.load('knife.png').convert_alpha(), (x, y-150))

    clock.tick(420)

    pygame.display.update()
