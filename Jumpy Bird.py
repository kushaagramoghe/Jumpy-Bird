
import pygame
import time
from random import randint

green = (35, 232, 61)
blue = (37,241,245)
black = (0,0,0)
grey = (9,105,16)
grey2 = (24,168,33)
grey3 = (220,220,220)
green2 = (161,255,167)
green3 = (87,255,98)
yellow = (246,255,0)
white = (255,255,255)
orange = (255,187,0)
brown = (143,71,0)
red = (255, 0 ,0)

pygame.init()

size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Jumpy Bird")
icon = pygame.image.load('bird3.png')
pygame.display.set_icon(icon)


smallfont = pygame.font.SysFont("timesnewroman",25)
medfont = pygame.font.SysFont("timesnewroman",50)
largefont = pygame.font.SysFont("timesnewroman",80)

img = pygame.image.load('bird3.png')
city = pygame.image.load('city.png')
land = pygame.image.load('land1.png')
front = pygame.image.load('splash.png')
grass = pygame.image.load('grass.png')
scoreboard = pygame.image.load('scoreboard.png')

clock = pygame.time.Clock()

soundObj1 = pygame.mixer.Sound('point.wav')
soundObj2 = pygame.mixer.Sound('hit.wav')
soundObj3 = pygame.mixer.Sound('wing.wav')

pygame.mixer.music.load('birds.wav')
pygame.mixer.music.play(-1)

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
         textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def message_to_screen(msg,color, y_displace = 0, size = "small") :
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (350), (250) + y_displace
    screen.blit(textSurf, textRect)



def obstacle(xloc, xsize, yloc, ysize, space):

    pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen, green, [xloc, yloc+ysize+space, xsize, ysize+500])

    pygame.draw.rect(screen, black, [xloc+63, yloc, 7, ysize])
    pygame.draw.rect(screen, black, [xloc+63, yloc+ysize+space, 7, ysize+500])

    pygame.draw.rect(screen, grey, [xloc+56, yloc, 7, ysize])
    pygame.draw.rect(screen, grey, [xloc + 56, yloc + ysize + space, 7, ysize + 500])

    pygame.draw.rect(screen, grey2, [xloc+49, yloc, 7, ysize])
    pygame.draw.rect(screen, grey2, [xloc + 49, yloc + ysize + space, 7, ysize + 500])

    pygame.draw.rect(screen, green2, [xloc, yloc, 7, ysize])
    pygame.draw.rect(screen, green2, [xloc, yloc + ysize + space, 7, ysize + 500])

    pygame.draw.rect(screen, green3, [xloc+7, yloc, 7, ysize])
    pygame.draw.rect(screen, green3, [xloc+7, yloc+ysize+space, 7, ysize+500])

def frontscreen():
    x = False
    while not x:
        screen.fill(white)
        screen.blit(grass, [0, 350])
        screen.blit(front, [252, 100])
        message_to_screen("SPACE to play, Q to quit", black, 30, size="medium")

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    x = True
                    f = open("Log.txt", "r")
                    for line in f:
                        nscore = int(line)
                        #print('HII' + str(highscore))
                    f.close()
                    gameLoop(nscore)
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def endscreen(score):
    pygame.mixer.music.stop()
    x = False
    global highscore
    f = open("Log.txt", "r")
    for line in f:
        highscore = int(line)
    f.close()
    if score > highscore:
        o = open("Log.txt", 'w', newline="\r\n")
        o.write(str(score))
        o.close
        highscore = score
    while not x:
        screen.fill(blue)
        screen.blit(scoreboard, [240, 200])
        message_to_screen("SPACE to play again, Q to quit", black, 50, size="medium")


        font = pygame.font.SysFont("timesnewroman",30)
        text = font.render(("Score: " + str(score)), True, black)
        screen.blit(text, [0, 0])

        font = pygame.font.SysFont("timesnewroman", 30)
        text = font.render(("High Score: " + str(highscore)), True, black)
        screen.blit(text, [510, 0])

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    x = True
                    pygame.mixer.music.play(-1)
                    gameLoop(highscore)

                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def ball(x, y):
    screen.blit(img,[x,y])

#def gameover():
  #  font = pygame.font.Font(None ,50)
  #  text = font.render("Game over", True, black)
    #screen.blit(text, [150, 250])

def Score(score):
    font = pygame.font.SysFont("timesnewroman",30)
    text = font.render(("Score: "+str(score)), True, black)
    screen.blit(text, [0, 0])



def cloud(clx, cly):
    pygame.draw.circle(screen, grey3, [(clx),int(cly)],20)
    pygame.draw.circle(screen, grey3, [int(clx+15),int(cly-10)],20)
    pygame.draw.circle(screen, grey3, [int(clx+30),int(cly)],20)
    pygame.draw.circle(screen, grey3, [int(clx+15),int(cly+10)],20)

def Ground(ground):
    pygame.draw.rect(screen, brown, [0, ground, 700, 60])

def cloudcall():
    x1 = []
    y1 = []
    for i in range(0, 5):
        x1.append(randint(0, 700))
        y1.append(randint(0, 200))
    return x1 , y1

def gameLoop(highscore):

    size = 700, 500
    xloc = 700
    xsize = 70
    yloc = 0
    ysize = randint(50, 250)
    x = 350
    y = 250
    yspeed = 0
    ground = 494.5
    obspeed = 1
    space = 170
    limit = -80
    score = 0
    flag = 1
    start = False

    done = False

    x1 , y1 = cloudcall()

    while not done:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(blue)
        screen.blit(city, [0, 200])
        for i in range(0, 5):
            cloud(x1[i], y1[i])
        screen.blit(land, [0,485])
        obstacle(xloc, xsize, yloc, ysize, space)


        ball(x, y)
        Score(score)

        while not start:
            screen.fill(blue)
            screen.blit(city, [0, 200])
            for i in range(0, 5):
                cloud(x1[i], y1[i])
            screen.blit(land, [0, 485])
            obstacle(xloc, xsize, yloc, ysize, space)

            ball(x, y)
            Score(score)

            font = pygame.font.SysFont("timesnewroman", 30)
            text = font.render(("High Score: " + str(highscore)), True, black)
            screen.blit(text, [510, 0])

            message_to_screen("Press SPACE to start", black, -100, size="medium")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        yspeed = 1
                        start = True
            pygame.display.update()

    #x, y is top left of bird
    #xloc, yloc is top left of obstacle
    #obspeed is speed with which obstacle moves left

        while start:

            screen.fill(blue)
            screen.blit(city, [0, 200])
            for i in range(0, 5):
                cloud(x1[i], y1[i])
            screen.blit(land, [0, 485])
            obstacle(xloc, xsize, yloc, ysize, space)


            if score > highscore:
                highscore = score
            font = pygame.font.SysFont("timesnewroman", 30)
            text = font.render(("High Score: " + str(highscore)), True, black)
            screen.blit(text, [510, 0])

            ball(x, y)
            Score(score)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if flag != 0:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            yspeed = -1.75
                            pygame.mixer.Sound.play(soundObj3)

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_SPACE:
                            yspeed = 1.5



            if y+60 > ground:
                pygame.mixer.Sound.play(soundObj2)
                time.sleep(1)
                done = True
                start = False
                obspeed = 0
                yspeed = 0
                flag = 0
                #gameover()

            else:
                xloc -= obspeed
                y += yspeed

            if x+50 > xloc and y+7 < ysize and x< xsize+xloc:
                pygame.mixer.Sound.play(soundObj2)
                time.sleep(1)
                done = True
                start = False
                obspeed = 0
                yspeed = 0
                flag = 0
                #gameover()




            else:
                xloc -= obspeed
                y += yspeed

            if x+50 > xloc and y+50 > ysize+space and x < xsize+xloc:
                pygame.mixer.Sound.play(soundObj2)
                time.sleep(1)
                done = True
                start = False
                obspeed = 0
                yspeed = 0
                flag = 0
                #gameover()

            else:
                xloc -= obspeed
                y += yspeed

            if xloc < limit:
                ysize = randint(50, 250)
                xloc = 700

            else:
                xloc -= obspeed
                y += yspeed

            if x > xloc and x < xloc+5:
                score = (score + 1)
                pygame.mixer.Sound.play(soundObj1)
            pygame.display.update()
            clock.tick(60)


        pygame.display.update()

    endscreen(score)
    pygame.quit()
    quit()

frontscreen()
gameLoop(0)

