import pygame
import time
import random

pygame.init()

pygame.mixer.music.load("Deep Mind - Jeremy Black.mp3")
crash_sound=pygame.mixer.Sound("Mirror Shattering.wav")
chop_sound=pygame.mixer.Sound("Eating-Sound.wav")


display_width=500
display_height=400

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
color=(53,115,255)
yellow = (255, 255, 0)
blue = (0, 0, 255)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tasty bite -- Nnaji Uche")
clock=pygame.time.Clock()


#snake
def long(x, y, width, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, h])


#Restart game
def crash():
    message_display('You crashed Respawn')

#food
def chop(thing_x, chop_y, chop_w, chop_h, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, chop_y, chop_w, chop_h])


def interset(count):    #score board function
    font=pygame.font.SysFont(None, 25)
    text=font.render("score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

def instruct():
    font=pygame.font.SysFont(None, 25)
    text=font.render("PRESS P TO PAUSE", True, black)
    gameDisplay.blit(text,(300,0))

def game_over():
    font=pygame.font.SysFont(None, 30)
    text=font.render("GAME OVER MAN", True, black)
    gameDisplay.blit(text,(display_width/2-50,display_height/2))

    pygame.display.update()
    time.sleep(3)
    clock.tick(10)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


myfont=pygame.font.SysFont('Corbel',35)
font1=pygame.font.SysFont('Corbel',25)

text=myfont.render('PLAY >>',True,yellow)
text1=myfont.render('GAME PAUSED', True, yellow)
text2=font1.render('QUIT', True, black)
text3=font1.render('RESUME', True, black)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type ==pygame.MOUSEBUTTONDOWN:
                if display_width/2+250 > mouse[0] > display_width/2+100 and display_height/2+200 > mouse[1] > display_height/2+100:
                    long_locate()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Tasty bite", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)

        mouse=pygame.mouse.get_pos()

        if display_width/2+250 > mouse[0] > display_width/2+100 and display_height/2+150 > mouse[1] > display_height/2+100:
            pygame.draw.rect(gameDisplay,color,[display_width/2+100,display_height/2+150,100,10])


        gameDisplay.blit(text , (display_width/2+100,display_height/2+100))


        pygame.display.update()
        #time.sleep(5)   #display time
        #clock.tick(10)  #Frames per second


def paused():

    pause=True

    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if display_width/2+250 > mouse[0] > display_width/2+100 and display_height/2+200 > mouse[1] > display_height/2+100:     #text2
                    pygame.quit()
                    quit()
                    #game_intro()

                if display_width/2+100> mouse[0] > display_width/2-100 and display_height/2+200 > mouse[1] > display_height/2+100:     #text3
                    pause=False

        mouse=pygame.mouse.get_pos()


        gameDisplay.blit(text1 , (display_width/2-100,display_height/2))

        gameDisplay.blit(text2, (display_width/2+100,display_height/2+100))

        gameDisplay.blit(text3, (display_width/2-100,display_height/2+100))


        pygame.display.update()
        clock.tick(15)


#snake location
def long_locate():
    pygame.mixer.music.play(-1)

    x = 300
    y = 100

    x_change = 0
    y_change = 0
    width=20
    h=10

    thing_x =random.randrange(0,display_width-10,2)
    chop_y=random.randrange(0,display_height-10,2)  #food y axis
    chop_w=10   #food width
    chop_h=10   #food height

    incre_w= 0
    incre_h=0
    contact=0

    gameExit=False

    while not gameExit:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -2
                    y_change=0
                    h=incre_h+10    #h=10
                    width= incre_w+20  #width=20
                if event.key == pygame.K_RIGHT:
                    x_change = 2
                    y_change =0
                    h=incre_h+10        #h=10
                    width=incre_w+20    #width=20


                if event.key == pygame.K_UP:
                    y_change = -2
                    x_change=0
                    width=incre_h+10             #width=10
                    h=incre_w+20                   #h=20

                if event.key == pygame.K_DOWN:
                    y_change = 2
                    x_change=0
                    width=incre_h+10
                    h=incre_w+20

                if event.key == pygame.K_p:
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    x_change = 2
                    y_change=0

                if event.key == pygame.K_LEFT:
                    x_change = -2
                    y_change= 0
                if event.key == pygame.K_UP:
                    y_change = -2
                    x_change=0
                if event.key == pygame.K_DOWN:
                    y_change = 2
                    x_change=0

                if event.key == pygame.K_p:
                    paused()


        x += x_change
        y += y_change

        gameDisplay.fill(white)

        long(x, y, width, h, color)
        chop(thing_x, chop_y, chop_w, chop_h,red)

        interset(contact)
        instruct()


        if x==thing_x and y==chop_y :
            pygame.mixer.Sound.play(chop_sound)
            incre_w+=2
            contact+=1
            chop_y=random.randrange(0,display_height-20,2)
            thing_x =random.randrange(0,display_width-20,2)


        #LOGIC FOR SNAKE COMING TOWARDS Y AXIS PART 1
        if x+8==thing_x and y== chop_y-2 or x+6==thing_x and y==chop_y-4 or x+4==thing_x and y==chop_y-6 or x+2==thing_x and y==chop_y-8:                #new thinking
            pygame.mixer.Sound.play(chop_sound)
            incre_w +=2
            contact +=1
            chop_y=random.randrange(0,display_height-20,2)
            thing_x =random.randrange(0,display_width-20,2)


        #LOGIC FOR SNAKE COMING TOWARDS Axis PART 2
        if x-8==thing_x and y== chop_y+2 or x-6==thing_x and y==chop_y+4 or x-4==thing_x and y==chop_y+6 or x-2==thing_x and y==chop_y+8  : #new thinking
            pygame.mixer.Sound.play(chop_sound)
            incre_w +=2
            contact +=1
            chop_y=random.randrange(0,display_height-20,2)
            thing_x =random.randrange(0,display_width-20,2)


        if contact >= 5:            # if score is greater or equalt to five
            gameDisplay.fill(blue)
            long(x, y, width, h, red)
            chop(thing_x, chop_y, chop_w, chop_h,white)
            interset(contact)
            instruct()

            #This code makes the game slow . i guess there were too many color filling and blitting
        '''if contact >= 10:           #if score is greater or equal to ten
            gameDisplay.fill(color)
            long(x, y, width, h, white)
            chop(thing_x, chop_y, chop_w, chop_h,white)
            interset(contact)
            instruct()

        if contact >= 20:           #if score is greater or equal to fiveteen
            gameDisplay.fill(yellow)
            long(x, y, width, h, black)
            chop(thing_x, chop_y, chop_w, chop_h,red)
            interset(contact)
            instruct() '''

        #LOGIC FOR OUT OF SCREEN
        if x > display_width or x<0:
            pygame.mixer.Sound.play(crash_sound)
            pygame.mixer.music.stop()
            game_over()
            long_locate()
            interset(contact)
            instruct()

        if y > display_height or y<0:
            pygame.mixer.Sound.play(crash_sound)
            pygame.mixer.music.stop()
            game_over()
            long_locate()
            interset(contact)
            instruct()

        pygame.display.update()
        clock.tick(60)

game_intro()
#long_locate()
pygame.quit()
quit()
