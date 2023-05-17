import pygame
from settings import *
from random import randint

class MagicPlayer:
    def __init__(self,animation_player):
        self.animation_player = animation_player

    def heal(self,player,strength,cost,groups):
        if player.energy >= cost:
            player.health += strength
            player.energy -= cost
            if player.health >= player.stats['health']:
                player.health = player.stats['health']
            self.animation_player.create_particles("aura",player.rect.center,groups)
            self.animation_player.create_particles("heal",player.rect.center + pygame.math.Vector2(0,-50),groups)
    
    def flame(self,player,cost,groups):
        if player.energy >= cost:
            player.energy -= cost
            

            if player.status.split("_")[0] == "right": direction = pygame.math.Vector2(1,0)
            elif player.status.split("_")[0] == "left": direction = pygame.math.Vector2(-1,0)
            elif player.status.split("_")[0] == "down": direction = pygame.math.Vector2(0,1)
            else: direction = pygame.math.Vector2(0,-1)

            for i in range(1,6):
                if direction.x:
                    offset_x = (direction.x * i) * TILESIZE
                    x = player.rect.centerx + offset_x
                    y = player.rect.centery
                    self.animation_player.create_particles("flame",(x,y),groups)
                else:
                    offset_y = (direction.y * i) * TILESIZE
                    x = player.rect.centerx
                    y = player.rect.centery + offset_y
                    self.animation_player.create_particles("flame",(x,y),groups)

    def water(self,player,cost,groups):
        if player.energy >= cost:
            player.energy -= cost

            if player.status.split("_")[0] == "right": direction = pygame.math.Vector2(1,0)
            elif player.status.split("_")[0] == "left": direction = pygame.math.Vector2(-1,0)
            elif player.status.split("_")[0] == "down": direction = pygame.math.Vector2(0,1)
            else: direction = pygame.math.Vector2(0,-1)

            if direction.x:
                offset_x = (direction.x * 1) * TILESIZE

                self.animation_player.create_particles("water",(player.rect.centerx + offset_x,player.rect.centery),groups)
                self.animation_player.create_particles("water",(player.rect.centerx + offset_x,player.rect.centery + offset_x),groups)
                self.animation_player.create_particles("water",(player.rect.centerx + offset_x,player.rect.centery - offset_x),groups)

            else:
                offset_y = (direction.y * 1) * TILESIZE

                self.animation_player.create_particles("water",(player.rect.centerx,player.rect.centery + offset_y),groups)
                self.animation_player.create_particles("water",(player.rect.centerx + offset_y,player.rect.centery + offset_y),groups)
                self.animation_player.create_particles("water",(player.rect.centerx - offset_y,player.rect.centery + offset_y),groups)