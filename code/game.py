#!/usr/bin/python
# -*- coding: utf-8 -*-

class game:

    def __init__(self):
        self.window: Surface = None

    def run(self):
        pass

import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(600, 480))
print('Setup End')

print('Loop Start')


while True:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
        print('Quiting...')
        pygame.quit()
        quit()