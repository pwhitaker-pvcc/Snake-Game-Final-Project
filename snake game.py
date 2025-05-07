import pygame
import sys
import random #imported library

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
body = []
score = 0



#apple
apple_pos = pygame.Rect(120, 120, cell_size, cell_size) 


def spawn_apple():
    # Random x, y on 30x30 grid within border (50 to 720)
    grid_points = list(range(60, 721, cell_size))  # 60, 90, ..., 720
    x = random.choice(grid_points)
    y = random.choice(grid_points)
    return pygame.Rect(x, y, cell_size, cell_size)


def handle_apple_collision(player_pos, apple_pos, body, score, old_head_pos):
    # Check if head collides with apple
    if player_pos.colliderect(apple_pos):
        # Respawn apple
        apple_pos = spawn_apple()
        # Grow body by one 30x30 green segment
        body.append(pygame.Rect(old_head_pos))
        # Increment score
        score += 1
    return apple_pos, score

# game loop
running = True
while running:
    pygame.time.delay(90)  # slows down the loop
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
                
             
    # Save current head position for body
    old_head_pos = pygame.Rect(player_pos)  # Copy head's position

    #Player Movement snake head
    player_pos.x += direction[0] * cell_size
    player_pos.y += direction[1] * cell_size

    # Move body: each segment takes the position of the one in front
    if body:  # If body exists
        # Store current body positions
        temp_positions = [pygame.Rect(segment) for segment in body]
        # Update body segments
        body[0] = pygame.Rect(old_head_pos)  # First segment takes head's old position
        for i in range(1, len(body)):  # Update remaining segments
            body[i] = pygame.Rect(temp_positions[i - 1])  # Take previous segment's position

    # Handle apple collision, growth, and score
    apple_pos, score = handle_apple_collision(player_pos, apple_pos, body, score, old_head_pos)
    #collison check: game over if we hit the wall
    if (player_pos.x < 50 or player_pos.x + cell_size > 750 or
        player_pos.y < 50 or player_pos.y + cell_size > 750):
        running = False #stops game after collision

    #player collision
    for segment in body:
        if player_pos.colliderect(segment):
            running = False
    #apple collision
    if player_pos.colliderect(apple_pos):
        apple_pos = spawn_apple()
        body.append(pygame.Rect(old_head_pos)) #Add new green
    #apple collecting
    if player_pos.colliderect(apple_pos):
        apple_pos = spawn_apple()


    #border
    pygame.draw.rect(screen, Black, border_rect, border_thickness) 
    #player square
    pygame.draw.rect(screen, DARK_GREEN, player_pos)
    #apple
    pygame.draw.rect(screen, Red, apple_pos)
    #body snake
    for segment in body:
        pygame.draw.rect(screen, Green, segment)
    # Score display
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, Black)
    screen.blit(score_text, (10, 10))
    #Update display
    pygame.display.update()



#quitting
pygame.quit()
sys.exit()
