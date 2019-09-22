import pygame
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,128,0)
game_over = False
game_over_reason = ""

screen_width = 800
screen_height = 800
game_title = "Blaster"

player_position_x = 400
player_position_y = 600
height = 40  # One Box Height and width
player_velocity = 0  # Player will start from rest
fps = 60

enemy_position_x_list = [random.randint(50,750),random.randint(50,750),random.randint(50,750)]
enemy_height = 60
enemy_position_y = 20
enemy_velocity = 10
enemy_list = []

missile_height = 10
missile_position_list = []
missile_velocity = 12
pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

def fire():
    for missile_position_x,missile_position_y,is_missile_launched in missile_position_list:
        if is_missile_launched:
            pygame.draw.rect(screen,red,[missile_position_x,missile_position_y,missile_height,missile_height])

def plot_enemy():
    for enemy_x,enemy_y in enemy_list:
        pygame.draw.rect(screen,green,[enemy_x,enemy_y,enemy_height,enemy_height])

while not game_over:
    screen.fill(white)  # Most important step

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_velocity = 10
            if event.key == pygame.K_LEFT:
                player_velocity = -10
            if event.key == pygame.K_RCTRL:
                missile_position_list.append([player_position_x,player_position_y,True])
                fire()

    # Declaring Enemy and player
    player = pygame.draw.rect(screen,black,[player_position_x,player_position_y,height,height])
    enemy_list.append([enemy_position_x_list[0],enemy_position_y])
    enemy_list.append([enemy_position_x_list[1],enemy_position_y])
    enemy_list.append([enemy_position_x_list[2], enemy_position_y])

    if len(enemy_list) >= 6:  # If it was not written then enemy will become so long
        del enemy_list[0]
        del enemy_list[0]
        del enemy_list[0]

    plot_enemy()
    fire()

    # Updating the position of the player,enemy and Missile
    player_position_x = player_position_x + player_velocity
    enemy_position_y = enemy_position_y + enemy_velocity

    count_missile = 0  # In this for loop the enumerate function is not working so i used this

    for missile_position_y,missile_position_x,launched in missile_position_list:
        if launched:
            missile_position_list[count_missile][1] = missile_position_list[count_missile][1] - missile_velocity
        if missile_position_list[count_missile][1] < 0:  # Means The missile is collide
            del missile_position_list[count_missile]
        count_missile = count_missile + 1

    # Checking the player is out or not
    if player_position_x < 0 or player_position_x > (screen_width-25):
        game_over_reason = "You are collide with walls "
        game_over = True

    for enemy_x, enemy_y in enemy_list:
        if abs(enemy_x - player_position_x) < 15 and abs(enemy_y - player_position_y) < 15:
            game_over_reason = "You are collide with Enemy"
            game_over = True

    no_of_kills = 0
    # Destroying Enemy when missile hit them
    for missile_count,(missile_position_x, missile_position_y, launched) in enumerate(missile_position_list):
        if launched:
            for enemy_count,(enemy_x, enemy_y) in enumerate(enemy_list):
                if abs(enemy_x - missile_position_x) < 30 and abs(enemy_y - missile_position_y) < 30:  # Means Missile hit the enemy
                    print("hello world")
                    curent_enemy_index = enemy_list.index([enemy_x, enemy_y])
                    del enemy_list[curent_enemy_index]
                    del missile_position_list[missile_position_list.index([missile_position_x,missile_position_y,launched])]
                    enemy_position_x_list[curent_enemy_index] = random.randint(50,750)
                    enemy_position_y = 0

    # Taking Enemy Position 0 when it collides
    if enemy_position_y >= screen_height:
        enemy_position_y = 0
        enemy_position_x_list = [random.randint(50,750),random.randint(50,750),random.randint(50,750)]

    pygame.display.update()
    clock.tick(fps)
