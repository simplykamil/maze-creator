import pygame

import v2.mazecreator.logic as logic
import v2.mazecreator.picasso as picasso
import v2.mazecreator.settings as settings
from v2.mazecreator.SquareState import SquareState

if __name__ == '__main__':
    WINDOW = pygame.display.set_mode((settings.WIDTH, settings.WIDTH))
    GRID = picasso.make_grid(settings.ROWS, settings.WIDTH)
    pygame.display.set_caption(settings.WINDOW_TITLE)

    start_pos = None
    end_pos = None

    [print(x) for x in GRID]

    run = True
    while run:
        picasso.draw(WINDOW, GRID)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
            elif pygame.mouse.get_pressed()[0]:
                row, col = logic.get_clicked_pos(pygame.mouse.get_pos())
                square = GRID[row][col]

                if not start_pos and square != end_pos and square.state != SquareState.WALL:
                    start_pos = square
                    start_pos.change_state(SquareState.START)
                elif not end_pos and square != start_pos and square.state != SquareState.WALL:
                    end_pos = square
                    end_pos.change_state(SquareState.END)
                elif square not in (start_pos, end_pos):
                    square.change_state(SquareState.WALL)

            elif pygame.mouse.get_pressed()[2]:
                row, col = logic.get_clicked_pos(pygame.mouse.get_pos())
                square = GRID[row][col]
                square.reset()

                if square == start_pos:
                    start_pos = None
                elif square == end_pos:
                    end_pos = None

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not start_pos:
                    print('Implement search you dumbo')

    pygame.quit()
    # while True:
    #     print(len(GRID))
    #
    # start = None
    # end = None
    #
    # run = True
    # while run:
    #     draw(win, grid, ROWS, width)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #
    #         if pygame.mouse.get_pressed()[0]:  # LEFT
    #             pos = pygame.mouse.get_pos()
    #             row, col = get_clicked_pos(pos, ROWS, width)
    #             spot = grid[row][col]
    #             if not start and spot != end:
    #                 start = spot
    #                 start.make_start()
    #
    #             elif not end and spot != start:
    #                 end = spot
    #                 end.make_end()
    #
    #             elif spot != end and spot != start:
    #                 spot.make_barrier()
    #
    #         elif pygame.mouse.get_pressed()[2]:  # RIGHT
    #             pos = pygame.mouse.get_pos()
    #             row, col = get_clicked_pos(pos, ROWS, width)
    #             spot = grid[row][col]
    #             spot.reset()
    #             if spot == start:
    #                 start = None
    #             elif spot == end:
    #                 end = None
    #
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_SPACE and start and end:
    #                 for row in grid:
    #                     for spot in row:
    #                         spot.update_neighbors(grid)
    #
    #                 algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
    #
    #             if event.key == pygame.K_c:
    #                 start = None
    #                 end = None
    #                 grid = make_grid(ROWS, width)
    #
    # pygame.quit()
