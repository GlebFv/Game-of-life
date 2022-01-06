import pygame
import pygame
import sys
import os
import random as rand
import runpy
import time
import random
from random import randint as rndi

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen_size = 512, 512
screen = pygame.display.set_mode(screen_size)


def draw_grid():
    # http://www.pygame.org/docs/ref/draw.html#pygame.draw.line
    for x in range(0, 1280, 4):
        pygame.draw.line(screen, pygame.Color('black'),
                         (x, 0), (x, 1280))
    for y in range(0, 1280, 4):
        pygame.draw.line(screen, pygame.Color('black'),
                         (0, y), (1280, y))


class Blok:
    def __init__(self, i, j):
        self.containment = 0
        self.colour = WHITE
        self.i = i
        self.j = j

    def new_creature(self):
        self.containment = 1
        self.colour = BLACK

    def send_containment(self):
        return self.containment

    def die(self):
        self.containment = 0
        self.colour = WHITE

    def draw(self, screen):
        if self.containment == 0:
            pygame.draw.rect(screen, WHITE, (self.i * 4, self.j * 4, self.i * 4 + 4, self.j * 4 + 4))
        else:
            pygame.draw.rect(screen, BLACK, (self.i * 4, self.j * 4, self.i * 4 + 4, self.j * 4 + 4))


class Field:
    def __init__(self):
        self.grid = [[Blok(i, j) for i in range(256)] for j in range(256)]

    def new_turn(self):
        self.new_grid = [[Blok(i, j) for i in range(256)] for j in range(256)]
        for i in range(256):
            for j in range(256):
                if i == 0 and j == 0:
                    count = 0
                    b_neigh = [self.grid[i + 1][j + 1].send_containment(), self.grid[i][j + 1].send_containment(), self.grid[i + 1][j].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
                elif i == 0 and j == 255:
                    count = 0
                    b_neigh = [self.grid[i][j - 1].send_containment(), self.grid[i + 1][j - 1].send_containment(),
                               self.grid[i + 1][j].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
                elif i == 255 and j == 0:
                    count = 0
                    b_neigh = [self.grid[i - 1][j].send_containment(), self.grid[i - 1][j + 1].send_containment(),
                               self.grid[i][j + 1].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
                elif i == 0:
                    count = 0
                    b_neigh = [self.grid[i + 1][j + 1].send_containment(), self.grid[i][j + 1].send_containment(),
                               self.grid[i + 1][j].send_containment(),
                               self.grid[i][j - 1].send_containment(), self.grid[i + 1][j - 1].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
                elif j == 0:
                    count = 0
                    b_neigh = [self.grid[i + 1][j + 1].send_containment(), self.grid[i][j + 1].send_containment(), self.grid[i + 1][j].send_containment(),
                               self.grid[i][j + 1].send_containment(), self.grid[i + 1][j + 1].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
                if i == 255 and j == 255:
                    count = 0
                    b_neigh = [self.grid[i - 1][j - 1].send_containment(), self.grid[i][j - 1].send_containment(),
                               self.grid[i - 1][j].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
                elif i == 255:
                    count = 0
                    b_neigh = [self.grid[i - 1][j - 1].send_containment(), self.grid[i][j - 1].send_containment(),
                               self.grid[i - 1][j].send_containment(), self.grid[i - 1][j + 1].send_containment(), self.grid[i][j + 1].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
                elif j == 255:
                    count = 0
                    b_neigh = [self.grid[i - 1][j - 1].send_containment(), self.grid[i][j - 1].send_containment(), self.grid[i - 1][j].send_containment(),
                               self.grid[i + 1][j - 1].send_containment(), self.grid[i + 1][j].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
                else:
                    count = 0
                    b_neigh = [self.grid[i - 1][j - 1].send_containment(), self.grid[i - 1][j].send_containment(),
                               self.grid[i - 1][j + 1].send_containment(), self.grid[i][j - 1].send_containment(),
                               self.grid[i][j + 1].send_containment(), self.grid[i + 1][j - 1].send_containment(),
                               self.grid[i + 1][j].send_containment(), self.grid[i + 1][j + 1].send_containment()]
                    for e in b_neigh:
                        if e == 1:
                            count += 1
                    if self.grid[i][j].send_containment() == 0 and count == 3:
                        self.new_grid[i][j].new_creature()
                    if self.grid[i][j].send_containment() == 1 and (count == 2 or count == 3):
                        self.new_grid[i][j].new_creature()
        self.grid = self.new_grid[::]

    def send_grid(self):
        return self.grid


def run():
    field = Field()
    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Game of Life')
    screen.fill(pygame.Color('white'))
    running = True
    in_run_grid = field.send_grid()
    for i in in_run_grid:
        for j in i:
            if rndi(1, 5) == 2:
                j.new_creature()
            j.draw(screen)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        in_run_grid = field.send_grid()
        for i in in_run_grid:
            for j in i:
                j.draw(screen)
        draw_grid()
        field.new_turn()
        #clock.tick(1)
        pygame.display.flip()
        clock.tick(1)
    pygame.quit()


run()