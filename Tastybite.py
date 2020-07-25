import pygame
import time
import random

pygame.init()


display_width=500
display_height=400

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
color=(53,115,255)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Tasty bite -- Nnaji Uche")
clock=pygame.time.Clock()


#snake
def long(x, y, width, h, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, h])


#food
def chop(thing_x, chop_y, chop_w, chop_h, color):
    pygame.draw.rect(gameDisplay, color, [thing_x, chop_y, chop_w, chop_h])

def interset(count):
    font=pygame.font.SysFont(None, 25)
    text=font.render("score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))



#snake location
def long_locate():
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

    font=pygame.font.SysFont(None,30)
    img=font.render("WELCOME TO TASTY BITE BY UCHE. PRESS U TO START",True, color)


    gameExit=False


    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -2  #1
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


        x += x_change
        y += y_change

        gameDisplay.fill(white)

        long(x, y, width, h, color)
        chop(thing_x, chop_y, chop_w, chop_h,red)
        interset(contact)


        if x==thing_x and y==chop_y :           #this happens in extremely rare cases hence my choice of 3
            incre_w+=2
            contact+=1
            chop_y=random.randrange(0,display_height-20,2)
            thing_x =random.randrange(0,display_width-20,2)
            print("haaaaa")



        #LOGIC FOR SNAKE COMING TOWARDS Y AXIS PART 1
        if x+8==thing_x and y== chop_y-2 or x+6==thing_x and y==chop_y-4 or x+4==thing_x and y==chop_y-6 or x+2==thing_x and y==chop_y-8:                #new thinking
            incre_w +=2
            contact +=1
            chop_y=random.randrange(0,display_height-20,2)
            thing_x =random.randrange(0,display_width-20,2)   #food x axis
            print (2)


        #LOGIC FOR SNAKE COMING TOWARDS Axis PART 2
        if x-8==thing_x and y== chop_y+2 or x-6==thing_x and y==chop_y+4 or x-4==thing_x and y==chop_y+6 or x-2==thing_x and y==chop_y+8  : #new thinking
            incre_w +=2
            contact +=1
            chop_y=random.randrange(0,display_height-20,2)
            thing_x =random.randrange(0,display_width-20,2)
            print (-2)


        #LOGIC FOR OUT OF SCREEN
        if x > display_width or x<0:
            long_locate()
            interset(contact)
        if y > display_height or y<0:
            long_locate()
            interset(contact)


        pygame.display.update()
        clock.tick(60)
long_locate()
pygame.quit()
quit()
