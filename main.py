from utils import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drawing App")

run = True
clock = pygame.time.Clock()
grid = create_base_grid()
drawing_color = BLACK

buttons = [
  Button(10, BUTTON_Y, 50, 50, BLACK),
  Button(70, BUTTON_Y, 50, 50, RED),
  Button(130, BUTTON_Y, 50, 50, GREEN),
  Button(190, BUTTON_Y, 50, 50, BLUE),
  Button(250, BUTTON_Y, 50, 50, WHITE, "Erase", BLACK),
  Button(310, BUTTON_Y, 50, 50, WHITE, "Clear", BLACK),
]

while run:
  # run loop with FPS speed and not faster than that
  clock.tick(FPS)

  for event in pygame.event.get():
    # Click 'x' of an app window
    if event.type == pygame.QUIT:
      run = False
    
    if pygame.mouse.get_pressed()[0]:
      pos = pygame.mouse.get_pos()
      row, col = get_row_col_from_pos(pos)
      try:
        check_pos_is_in_toolbar(row)
        grid[row][col] = drawing_color
      except IndexError:
        for btn in buttons:
          if not btn.is_clicked(pos):
            continue

          if btn.text == "Clear":
            grid = create_base_grid()
            drawing_color = BLACK
            break

          drawing_color = btn.color
          break

  draw(WIN, grid, buttons)

pygame.quit()