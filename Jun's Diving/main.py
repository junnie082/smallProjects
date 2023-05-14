import pygame
import random
import math

gameNotOver = 1
score = 0

pygame.init()
pygame.display.set_caption("Jun's Diving")
icon = pygame.image.load('diver.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode( (1200, 600) )

# Background
background = pygame.image.load('sea.png')

# Game Over
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Score
score_font = pygame.font.Font('freesansbold.ttf', 32)

# Oxygen tank
oxygenTankImg = pygame.image.load('oxygen-tank.png')

# Diver
diverImg = pygame.image.load('diver.png')
diverX = 50
diverY = 300
diverY_change = 0

# Rock
rockImg = pygame.image.load('rocks.png')
rockX = 1200
rockY = random.randint(400, 536)
rockX_change = 2

# Big Shark
bigSharkImg = pygame.image.load('bigshark.png')
bigSharkX = 1200
bigSharkY = random.randint(0, 400)
bigSharkX_change = 3

# Water Pressure
waterPressure = 0
# totalBuoyancy
totalBuoyancy = 0
# speed up ratio
speedUp = 0.001

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(over_text, (400, 250))

def score_text(score):
    score_text = score_font.render("Score: " + str(score), True, (255, 0, 0))
    screen.blit(score_text, (10, 10))

def distance(diverX, diverY, bigSharkX, bigSharkY):
    distance = math.sqrt(math.pow(diverX - bigSharkX, 2) + math.pow(diverY - bigSharkY, 2))

    if distance < 32:
        return True
    else:
        return False


def diver(X, Y):
    screen.blit(diverImg, (X, Y) )

def rock(X, Y):
    screen.blit(rockImg, (X, Y) )

def bigShark(X, Y):
    screen.blit(bigSharkImg, (X, Y))


time = 0
running = True
while running:
    time += 1
    # RGB - Red, Green Blue
    screen.fill( (100, 150, 200) )
    screen.blit(background, (0, 0))

    if time % 100 == 0 and gameNotOver:
        score += 1
    score_text(score)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether it's right or left
        if event.type == pygame.KEYDOWN:
            # breath
            if event.key == pygame.K_UP:
                diverY_change -= 2
            if event.key == pygame.K_DOWN:
                diverY_change += 2
            # inflator / deflator
            if event.key == pygame.K_i:
                diverY_change -= 4
                print(diverY_change)
            if event.key == pygame.K_d:
                diverY_change += 4
                print(diverY_change)
        if event.type == pygame.KEYUP:
            diverY_change = 0

    #Collision
    collision = distance(diverX, diverY, bigSharkX, bigSharkY)
    if collision:
        gameNotOver = 0
        bigSharkY = 2000
        rockY = 2000
        game_over_text()

    if bigSharkY > 1200:
        game_over_text()

    # water pressure (depth)
    if diverY <= 150:
        waterPressure = -0.02
    elif diverY <= 300:
        waterPressure = -0.01
    elif diverY <= 450:
        waterPressure = 0.01
    elif diverY <= 600:
        waterPressure = 0.02


    diverY_change += waterPressure
    diverY += diverY_change

    # Gets faster
    speedUp += 0.01
    # Big Shark
    bigSharkX -= bigSharkX_change + speedUp
    #rock
    rockX -= rockX_change + speedUp


    if diverY <= 0:
        diverY = 0
    if diverY >= 536:
        diverY = 536

    # If the obstacles reach the x = 0
    if bigSharkX <= 0 and gameNotOver:
        bigSharkX = 1200
        bigSharkY = random.randint(0, 350)
    if rockX <= 0 and gameNotOver:
        rockX = 1200
        rockY = random.randint(350, 500)


    screen.blit(oxygenTankImg, (1000, 50))
    diver(diverX, diverY)
    rock(rockX, rockY)
    bigShark(bigSharkX, bigSharkY)
    pygame.display.update()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
