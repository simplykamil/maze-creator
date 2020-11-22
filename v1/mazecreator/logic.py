import pygame

import v1.mazecreator.colours as colours
from v1.mazecreator.Square import Square

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('Maze creator')


def h(p1: tuple, p2: tuple):
    """
    Calculate heuristic value
    From: https://en.wikipedia.org/wiki/Heuristic_(computer_science)
    In human words: approximate
    There are multiple way to calculate an approximate distance, this case uses manhattan distance / taxicab geometry
    https://www.sciencedirect.com/topics/mathematics/manhattan-distance#:~:text=The%20Manhattan%20distance%20between%20two,the%20%E2%80%9Ctaxi%20cab%E2%80%9D%20metric.

    :param p1: point 1
    :param p2: point 2
    :return: Manhattan distance
    :rtype: int
    """

    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


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
            grid[row].append(Square(row, col, gap, rows))

    return grid


def draw_grid(win, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, colours.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, colours.GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(colours.WHITE)

    for row in grid:
        for square in row:
            square.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows

    y, x = pos

    row = y // gap
    col = x // gap

    return row, col
