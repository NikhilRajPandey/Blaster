import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
game_over = False

screen_width = 800
screen_height = 800
game_title = "Blaster"
player_position_x = 400
player_position_y = 600
player_height = 40
player_velocity = 0  # Player will start from rest
fps = 30

pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_velocity = 15
            if event.key == pygame.K_LEFT:
                player_velocity = -15
    screen.fill(white)  # Most important step
    player = pygame.draw.rect(screen,black,[player_position_x,player_position_y,player_height,player_height])

    # Updating the position of the player
    player_position_x = player_position_x + player_velocity
    pygame.display.update()
    clock.tick(fps)
