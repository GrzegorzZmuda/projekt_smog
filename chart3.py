import time
import numpy as np
import os

import pygame
from pygame import surfarray
from pygame.locals import *
from numpy import int32

pygame.init()
from chart import chart

gridsize = 50
scale = 8

dff = 0.05  # ile zanieczyszczeń przechodzi na sąsiadującą kratkę
sd = 0.99  # ile zanieczyszczeń pozostaje w cyklu

# źródła
sources = np.zeros((gridsize, gridsize))
sources[25][25] = 100


def convert(temp):
    temp = temp / 35
    if temp > 255 * 255 * 255:
        blue = 255

    elif temp > 255 * 255:
        blue = temp // 255 // 255
    else:
        blue = 0

    if blue > 0:
        blue -= 1
        green = 255

    elif temp > 255:
        green = (temp // 255) % 255

    else:
        green = 0

    if green > 0:
        green -= 1
        red = 255
    else:
        red = temp % 255 % 255

    return (255 - blue, 255 - green, 255 - red)


def show(data):
    screen = pygame.display.set_mode((data.shape[0] * scale, data.shape[1] * scale), 0, 32)
    img = np.zeros((data.shape[0], data.shape[1], 3))
    for x in range(data.shape[0]):
        for y in range(data.shape[1]):
            img[x, y, :] = convert(data[x, y])

    surfarray.blit_array(screen, img.repeat(scale, axis=0).repeat(scale, axis=1))

    pygame.display.flip()

    pygame.display.set_caption("test")
    """
    while 1:
        e = pygame.event.wait()
        if e.type == MOUSEBUTTONDOWN: break
        elif e.type == QUIT:
            pygame.quit()
            raise SystemExit()
    """

    time.sleep(0.1)


grid = np.zeros((gridsize, gridsize))

for abdas in range(200):
    gridn = np.zeros((gridsize, gridsize))

    grid = grid

    # add pollution from sources to new grid
    gridn += sources

    # spread old pollution and...
    # reduce pollution from old grid because it disapears over time

    for x in range(1, gridsize - 1):
        for y in range(1, gridsize - 1):  # sorces + remaining pollution from previous cycle (spreaded pollution)
            gridn[x][y] = gridn[x][y] + sd * (
                        dff * (grid[x - 1][y] + grid[x + 1][y] + grid[x][y - 1] + grid[x][y + 1]) + (1 - dff) * grid[x][
                    y])

    # chart(grid, gridsize, gridsize)
    grid = gridn

    show(grid)

pygame.quit()