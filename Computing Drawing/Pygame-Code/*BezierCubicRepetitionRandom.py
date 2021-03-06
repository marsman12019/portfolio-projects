import pygame, sys, os, random, math, time
from pygame.locals import *

fileCount = 0
pygame.init()
windowX = 700
windowY = 800
window = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption('COMPUTING DRAWING')
screen = pygame.display.get_surface()

def clear():
    screen = pygame.display.get_surface()
    screen.fill((255, 255, 255))


def input(events):
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type ==  pygame.KEYDOWN and ((event.key == pygame.K_RETURN) or (event.key == pygame.K_KP_ENTER)):
            global fileCount
            screen = pygame.display.get_surface()
            filePath = './image'+str(int(time.time()))+'_'+str(fileCount) + '.png'
            print 'now saving image' + filePath
            pygame.image.save(screen, filePath)
            fileCount = fileCount+1


#Code below here ----------------------------------------------

def connect_points(pts, w):
    first_pt = pts[0]
    i = 1
    while i<len(pts):
        next_pt = pts[i]
        pygame.draw.aaline(screen, black, first_pt, next_pt, w)
        first_pt = next_pt
        i += 1



def random_point():
    x = random.randint(0,windowX)
    y = random.randint(0,windowY)
    return (x,y)

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


black = (0,0,0)
red = (255,0,0)
gray = (150, 150, 150)


clear()
while (1==1):

    # Vertical Copy
    y = 0
    while y <= windowY:

        # Set Control Pts
        control_pointlist = [(0,y), (windowX/3, y+7*random.gauss(0, .2)), (windowX-windowX/3, y+7*random.gauss(0, .2)), (windowX, y)]

        # pygame.draw.circle(screen, gray, (control_pointlist[0][0],control_pointlist[0][1]), 2, 0)
        # pygame.draw.circle(screen, gray, (control_pointlist[1][0],control_pointlist[1][1]), 2, 0)
        # pygame.draw.circle(screen, gray, (control_pointlist[2][0],control_pointlist[2][1]), 2, 0)

        pointlist = []

        # Curve Points
        t = 0
        while t <= 1:

            x = (1-t)**3*control_pointlist[0][0]+3*(1-t)**2*t*control_pointlist[1][0]+3*(1-t)*t**2*control_pointlist[2][0]+t**3*control_pointlist[3][0]
            y = (1-t)**3*control_pointlist[0][1]+3*(1-t)**2*t*control_pointlist[1][1]+3*(1-t)*t**2*control_pointlist[2][1]+t**3*control_pointlist[3][1]

            pointlist.append((x,y))

            t += .01

        y += 5

        connect_points(pointlist, 1)

    # pygame.draw.circle(screen, red, attractor, radius, 0)

    pygame.display.flip()
    input(pygame.event.get())
    # clear()



