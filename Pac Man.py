import pygame
import random
import math
pygame.init()

# Screen
screen_x = 599
screen_y = 512
screen = pygame.display.set_mode((screen_x, screen_y))
pygame.display.set_caption("PAC MAN")
icon1 = pygame.image.load('arcade-game.png')
pygame.display.set_icon(icon1)
background = pygame.image.load('NewGame/Graphics/Backgrounds/bg_desert.png').convert_alpha()
bg_x=0
test_font=pygame.font.Font('NewGame/Graphics/font/Pixeltype.ttf',50)
text_surface=test_font.render('My game',False,'Black')

# Player
playerimg = pygame.image.load('gamer.png')
player_x = (screen_x/2) - 32
player_y = (screen_y/2) +156
player_dx = 0
player_dy = 0

# Alien1
alien1img=pygame.image.load('ghost.png')
alien1_x=random.randint(0,screen_x-20-200)
alien1_y=random.randint(0,screen_y-64-200)
alien1_dx=.5
alien1_dy=.5

# Alien2
alien2img=pygame.image.load('ghost2.png')
alien2_x=random.randint(0,screen_x-20-200)
alien2_y=random.randint(0,screen_y-64-200)
alien2_dx=.5
alien2_dy=.5

# Alien3
alien3img=pygame.image.load('ghost2.png')
alien3_x=random.randint(0,screen_x-20-200)
alien3_y=random.randint(0,screen_y-64-200)
alien3_dx=.5
alien3_dy=.5

# Alien4
alien4img=pygame.image.load('ghost.png')
alien4_x=random.randint(0,screen_x-20-200)
alien4_y=random.randint(0,screen_y-64-200)
alien4_dx=.5
alien4_dy=0.5

# Alien5
alien5img=pygame.image.load('ghost2.png')
alien5_x=random.randint(0,screen_x-20-200)
alien5_y=random.randint(0,screen_y-64-200)
alien5_dx=.5
alien5_dy=.5

# Alien6
alien6img=pygame.image.load('ghost.png')
alien6_x=random.randint(0,screen_x-20-200)
alien6_y=random.randint(0,screen_y-64-200)
alien6_dx=0.5
alien6_dy=0.5

# Alien7
alien7img=pygame.image.load('ghost2.png')
alien7_x=random.randint(20,screen_x-20)
alien7_y=random.randint(20,screen_y-20)
alien7_dx=1
alien7_dy=1

# Alien8
alien8img=pygame.image.load('ghost.png')
alien8_x=random.randint(0,screen_x-20)
alien8_y=random.randint(0,screen_y-20)
alien8_dx=1
alien8_dy=1

# Alien9
alien9img=pygame.image.load('ghost2.png')
alien9_x=random.randint(0,screen_x-20)
alien9_y=random.randint(0,screen_y-20)
alien9_dx=1
alien9_dy=1

# Food1
food1img=pygame.image.load('record.png')
food1_x=random.randint(0,screen_x-20)
food1_y=random.randint(0,screen_y-20-200)

# Food2
food2img=pygame.image.load('record.png')
food2_x=random.randint(0,screen_x-20)
food2_y=random.randint(0,screen_y-20-200)

# Food3
food3img=pygame.image.load('record.png')
food3_x=random.randint(0,screen_x-20)
food3_y=random.randint(0,screen_y-20-200)

# Food4
food4img=pygame.image.load('record.png')
food4_x=random.randint(0,screen_x-20)
food4_y=random.randint(0,screen_y-20-200)

# Food5
food5img=pygame.image.load('record.png')
food5_x=random.randint(0,screen_x-20)
food5_y=random.randint(0,screen_y-20-200)

# Food6
food6img=pygame.image.load('record.png')
food6_x=random.randint(0,screen_x-20)
food6_y=random.randint(0,screen_y-20-200)

# Food7
food7img=pygame.image.load('record.png')
food7_x=random.randint(0,screen_x-20)
food7_y=random.randint(0,screen_y-20-200)

# Food8
food8img=pygame.image.load('record.png')
food8_x=random.randint(0,screen_x-20)
food8_y=random.randint(0,screen_y-20-200)

# Food9
food9img=pygame.image.load('record.png')
food9_x=random.randint(0,screen_x-20)
food9_y=random.randint(0,screen_y-20-200)

# Food10
food10img=pygame.image.load('record.png')
food10_x=random.randint(0,screen_x-20)
food10_y=random.randint(0,screen_y-20-200)

# Food11
food11img=pygame.image.load('record.png')
food11_x=random.randint(0,screen_x-20)
food11_y=random.randint(0,screen_y-20-200)

# Food12
food12img=pygame.image.load('record.png')
food12_x=random.randint(0,screen_x-20)
food12_y=random.randint(0,screen_y-20-200)

# Food13
food13img=pygame.image.load('record.png')
food13_x=random.randint(0,screen_x-20)
food13_y=random.randint(0,screen_y-20-200)

# Food14
food14img=pygame.image.load('record.png')
food14_x=random.randint(0,screen_x-20)
food14_y=random.randint(0,screen_y-20-200)

# Food15
food15img=pygame.image.load('record.png')
food15_x=random.randint(0,screen_x-20)
food15_y=random.randint(0,screen_y-20-200)

# Food16
food16img=pygame.image.load('record.png')
food16_x=random.randint(0,screen_x-20)
food16_y=random.randint(0,screen_y-20-200)

# Food17
food17img=pygame.image.load('record.png')
food17_x=random.randint(0,screen_x-20)
food17_y=random.randint(0,screen_y-20-200)

# Food18
food18img=pygame.image.load('record.png')
food18_x=random.randint(0,screen_x-20)
food18_y=random.randint(0,screen_y-20-200)

# Food19
food19img=pygame.image.load('record.png')
food19_x=random.randint(0,screen_x-20)
food19_y=random.randint(0,screen_y-20-200)

# Food20
food20img=pygame.image.load('record.png')
food20_x=random.randint(0,screen_x-20)
food20_y=random.randint(0,screen_y-20-200)

def food1(x,y):
    screen.blit(food1img,(x,y))
def food2(x,y):
    screen.blit(food2img,(x,y))
def food3(x,y):
    screen.blit(food3img,(x,y))
def food4(x,y):
    screen.blit(food4img,(x,y))
def food5(x,y):
    screen.blit(food5img,(x,y))
def food6(x,y):
    screen.blit(food6img,(x,y))
def food7(x,y):
    screen.blit(food7img,(x,y))
def food8(x,y):
    screen.blit(food8img,(x,y))
def food9(x,y):
    screen.blit(food9img,(x,y))
def food10(x,y):
    screen.blit(food10img,(x,y))
def food11(x,y):
    screen.blit(food1img,(x,y))
def food12(x,y):
    screen.blit(food2img,(x,y))
def food13(x,y):
    screen.blit(food3img,(x,y))
def food14(x,y):
    screen.blit(food4img,(x,y))
def food15(x,y):
    screen.blit(food5img,(x,y))
def food16(x,y):
    screen.blit(food6img,(x,y))
def food17(x,y):
    screen.blit(food7img,(x,y))
def food18(x,y):
    screen.blit(food8img,(x,y))
def food19(x,y):
    screen.blit(food9img,(x,y))
def food20(x,y):
    screen.blit(food10img,(x,y))

def Alien1(x,y):
    screen.blit(alien1img,(x,y))
def Alien2(x,y):
    screen.blit(alien2img,(x,y))
def Alien3(x,y):
    screen.blit(alien3img,(x,y))
def Alien4(x,y):
    screen.blit(alien4img,(x,y))
def Alien5(x,y):
    screen.blit(alien5img,(x,y))
def Alien6(x,y):
    screen.blit(alien6img,(x,y))
def Alien7(x,y):
    screen.blit(alien7img,(x,y))
def Alien8(x,y):
    screen.blit(alien8img,(x,y))
def Alien9(x,y):
    screen.blit(alien9img,(x,y))



def player(x, y):
    screen.blit(playerimg, (x, y))

# Game Loop
run = True
while run:
        screen.fill((0, 0, 0))
        bg_x-=1
        if bg_x< -background.get_width():
         bg_x=0
        screen.blit(background,(bg_x,0))
        screen.blit(background,(bg_x+background.get_width(),0))
        #screen.blit(text_surface,(300,50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_dy = -0.75
                if event.key == pygame.K_DOWN:
                    player_dy = +0.75
                if event.key == pygame.K_LEFT:
                    player_dx = -0.75
                if event.key == pygame.K_RIGHT:
                    player_dx = +0.75
                    
            if event.type == pygame.KEYUP:
                player_dx = 0
                player_dy = 0
        player_x += player_dx
        player_y += player_dy
        alien1_x+=alien1_dx
        alien1_y+=alien1_dy
        alien2_x+=alien2_dx
        alien2_y+=alien2_dy
        alien3_x+=alien3_dx
        alien3_y+=alien3_dy
        alien4_x+=alien4_dx
        alien4_y+=alien4_dy
        alien5_x+=alien5_dx
        alien5_y+=alien5_dy
        alien6_x+=alien6_dx
        alien6_y+=alien6_dy
        alien7_x+=alien7_dx
        alien7_y+=alien7_dy
        alien8_x+=alien8_dx
        alien8_y+=alien8_dy
        alien9_x+=alien9_dx
        alien9_y+=alien9_dy
        
        if player_x>=(screen_x-64):
            player_x=(screen_x-64)
        if player_x<=0:
            player_x=0
        if player_y>=(screen_y-64):
            player_y=screen_y-64
        if player_y<=0:
            player_y=0
        if alien1_x<=0 or alien1_x>=(screen_x-64):
            alien1_dx=-alien1_dx
        if alien1_y<=0 or alien1_y>=(screen_y-64-200):
            alien1_dy=-alien1_dy
        if alien2_x<=0 or alien2_x>=(screen_x-64):
            alien2_dx=-alien2_dx
        if alien2_y<=0 or alien2_y>=(screen_y-64-200):
            alien2_dy=-alien2_dy
        if alien3_x<=0 or alien3_x>=(screen_x-64):
            alien3_dx=-alien3_dx
        if alien3_y<=0 or alien3_y>=(screen_y-64-200):
            alien3_dy=-alien3_dy
        if alien4_x<=0 or alien4_x>=(screen_x-64):
            alien4_dx=-alien4_dx
        if alien4_y<=0 or alien4_y>=(screen_y-64-200):
            alien4_dy=-alien4_dy
        if alien5_x<=0 or alien5_x>=(screen_x-64):
            alien5_dx=-alien5_dx
        if alien5_y<=0 or alien5_y>=(screen_y-64-200):
            alien5_dy=-alien5_dy
        if alien6_x<=0 or alien6_x>=(screen_x-64):
            alien6_dx=-alien6_dx
        if alien6_y<=0 or alien6_y>=(screen_y-64-200):
            alien6_dy=-alien6_dy
        if math.sqrt((player_x-food1_x)**2 + (player_y-food1_y)**2)<=40:
            food1_x=-100
            food1_y=-100
        if math.sqrt((player_x-food2_x)**2 + (player_y-food2_y)**2)<=40:
            food2_x=-100
            food2_y=-100
        if math.sqrt((player_x-food3_x)**2 + (player_y-food3_y)**2)<=40:
            food3_x=-100
            food3_y=-100
        if math.sqrt((player_x-food4_x)**2 + (player_y-food4_y)**2)<=40:
            food4_x=-100
            food4_y=-100
        if math.sqrt((player_x-food5_x)**2 + (player_y-food5_y)**2)<=40:
            food5_x=-100
            food5_y=-100
        if math.sqrt((player_x-food6_x)**2 + (player_y-food6_y)**2)<=40:
            food6_x=-100
            food6_y=-100
        if math.sqrt((player_x-food7_x)**2 + (player_y-food7_y)**2)<=40:
            food7_x=-100
            food7_y=-100
        if math.sqrt((player_x-food8_x)**2 + (player_y-food8_y)**2)<=40:
            food8_x=-100
            food8_y=-100
        if math.sqrt((player_x-food9_x)**2 + (player_y-food9_y)**2)<=40:
            food9_x=-100
            food9_y=-100
        if math.sqrt((player_x-food10_x)**2 + (player_y-food10_y)**2)<=40:
            food10_x=-100
            food10_y=-100
        if math.sqrt((player_x-food11_x)**2 + (player_y-food11_y)**2)<=40:
            food11_x=-100
            food11_y=-100
        if math.sqrt((player_x-food12_x)**2 + (player_y-food12_y)**2)<=40:
            food12_x=-100
            food12_y=-100
        if math.sqrt((player_x-food13_x)**2 + (player_y-food13_y)**2)<=40:
            food13_x=-100
            food13_y=-100
        if math.sqrt((player_x-food14_x)**2 + (player_y-food14_y)**2)<=40:
            food14_x=-100
            food14_y=-100
        if math.sqrt((player_x-food15_x)**2 + (player_y-food15_y)**2)<=40:
            food15_x=-100
            food15_y=-100
        if math.sqrt((player_x-food16_x)**2 + (player_y-food16_y)**2)<=40:
            food16_x=-100
            food16_y=-100
        if math.sqrt((player_x-food17_x)**2 + (player_y-food17_y)**2)<=40:
            food17_x=-100
            food17_y=-100
        if math.sqrt((player_x-food18_x)**2 + (player_y-food18_y)**2)<=40:
            food18_x=-100
            food18_y=-100
        if math.sqrt((player_x-food19_x)**2 + (player_y-food19_y)**2)<=40:
            food19_x=-100
            food19_y=-100
        if math.sqrt((player_x-food20_x)**2 + (player_y-food20_y)**2)<=40:
            food20_x=-100
            food20_y=-100
        if math.sqrt((player_x-alien1_x)**2+(player_y-alien1_y)**2)<=40:
            run = False
        if math.sqrt((player_x-alien2_x)**2+(player_y-alien2_y)**2)<=40:
            run = False
        if math.sqrt((player_x-alien3_x)**2+(player_y-alien3_y)**2)<=40:
            run = False
        if math.sqrt((player_x-alien4_x)**2+(player_y-alien4_y)**2)<=40:
            run = False
        if math.sqrt((player_x-alien5_x)**2+(player_y-alien5_y)**2)<=40:
            run = False
        if math.sqrt((player_x-alien6_x)**2+(player_y-alien6_y)**2)<=40:
            run = False

        player(player_x, player_y)
        Alien1(alien1_x,alien1_y)
        Alien2(alien2_x,alien2_y)
        Alien3(alien3_x,alien3_y)
        Alien4(alien4_x,alien4_y)
        Alien5(alien5_x,alien5_y)
        Alien6(alien6_x,alien6_y)
        food1(food1_x,food1_y)
        food2(food2_x,food2_y)
        food3(food3_x,food3_y)
        food4(food4_x,food4_y)
        food5(food5_x,food5_y)
        food6(food6_x,food6_y)
        food7(food7_x,food7_y)
        food8(food8_x,food8_y)
        food9(food9_x,food9_y)
        food10(food10_x,food10_y)
        food11(food11_x,food11_y)
        food12(food12_x,food12_y)
        food13(food13_x,food13_y)
        food14(food14_x,food14_y)
        food15(food15_x,food15_y)
        food16(food16_x,food16_y)
        food17(food17_x,food17_y)
        food18(food18_x,food18_y)
        food19(food19_x,food19_y)
        food20(food20_x,food20_y)
        pygame.display.update()
    
    

pygame.quit()



    
