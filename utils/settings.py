import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

FPS = 360

WIDTH, HEIGHT = 600, 700

ROWS = COLS = 100

TOOLBAR_HEIGHT = HEIGHT - WIDTH

PIXEL_SIZE = WIDTH // ROWS

BG_COLOR = WHITE

BUTTON_Y = HEIGHT - TOOLBAR_HEIGHT/2 - 25

DRAW_GRID_LINES = True

def get_font(size):
  return pygame.font.SysFont("comicsans", size)
