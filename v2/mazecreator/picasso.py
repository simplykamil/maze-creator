import pygame

import v2.mazecreator.rgbcolours as colours
from v2.mazecreator.Square import Square

import v2.mazecreator.settings as settings


def make_grid(rows: int, width: int):
    """
    Create grid
    :param rows: number of rows
    :param width: width
    :return: grid
    :rtype: list
    """

    grid = list()
    gap = width // rows

    for row in range(rows):
        grid.append(list())
        for col in range(rows):
            grid[row].append(Square(row, col))

    return grid


def draw_grid(win, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, settings.LINE_COLOUR, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, settings.LINE_COLOUR, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows=settings.ROWS, width=settings.WIDTH):
    win.fill(colours.WHITE)

    for row in grid:
        for square in row:
            square.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()
