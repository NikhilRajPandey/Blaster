import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
game_over = False

screen_width = 800
screen_height = 800
game_title = "Blaster"

player_position_x = 400
player_position_y = 600
height = 40  # One Box Height and width
player_velocity = 0  # Player will start from rest
fps = 30

enemy_position_x_list = [random.randint(50,750),random.randint(50,750)]
enemy_position_y = 20
enemy_velocity = 20
enemy_list = []

pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

def plot_enemy():
    for enemy_x,enemy_y in enemy_list:
        pygame.draw.rect(screen,black,[enemy_x,enemy_y,height,height])

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_velocity = 20
            if event.key == pygame.K_LEFT:
                player_velocity = -20

    screen.fill(white)  # Most important step

    # Declaring Enemy and player
    player = pygame.draw.rect(screen,black,[player_position_x,player_position_y,height,height])
    enemy_list.append([enemy_position_x_list[0],enemy_position_y])
    enemy_list.append([enemy_position_x_list[1],enemy_position_y])

    # If it was not written then enemy will become so long
    if len(enemy_list) >= 8:
        del enemy_list[0]
        del enemy_list[0]

    # Updating the position of the player and enemy
    plot_enemy()
    player_position_x = player_position_x + player_velocity
    enemy_position_y = enemy_position_y + enemy_velocity

    # Taking Enemy Position 0 when it collides
    if enemy_position_y >= screen_height:
        enemy_position_y = 0
        enemy_position_x_list = [random.randint(50,750),random.randint(50,750)]

    pygame.display.update()
    clock.tick(fps)
