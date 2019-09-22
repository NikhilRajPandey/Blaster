import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
game_over = False

screen_width = 800
screen_height = 800
game_title = "Blaster"

player_position_x = 400
player_position_y = 600
height = 40  # One Box Height and width
player_velocity = 0  # Player will start from rest
fps = 25

enemy_position_x_list = [random.randint(50,750),random.randint(50,750),random.randint(50,750)]
enemy_position_y = 20
enemy_velocity = 20
enemy_list = []

missile_height = 10
missile_position_list = []
missile_velocity = 20
pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

def fire():
    for missile_position_x,missile_position_y,is_missile_launched in missile_position_list:
        if is_missile_launched:
            pygame.draw.rect(screen,red,[missile_position_x,missile_position_y,missile_height,missile_height])

def plot_enemy():
    for enemy_x,enemy_y in enemy_list:
        pygame.draw.rect(screen,black,[enemy_x,enemy_y,height,height])

while not game_over:
    screen.fill(white)  # Most important step

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_velocity = 20
            if event.key == pygame.K_LEFT:
                player_velocity = -20
            if event.key == pygame.K_RCTRL:
                missile_position_list.append([player_position_x,player_position_y,True])
                fire()

    # Declaring Enemy and player
    player = pygame.draw.rect(screen,black,[player_position_x,player_position_y,height,height])
    enemy_list.append([enemy_position_x_list[0],enemy_position_y])
    enemy_list.append([enemy_position_x_list[1],enemy_position_y])
    enemy_list.append([enemy_position_x_list[2], enemy_position_y])

    if len(enemy_list) >= 12:  # If it was not written then enemy will become so long
        del enemy_list[0]
        del enemy_list[0]
        del enemy_list[0]

    plot_enemy()
    fire()

    # Updating the position of the player,enemy and Missile
    player_position_x = player_position_x + player_velocity
    enemy_position_y = enemy_position_y + enemy_velocity
    if is_missile_launched:
        for missile_position_y,missile_position_x in missile_position_list:
            missile_position_y = missile_position_y - missile_velocity
            if missile_position_y < 0:  # Means The missile is collide
                is_missile_launched = False

    # Taking Enemy Position 0 when it collides
    if enemy_position_y >= screen_height:
        enemy_position_y = 0
        enemy_position_x_list = [random.randint(50,750),random.randint(50,750),random.randint(50,750)]

    pygame.display.update()
    clock.tick(fps)
