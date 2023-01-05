import pygame
from .settings import *

def init_grid(rows, cols, color):
  grid = []
  for i in range(rows):
    grid.append([])
    for _ in range(cols):
      grid[i].append(color)
  return grid

def create_base_grid():
  return init_grid(ROWS, COLS, BG_COLOR)

def draw_grid(win, grid):
  for i, row in enumerate(grid):
    for j, pixel in enumerate(row):
      pygame.draw.rect(win, pixel, (j * PIXEL_SIZE, i * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
  if DRAW_GRID_LINES:
    for i in range(ROWS + 1):
      pygame.draw.line(win, BLACK, (0, i * PIXEL_SIZE), (WIDTH, i * PIXEL_SIZE))
    for j in range(COLS + 1):
      pygame.draw.line(win, BLACK, (j * PIXEL_SIZE, 0), (j * PIXEL_SIZE, HEIGHT - TOOLBAR_HEIGHT))

def draw(win, grid, buttons):
  win.fill(BG_COLOR)
  draw_grid(win, grid)
  for btn in buttons:
    btn.draw(win)
  pygame.display.update()

def get_row_col_from_pos(pos):
  x, y = pos
  row = y // PIXEL_SIZE
  col = x // PIXEL_SIZE
  return row, col

def check_pos_is_in_toolbar(row):
  if row >= ROWS:
    raise IndexError