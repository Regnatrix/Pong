'''Sandra Dögg Kristmundsdóttir
30.01.2018'''
import pygame
from pygame.locals import *
from random import randint

yes = True
maybe = True
while True:
    name1 = input("Nafn spilara 1: ")
    name2 = input("Nafn spilari 2: ")

    if len(name1) > 10 or len(name2) > 10:
        print("10 eða færri stafi takk")

    else:
        break

pygame.init()
pygame.font.init()

window_size = window_width, window_height = 960, 770
window = pygame.display.set_mode(window_size)

pygame.display.set_caption('Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
litur = [255, 255, 255]
litur2 = [255, 255, 255]
rainbow = (randint(0,255), randint(0,255), randint(0,255))
myfont = pygame.font.SysFont('Comic Sans MS', 30)

ballXList = [-2, 2]
ballYList = [-2, -1, 1, 2]

player1_x_position = 60
player1_y_position = 330

player2_x_position = 890
player2_y_position = 330

player1_y_velocity = 0
player2_y_velocity = 0

ball_xpos = 480
ball_ypos = 360

ball_xvel = ballXList[randint(0,1)]
ball_yvel = ballYList[randint(0,3)]

score1 = 0
score2 = 0
hradi = 1

window.fill(BLACK)

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player2_y_velocity = -7
            elif event.key == pygame.K_DOWN:
                player2_y_velocity = 7

            if event.key == pygame.K_w:
                player1_y_velocity = -7
            elif event.key == pygame.K_s:
                player1_y_velocity = 7

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_UP:
                player2_y_velocity = 0
            elif event.key == pygame.K_DOWN:
                player2_y_velocity = 0

            if event.key == pygame.K_w:
                player1_y_velocity = 0
            elif event.key == pygame.K_s:
                player1_y_velocity = 0

    rainbow = (randint(0, 255), randint(0, 255), randint(0, 255))
    ball_xpos += ball_xvel
    ball_ypos += ball_yvel

    player1_y_position += player1_y_velocity

    player2_y_position += player2_y_velocity

    window.fill(BLACK)
    # Objects
    ball = pygame.draw.circle(window, rainbow, (ball_xpos, ball_ypos), 10)
    rect1 = pygame.draw.rect(window, litur, pygame.Rect(player1_x_position, player1_y_position, 15, 60))
    rect2 = pygame.draw.rect(window, litur2, pygame.Rect(player2_x_position, player2_y_position, 15, 60))
    # Lines
    pygame.draw.line(window, WHITE, (0, 70), (1000, 70))
    pygame.draw.line(window, RED, (60+15, player1_y_position + 60), (60+15, player1_y_position))
    pygame.draw.line(window, RED, (890, player2_y_position + 60), (890, player2_y_position))
    # Text
    name1Score = myfont.render(str(name1), True, (WHITE))
    window.blit(name1Score, (10, -5))
    player1Score = myfont.render(str(score1), True, (WHITE))
    window.blit(player1Score, (25, 25))

    name1Score = myfont.render(str(name2), True, (WHITE))
    window.blit(name1Score, (880, -5))
    player2Score = myfont.render(str(score2), True, (WHITE))
    window.blit(player2Score, (900, 25))

    hraditexti = myfont.render("Hraði: "+ str(hradi), True, (WHITE))
    window.blit(hraditexti, (435, -5))

    # Athugar hvort að bolti hittir h spilara og skiptir um lit
    if player1_x_position < ball_xpos < player1_x_position + 25 and player1_y_position < ball_ypos < player1_y_position + 60:
        print("hægri")
        litur = [randint(0, 255), randint(0, 255), randint(0, 255)]
        ball_xvel *= -1
        ball_xvel += 2
        hradi += 1

    # Athugar hvort að bolti hittir v spilara og skiptir um lit
    if player2_x_position - 5 < ball_xpos < player2_x_position + 15 and player2_y_position < ball_ypos < player2_y_position + 60:
        print("vinstri")
        litur2 = [randint(0, 255), randint(0, 255), randint(0, 255)]
        ball_xvel *= -1
        ball_xvel -= 2
        hradi += 1

    # Ef y position er
    if ball_ypos > 760 or ball_ypos < 80:
        ball_yvel *= -1

    if ball_xpos > 960:
        ball_xpos = 480
        ball_ypos = 360
        ball_xvel = ballXList[randint(0,1)]
        ball_yvel = randint(-20, 20)
        score1 +=1
        hradi = 1

    if ball_xpos < 0:
        ball_xpos = 480
        ball_ypos = 360
        ball_xvel = ballXList[randint(0,1)]
        ball_yvel = ballYList[randint(0,3)]
        score2 += 1
        hradi = 1

    if player1_y_position > 708 or player1_y_position < 75:
        if player1_y_position > 708:
            player1_y_position = 710
        if player1_y_position < 75:
            player1_y_position = 70
        player1_y_velocity = 0

    if player2_y_position > 708 or player2_y_position < 75:
        if player2_y_position > 708:
            player2_y_position = 710
        if player2_y_position < 75:
            player2_y_position = 70
        player2_y_velocity = 0

    if score1 > 9:
        name1Score = myfont.render(str(name1), True, (GREEN))
        window.blit(name1Score, (10, -5))

    if score2 > 9:
        name1Score = myfont.render(str(name2), True, (GREEN))
        window.blit(name1Score, (880, -5))

    if score1 > 19:
        player1Score = myfont.render(str(score1), True, (BLUE))
        window.blit(player1Score, (25, 25))

    if score2 > 19:
        player2Score = myfont.render(str(score2), True, (BLUE))
        window.blit(player2Score, (900, 25))

    pygame.display.update()
    clock.tick(60)
pygame.quit()