# Background : Photo by Francesco Ungaro from Pexels
# Music : https://www.youtube.com/watch?v=QglaLzo_aPk&list=PLKUA473MWUv03VnZLb98iAxdbCLxl0qG3

import pygame
import random

pygame.init()
pygame.mixer.init()


screen_width = 800
screen_height = 800
game_title = "Blaster"

background = pygame.image.load('images/background.jpg')
music = pygame.mixer.music.load('sounds/song.mp3')
pygame.mixer.music.play(100)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,128,0)

game_over = False
game_quit = False
game_started = False
game_over_reason = ""

pygame.display.set_caption(game_title)
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

heading_style = pygame.font.SysFont(None,200)
sub_heading_style = pygame.font.SysFont(None, 85)
fps = 60

player_position_x = 400
player_position_y = 600
height = 40  # One Box Height and width
player_velocity = 0  # Player will start from rest

enemy_position_x_list = [random.randint(50,750),random.randint(50,750),random.randint(50,750)]
enemy_height = 60
enemy_position_y_list = [5,5,5]
enemy_velocity = 10
enemy_list = []

missile_height = 10
missile_position_list = []
missile_velocity = 12


def fire():
    for missile_position_x,missile_position_y,is_missile_launched in missile_position_list:
        if is_missile_launched:
            pygame.draw.rect(screen,red,[missile_position_x,missile_position_y,missile_height,missile_height])

def plot_enemy():
    for enemy_x,enemy_y in enemy_list:
        pygame.draw.rect(screen,green,[enemy_x,enemy_y,enemy_height,enemy_height])

while not game_quit:
    print(game_over)
    if not game_started:
        screen.blit(background, [0, 0])
        # Intro
        heading = heading_style.render("Blaster",True,white)
        sub_heading = sub_heading_style.render("Enter to play this game", True, white)
        screen.blit(heading,[155,150])
        screen.blit(sub_heading,[70,300])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_started = True

    elif game_over:
        screen.blit(background, [0, 0])
        heading = heading_style.render("Game Over",True,white)
        sub_heading = sub_heading_style.render(game_over_reason,True,white)
        sub_heading_2 = sub_heading_style.render("Enter to play again", True, green)
        pygame.mixer.music.stop()
        screen.blit(heading,[10,50])
        screen.blit(sub_heading,[25,200])
        screen.blit(sub_heading_2, [120, 400])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Resetting all the variables
                    pygame.mixer.music.play(100)
                    player_position_x = 400
                    player_position_y = 600
                    player_velocity = 0

                    enemy_position_x_list = [random.randint(50, 750), random.randint(50, 750), random.randint(50, 750)]
                    enemy_position_y_list = [5, 5, 5]
                    enemy_velocity = 10
                    enemy_list = []

                    missile_height = 10
                    missile_position_list = []
                    game_over = False
    else:
        screen.blit(background, [0, 0])
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
        enemy_list.append([enemy_position_x_list[0],enemy_position_y_list[0]])
        enemy_list.append([enemy_position_x_list[1],enemy_position_y_list[1]])
        enemy_list.append([enemy_position_x_list[2], enemy_position_y_list[2]])

        if len(enemy_list) >= 6:  # If it was not written then enemy will become so long
            del enemy_list[0]
            del enemy_list[0]
            del enemy_list[0]

        plot_enemy()
        fire()

        # Updating the position of the player,enemy and Missile
        player_position_x = player_position_x + player_velocity

        for enemy_position_y in enemy_position_y_list:
            current_position_index = enemy_position_y_list.index(enemy_position_y)
            enemy_position_y_list[current_position_index] = enemy_position_y_list[current_position_index] + enemy_velocity

        count_missile = 0  # In this for loop the enumerate function is not working so i used this

        for missile_position_y,missile_position_x,launched in missile_position_list:
            if launched:
                missile_position_list[count_missile][1] = missile_position_list[count_missile][1] - missile_velocity
            if missile_position_list[count_missile][1] < 0:  # Means The missile is collide
                del missile_position_list[count_missile]
            count_missile = count_missile + 1

        # Checking the player is out or not
        if player_position_x < 0 or player_position_x > (screen_width-25):
            game_over_reason = "You had collide with walls "
            game_over = True

        for enemy_x, enemy_y in enemy_list:
            if abs(enemy_x - player_position_x) < 15 and abs(enemy_y - player_position_y) < 15:
                game_over_reason = "You had collide with Enemy"
                game_over = True

        no_of_kills = 0  # I will use this later

        # Destroying Enemy when missile hit them
        for missile_count,(missile_position_x, missile_position_y, launched) in enumerate(missile_position_list):
            deleted_missile = False
            if launched:
                for enemy_count,(enemy_x, enemy_y) in enumerate(enemy_list):
                    if abs(enemy_x - missile_position_x) < 30 and abs(enemy_y - missile_position_y) < 30 and not deleted_missile:  # Means Missile hit the enemy
                        curent_enemy_index = enemy_list.index([enemy_x, enemy_y])
                        del enemy_list[curent_enemy_index]
                        del missile_position_list[missile_position_list.index([missile_position_x,missile_position_y,launched])]
                        deleted_missile = True
                        enemy_position_x_list[curent_enemy_index] = random.randint(50,750)
                        enemy_position_y_list[curent_enemy_index] = 20

        # Taking Enemy Position 0 when it collides
        for enemy_position_y in enemy_position_y_list:
            if int(enemy_position_y) >= screen_height:
                index_of_current_position = enemy_position_y_list.index(enemy_position_y)
                enemy_position_y_list[index_of_current_position] = 20
                enemy_position_x_list[index_of_current_position] = random.randint(5,750)

        enemy_list = []

        pygame.display.update()
        clock.tick(fps)
        
