import pygame
import random
import pygame.mixer
import math

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load("music1.mp3")  # Imports music
pygame.mixer.music.play()  # Plays music


def move1(image1, image2, image3, image4):  # Moving animation for Ashe
    global count
    if count < 5:
        image = image1
    elif 5 <= count < 11:
        image = image2
    elif 11 <= count < 16:
        image = image3
    elif count >= 16:
        image = image4

    if count >= 21:
        count = 0
    else:
        count += 1
    return image


def move2(image1, image2, image3, image4):  # Moving animation for Misty
    global count
    if count < 5:
        image = image1
    elif 5 <= count < 11:
        image = image2
    elif 11 <= count < 16:
        image = image3
    elif count >= 16:
        image = image4
    if count >= 21:
        count = 0
    else:
        count += 1
    return image


def playersTouching():  # If players collides with each other they will be bounced back by 2
    global xa, ya, x, y

    if -20 < xa - x < 20 and -20 < ya - y < 20:
        xDiff = xa - x
        yDiff = ya - y

        for dist in range(math.floor(xDiff)//2):
            if xDiff > 0:
                if xa + 20 + 2 < rightWall:  # Prevents the players from being knocked into walls
                    xa += 2  # If it is clear on the sides the players will get knoced by 2 units
                if x - 2 > leftWall:
                    x -= 2
            else:
                if xa - 2 > leftWall:
                    xa -= 2
                if x + 2 + 20 < rightWall:
                    x += 2

        for dist in range(math.floor(xDiff)//2):
            if yDiff > 0:
                if ya + 2 + 20 < bottomWall:
                    ya += 2  # If it is clear on the top and bottom players will get knocked up or down by 2 units
                if y - 2 > topWall:
                    y -= 2
            else:
                if ya - 2 > topWall:
                    ya -= 2
                if y + 2 + 20 < bottomWall:
                    y += 2


def touchingCoin(cx, cy):  # To check if players are touching the collision box of the coin
    return -20 < cx - coinPos[0] < 20 and -20 < cy - coinPos[1] < 20


def randomPosition():  # Method to calculate a random coordinates without getting off screen and returning the value to method caller
    cx = random.randrange(15, windowSize[0] - 35)
    cy = random.randrange(64, windowSize[1] - 9)
    return cx, cy


windowSize = [480, 296]  # Setting up windows
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

pointFont = pygame.font.SysFont("Monospace", 15)  # Font of points

astanding = pygame.image.load('astanding.png')  # Standing images
standing = pygame.image.load('standing.png')

down1 = pygame.image.load('down1.png')  # Ashe's down animation
down2 = pygame.image.load('down2.png')
down3 = pygame.image.load('down3.png')
down4 = pygame.image.load('down4.png')

back1 = pygame.image.load('back1.png')  # Misty's down animation
back2 = pygame.image.load('back2.png')
back3 = pygame.image.load('back3.png')
back4 = pygame.image.load('back2.png')

up1 = pygame.image.load('up1.png')  # Ashe's up animation
up2 = pygame.image.load('up2.png')
up3 = pygame.image.load('up3.png')
up4 = pygame.image.load('up4.png')

front1 = pygame.image.load('front1.png')  # Misty's up animation
front2 = pygame.image.load('front2.png')
front3 = pygame.image.load('front3.png')
front4 = pygame.image.load('front2.png')

aright1 = pygame.image.load('aright1.png')  # Ashe's right animation
aright2 = pygame.image.load('aright2.png')
aright3 = pygame.image.load('aright3.png')
aright4 = pygame.image.load('aright4.png')

right1 = pygame.image.load('right1.png')  # Misty's right animation
right2 = pygame.image.load('right2.png')
right3 = pygame.image.load('right3.png')
right4 = pygame.image.load('right2.png')

aleft1 = pygame.image.load('aleft1.png')  # Ashe's left animation
aleft2 = pygame.image.load('aleft2.png')
aleft3 = pygame.image.load('aleft3.png')
aleft4 = pygame.image.load('aleft4.png')

left1 = pygame.image.load('left1.png')  # Misty's left animation
left2 = pygame.image.load('left2.png')
left3 = pygame.image.load('left3.png')
left4 = pygame.image.load('left2.png')

poke1 = pygame.image.load('poke1.png')  # Pokeballs
poke2 = pygame.image.load('poke2.png')

coinSound = pygame.mixer.Sound("coin.wav")  # Music and sound effects

background = pygame.image.load('pokemonCentre.png')  # Background image

topWall = 63  # Defining walls
bottomWall = windowSize[1] - 38
leftWall = 15
rightWall = windowSize[0] - 15

count = 0
xa = windowSize[0] / 2 - (windowSize[0] / 4)  # Starting coordinates for Ashe
ya = windowSize[1] / 2
x = windowSize[0] / 2 + (windowSize[0] / 4)  # Starting coordinates for Misty
y = windowSize[1] / 2

coinPos = randomPosition()  # First position of the pokeball(coin)
mpoints = 0  # Scores for Misty
apoints = 0  # Scores for Ashe

locked = False

done = False
while not done:
    keys = pygame.key.get_pressed()
    if not locked:
        if keys[pygame.K_s]:  # Controls for the player Ashe which uses the keys w,a,s,d
            aimage = move1(down1, down2, down3, down4)
            if (
                    ya + 1) < bottomWall:  # This is to check the space available to make sure Ashe doesn't walk into the walls
                ya += 1
        elif keys[pygame.K_w]:
            aimage = move1(up1, up2, up3, up4)
            if (ya - 1) > topWall:
                ya -= 1
        elif keys[pygame.K_d]:
            aimage = move1(aright1, aright2, aright3, aright4)
            if (xa + 1) + 20 < rightWall:
                xa += 1
        elif keys[pygame.K_a]:
            aimage = move1(aleft1, aleft2, aleft3, aleft4)
            if (xa - 1) > leftWall:
                xa -= 1
        elif keys[pygame.K_SPACE]:
            locked = True
        else:
            aimage = astanding
    if not locked:
        if keys[pygame.K_DOWN]:  # Controls for the player Misty which uses arrow keys on the right side of the keyboard
            image = move2(front1, front2, front3, front4)
            if (
                    y + 1) < bottomWall:  # This is to check for the space available to make sure Misty doesn't walk into the walls
                y += 1
        elif keys[pygame.K_UP]:
            image = move2(back1, back2, back3, back4)
            if (y - 1) > topWall:
                y -= 1
        elif keys[pygame.K_RIGHT]:
            image = move2(right1, right2, right3, right4)
            if (x + 1) + 20 < rightWall:
                x += 1
        elif keys[pygame.K_LEFT]:
            image = move2(left1, left2, left3, left4)
            if (x - 1) > leftWall:
                x -= 1
        elif keys[pygame.K_SPACE]:
            locked = True
        else:
            image = standing

    playersTouching()  # Checking if players are touching each other

    if touchingCoin(xa, ya):  # Checking if Ashe touches the coin
        apoints += 1
        coinSound.play()

    if touchingCoin(x, y):  # Checking if Misty touches the coin
        mpoints += 1
        coinSound.play()

    if touchingCoin(xa, ya) or touchingCoin(x, y):  # Moves coin to random position when players touch it
        coinPos = randomPosition()

    apointslabel = pointFont.render(str(apoints), 1, (0, 0, 0))  # Displaying points of Ashe
    mpointslabel = pointFont.render(str(mpoints), 1, (0, 0, 0))  # Displaying points of Misty

    screen.blit(background, (0, 0))
    screen.blit(aimage, (xa, ya))  # For image to appear on screen
    screen.blit(image, (x, y))
    screen.blit(poke1, coinPos)
    screen.blit(apointslabel, [xa - 8, ya - 8])
    screen.blit(mpointslabel, [x - 8, y - 8])

    pygame.display.flip()  # Refreshes screen so image shows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    clock.tick(60)
pygame.quit()
