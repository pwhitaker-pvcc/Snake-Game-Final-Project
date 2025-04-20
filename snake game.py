import pygame
import sys

pygame.init()


#Window
Width = 800
Height = 800
cell_size = 30
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Snake Game")

#color
Red = (255, 0, 0)
Green = (0, 255, 0)
DARK_GREEN = (0,150,0)
Black = (0,0,0) 
White = (255, 255, 255)

#Square Border
border_rect = pygame.Rect(50,50, 700, 700)
border_thickness = 8
#player Pos Snake
player_pos = pygame.Rect(90, 90, 30, 30) #aligned with a 30x30 grid
direction = (1, 0)



# game loop
running = True
while running:
    pygame.time.delay(80)  # slows down the loop
    screen.fill(White)     # clear the screen

    # event handling; in this example, quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            #Player movement keys
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and direction != (0, 1):
                direction = (0, -1)  # Move up
            elif event.key == pygame.K_s and direction != (0, -1):
                direction = (0, 1)   # Move down
            elif event.key == pygame.K_a and direction != (1, 0):
                direction = (-1, 0)  # Move left
            elif event.key == pygame.K_d and direction != (-1, 0):
                direction = (1, 0)   # Move right


                
    #Player Movement snake head
    player_pos.x += direction[0] * cell_size
    player_pos.y += direction[1] * cell_size

    #collison check: game over if we hit the wall
    if (player_pos.x < 50 or player_pos.x + cell_size > 750 or
        player_pos.y < 50 or player_pos.y + cell_size > 750):
        running = False #stops game after collision


    #border
    pygame.draw.rect(screen, Black, border_rect, border_thickness) 
    #player square
    pygame.draw.rect(screen, DARK_GREEN, player_pos)
       
    #Update display
    pygame.display.update()



#quitting
pygame.quit()
sys.exit()
