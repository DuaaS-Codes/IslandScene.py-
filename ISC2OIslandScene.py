#Author: Duaa Shahzad
#Date: January 14, 2020
#ICS2O Pygame Culminating
#Island Scene

import pygame
clock = pygame.time.Clock() #Refreshes the screen
screen = pygame.display.set_mode((1000,500)) #Sets size of the screen
screen.fill((183,237,240)) #Sets colour of the screen
pygame.display.flip() #Updates the screen

#Sets colour values needed to be used in screen
WHITE = (255,255,255)
TAN = (220,192,129)
GREEN = (130,153,138)
BLUE = (117,124,213)
BLACK = (0,0,0)
darkBROWN = (84,58,54)
BROWN = (102,71,66)
lightBROWN = (156,112,103)
GREY = (174,185,191)
YELLOW = (225,217,83)
lightYELLOW = (239,228,176)
WHITE = (255,255,255)
ORANGE = (255,190,92)
BLACK = (0,0,0)

import math #Imports the math plugin
            #Needed to draw certain shapes

#Sets shapes needed to be used in screen
pygame.draw.circle(screen,YELLOW,(926,55),50,0)
pygame.draw.rect(screen,GREEN,(0,367,1000,80))
pygame.draw.circle(screen,lightYELLOW,(630,340),30)
pygame.draw.arc(screen,TAN,((455,330), (300,200)), math.pi/2, 20,70)
pygame.draw.rect(screen,BLUE,(0, 400, 1000, 129))
pygame.draw.ellipse(screen,ORANGE,[430,430,120,60],0)
pygame.draw.ellipse(screen,ORANGE,[280,420,120,60],0)
pygame.draw.circle(screen,ORANGE,(280,450),20)
pygame.draw.circle(screen,ORANGE,(430,460),20)
pygame.draw.circle(screen,WHITE,(530,450),10,0) 
pygame.draw.circle(screen,WHITE,(380,440),10,0)
pygame.draw.rect(screen,BROWN,(600,180,115,200))
pygame.draw.polygon(screen,darkBROWN,((600, 180), (652, 100),(715, 180)))
pygame.draw.rect(screen,GREY,(605,200,50,50))
pygame.draw.rect(screen,GREY,(660,200,50,50))
pygame.draw.rect(screen,lightBROWN,(625,280,65,100))
pygame.draw.circle(screen,WHITE,(250,110),30,0)
pygame.draw.circle(screen,WHITE,(290,110),30,0)
pygame.draw.circle(screen,WHITE,(350,70),30,0)
pygame.draw.circle(screen,WHITE,(390,70),30,0)
pygame.draw.circle(screen,WHITE,(550,50),30,0)
pygame.draw.circle(screen,WHITE,(590,50),30,0)
pygame.draw.arc(screen,BLACK,((813,88), (50,30)), math.pi/6, math.pi/1)
pygame.draw.arc(screen,BLACK,((770,88), (50,30)), math.pi/4, math.pi/1)
pygame.draw.arc(screen,BLACK,((673,50), (50,30)), math.pi/6, math.pi/1)
pygame.draw.arc(screen,BLACK,((720,50), (50,30)), math.pi/4, math.pi/1)

#While loop to refresh the screen
while (True):
 for i in range(0,250): #For loop to determine how far
                        #The shapes move on the screen
  screen.fill((183,237,240))
  pygame.draw.circle(screen,YELLOW,(926,55+i),50,0)
  pygame.draw.rect(screen,GREEN,(0,367,1000,80))
  pygame.draw.circle(screen,lightYELLOW,(630-i,340),30)
  pygame.draw.arc(screen,TAN,((455,330), (300,200)), math.pi/2, 20,70)
  pygame.draw.rect(screen,BLUE,(0, 400, 1000, 129))
  pygame.draw.ellipse(screen,ORANGE,[430+i,430,120,60],0)
  pygame.draw.ellipse(screen,ORANGE,[280+i,420,120,60],0)
  pygame.draw.circle(screen,ORANGE,(280+i,450),20)
  pygame.draw.circle(screen,ORANGE,(430+i,460),20)
  pygame.draw.circle(screen,WHITE,(530+i,450),10,0) 
  pygame.draw.circle(screen,WHITE,(380+i,440),10,0)
  pygame.draw.rect(screen,BROWN,(600,180,115,200))
  pygame.draw.polygon(screen,darkBROWN,((600, 180), (652, 100),(715, 180)))
  pygame.draw.rect(screen,GREY,(605,200,50,50))
  pygame.draw.rect(screen,GREY,(660,200,50,50))
  pygame.draw.rect(screen,lightBROWN,(625,280,65,100))
  pygame.draw.circle(screen,WHITE,(250-i,110),30,0)
  pygame.draw.circle(screen,WHITE,(290-i,110),30,0)
  pygame.draw.circle(screen,WHITE,(350-i,70),30,0)
  pygame.draw.circle(screen,WHITE,(390-i,70),30,0)
  pygame.draw.circle(screen,WHITE,(550+i,50),30,0)
  pygame.draw.circle(screen,WHITE,(590+i,50),30,0)
  pygame.draw.arc(screen,BLACK,((813,88-i), (50,30)), math.pi/6, math.pi/1)
  pygame.draw.arc(screen,BLACK,((770,88-i), (50,30)), math.pi/4, math.pi/1)
  pygame.draw.arc(screen,BLACK,((673,50-i), (50,30)), math.pi/6, math.pi/1)
  pygame.draw.arc(screen,BLACK,((720,50-i), (50,30)), math.pi/4, math.pi/1)
  clock.tick(100) #Controls the FPS the program runs at
  pygame.display.update() #Refreshes the screen
 
 event = pygame.event.poll() #Checks for user events 
 if (event.type == pygame.QUIT): 
    break 
#Used for the program to close 
#When the user chooses to end the program
