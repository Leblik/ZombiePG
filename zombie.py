# The Zombie. Scroll-shooter game on PyGame
import pygame


# START VALUE
w_width = 500
w_height = 500
x, y = 50, 423
width = 60
height = 71
speed = 10
clock = pygame.time.Clock()

isJump = False
jumpCount = 10  # g - gravity constant m/c**2
run = True

left = False
right = False
animCount = 0  # count of animation
lastMove = "right"

bullets = []


# START PyGAME
pygame.init()
win = pygame.display.set_mode((w_width, w_height))  # set width and height of window
pygame.display.set_caption("Zombie")  # window name

# LOAD SPRITES
# lists of walk sprites
# walkRight = [pygame.image.load('right_1.png'), pygame.image.load('right_2.png'), pygame.image.load('right_3.png'),
#              pygame.image.load('right_4.png'), pygame.image.load('right_5.png'), pygame.image.load('right_6.png')]
#
# walkLeft = [pygame.image.load('left_1.png'), pygame.image.load('left_2.png'), pygame.image.load('left_3.png'),
#             pygame.image.load('left_4.png'), pygame.image.load('left_5.png'), pygame.image.load('left_6.png')]

# playerStand = pygame.image.load('idle.png')
# bg = pygame.image.load('bg.jpg')  # load background

class snaryad():
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing  # speed of snaryad

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


# Function clear and draw in window
def drawWindow():
    global animCount
    win.fill((0, 0, 0))  # clear window
    pygame.draw.rect(win, (10,255,20), (x, y, width, height))  # 1st ver. draw character "square" of player in win
    # with color(0,152,255) and coordinate (x, y, width, height)
    # Draw background
    win.blit(bg, (0, 0))
    # Count of frames
    if animCount +1 >= 30:  # 30 - frame/second
        animCount = 0
    # Draw character of player
    if left:
        win.blit(walkLeft[animCount // 5], (x, y))  # ...5...10...15...20...25...30 - 6 sprites on 30 frames / sec
        animCount += 1
    elif right:
        win.blit(walkRight[animCount // 5], (x, y))
        animCount += 1
    else:
        win.blit(playerStand, (x, y))
    # Draw bullets
    for bullet in bullets:
        bullet.draw(win)
    # win.blit(bg, (0, 0))  # draw background
    # Update the window of game
    pygame.display.update()


# START Game Loop
while run:

    clock.tick(30)  # 30 frame/sec
    # pygame.time.delay(int(0.05*1000))  # value of frames/sec
    # pygame.time.delay(50)

    # check all doing events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    # Check push keys
    keys = pygame.key.get_pressed()
    # if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT] and speed < 20:
    #     speed += 1
    # if (keys[pygame.K_RCTRL] or keys[pygame.K_LCTRL]) and speed > 3:
    #     speed -= 1

    # get shot
    if keys[pygame.K_f]:
        if lastMove == "right":
            facing = 1
        else:
            facing = -1

        if len(bullets) < 5:
            bullets.append(snaryad(round(x + width // 2), round(y + height // 2), 5, (255, 0, 0), facing))

    # move left-right
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and x > speed:
        x -= speed
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and x < w_width - width - speed:
        x += speed
        right = True
        left = False
        lastMove = "right"
    else:
        left = False
        right = False
        animCount = 0


    # if not(isJump):  # isJump = False
    #     if keys[pygame.K_UP] or keys[pygame.K_w] and y > speed:
    #         y -= speed
    #     if keys[pygame.K_DOWN] or keys[pygame.K_s] and y < w_width - height - speed:
    #         y += speed
    #     if keys[pygame.K_SPACE]:
    #         isJump = True
    # else:  # isJump = True
    #     if jumpCount >= -10:
    #         if jumpCount < 0:
    #             y += (jumpCount ** 2) / 2
    #         else:
    #             y -= (jumpCount ** 2) / 2
    #         jumpCount -= 1
    #     else:
    #         isJump = False
    #         jumpCount = 10

    if isJump:  # isJump = True
        print("DEBUG:   y=", y, ", jumpCount(g)=", jumpCount)  # debug
        if jumpCount >= -10:
            if jumpCount > 0:
                y -= (jumpCount ** 2) / 2
            else:
                y += (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    else:  # isJump = False
        # if keys[pygame.K_UP] or keys[pygame.K_w] and y > speed:  # move UP
        #     y -= speed
        # if keys[pygame.K_DOWN] or keys[pygame.K_s] and y < w_width - height - speed:  # move DOWN
        #     y += speed
        if keys[pygame.K_SPACE]:  # make JUMP
            isJump = True

    # # 1st ver. Clear and draw in window
    win.fill((0, 0, 0))  # clear window
    pygame.draw.rect(win, (10,255,20), (x, y, width, height))  # draw character "square" of player in win
    # with color(0,152,255) and coordinate (x, y, width, height)
    pygame.display.update()  # update the window of game

    # 2st ver. Clear and draw in window by func "drawWindow"
    # drawWindow()

# END Game Loop

pygame.quit()  # Exit PyGame window
