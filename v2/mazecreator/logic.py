import v2.mazecreator.settings as settings


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


def get_clicked_pos(pos, rows=settings.ROWS, width=settings.WIDTH):
    y, x = pos

    row = y // settings.GAP
    col = x // settings.GAP

    return row, col
