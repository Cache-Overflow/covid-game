import pygame
from pygame.locals import *
import random
import math
import sys
from pygame import mixer
import webbrowser
mainClock = pygame.time.Clock()
pygame.init()

# background
background = pygame.image.load("vessel.jpg")
win = pygame.display.set_mode((1000,800))
pygame.display.set_caption("Corona Defense")

font = pygame.font.Font('Naughty_Cartoons.ttf', 16)
introtext = pygame.font.Font('Naughty_Cartoons.ttf', 30)
titletext = pygame.font.Font('Naughty_Cartoons.ttf', 50)
mixer.music.load("bgmusic.wav")
#player/white blood cell code
#Starting position in the bottom left
x = 0
y = 650
width = 100
height = 100
vel = 3
virusHeight = 50
virusWidth = 50
score = 100
score_value = 0
scoreX = 10
scoreY = 10
boardX = 10
boardY = 700
lives = 3
high_score = 0

class button():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = introtext
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False
def show_score(x,y, score_value, high_score):
    score = font.render("Score: "+ str(score_value), True, (255,255,255))
    high_score = font.render("High Score: " + str(high_score), True, (255,255,255))
    win.blit(high_score, (x, y+30))
    win.blit(score,(x,y))

def show_lives(x,y, lives):
    life = font.render("Lives: " + str(lives), True, (255,255,255))
    win.blit(life,(x,y))
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)
def stopTheSpread():
     mixer.music.stop()
     while True:
        pygame.display.update()
        win.blit(background, (0,0))
        draw_text('stay home. save lives.', titletext, (255, 255, 255), win, 40, 50)
        draw_text('Help stop coronavirus', introtext, (255, 255, 255), win, 200, 150)
        draw_text('1. stay home as much as you can', font, (255, 255, 255), win, 300, 250)
        draw_text('2. keep a safe distance', font, (255, 255, 255), win, 300, 300)
        draw_text('3. wash hands often', font, (255, 255, 255), win, 300, 350)
        draw_text('4. cover your cough', font, (255, 255, 255), win, 300, 400)
        draw_text('5. sick? Call ahead', font, (255, 255, 255), win, 300, 450)
        button_moreinfo = button((139,0,0), 325, 525, 280, 50, "More Info")
        button_mainmenu = button((139,0,0), 325, 625, 280, 50, "Main Menu")
        button_mainmenu.draw(win, (0,0,0))
        button_moreinfo.draw(win, (0,0,0))
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_mainmenu.isOver(pos):
                    main_menu()
                if button_moreinfo.isOver(pos):
                    webbrowser.open("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public")
            if event.type == pygame.MOUSEMOTION:
                if button_mainmenu.isOver(pos):
                    button_mainmenu.color = (0,0,0)
                else:
                    button_mainmenu.color = (139, 0, 0)
        mainClock.tick(60)
def main_menu():
    while True:
        pygame.display.update()
        button_play = button((139,0,0), 420, 310, 150, 50, "Play")
        button_stop = button((139,0,0), 420, 410, 150, 50, "HELP")
        button_quit = button((139,0,0), 420, 510, 150, 50, "Quit")
        win.blit(background, (0,0))
        button_play.draw(win, (255,255,255))
        button_quit.draw(win, (255,255,255))
        button_stop.draw(win, (255,255,255))
        draw_text('Corona Defense', titletext, (255, 255, 255), win, 175, 50)
        draw_text('Main Menu', introtext, (255, 255, 255), win, 375, 200)

        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.isOver(pos):
                    game()
                if button_quit.isOver(pos):
                    pygame.quit()
                    sys.exit()
                if button_stop.isOver(pos):
                    stopTheSpread()
            if event.type == pygame.MOUSEMOTION:
                if button_play.isOver(pos):
                    button_play.color = (0,0,0)
                    button_quit.color = (0,0,0) 
                else:
                    button_play.color = (139, 0, 0)
                    button_quit.color = (139,0,0)
        mainClock.tick(60)
def game_over():
    mixer.music.stop()
    gameover = mixer.Sound("gameover.wav")
    gameover.set_volume(0.1)
    gameover.play()
    while True:
        pygame.display.update()
        button_retry = button((139,0,0), 420, 310, 180, 50, "Retry")
        button_mainmenu = button((139,0,0), 380, 410, 280, 50, "Main Menu")

        win.blit(background, (0,0))
        button_retry.draw(win, (255,255,255))
        button_mainmenu.draw(win, (255,255,255))
        draw_text('Game Over', introtext, (255, 255, 255), win, 380, 200)

        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_retry.isOver(pos):
                    game()
                if button_mainmenu.isOver(pos):
                    main_menu()
            if event.type == pygame.MOUSEMOTION:
                if button_retry.isOver(pos):
                    button_retry.color = (0,0,0)
                    button_mainmenu.color = (0,0,0) 
                else:
                    button_retry.color = (139, 0, 0)
                    button_mainmenu.color = (139,0,0)
        mainClock.tick(60)

## Three Things TO DO:
#1. Enemy collision
#2. Enemy Spawn
#3. Enemy Respawning

#virus code to create many viruses

#white bloodcells
whiteImg = pygame.image.load("cell.png")
whiteImg = pygame.transform.scale(whiteImg, (width, height))
#Positive Y direction = moving downward.
#Sets the downward velocity of the virus

def collides(cellX,cellY,virX,virY):
    
    #midpoint of white blood cell
    cellX += 50
    cellY += 50
    #midpoint of virus
    virX += 25
    virY += 25
    d = math.sqrt((virX-cellX)**2 + (virY-cellY)**2)
    if d < 75:

        return True
    else:
        return False


def virus(virusI, x, y):
    win.blit(virusI,(x, y))

def game():
    mixer.music.play(-1)
    mixer.music.set_volume(0.1)
    x=500
    y=600
    run = True
    virusImg = []
    virusX = []
    virusY = []
    virusY_change = []
    virusX_change = []
    num_of_virus = 3
    score_value = 0
    lives = 3
    global high_score
    for i in range(num_of_virus):
        virusImg.append(pygame.image.load("virus.png"))
        virusImg[i] = pygame.transform.scale(virusImg[i], (virusWidth, virusHeight))
        virusX.append(random.randint(100,900))
        virusY.append(random.randint(50,150))
        virusY_change.append(random.randint(1,3))
        virusX_change.append(random.randint(1,10))
    while run:
        pygame.time.delay(7) # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
        show_score(boardX,boardY, show_score, high_score)
        #Ends game when window is closed
        for event in pygame.event.get():  # This will loop through a list of any keyboard or mouse events.
            if event.type == pygame.QUIT: # Checks if the red button in the corner of the window is clicked
                run = False # Ends the game loop
                sys.exit()  

        #Moves the red rectangle when arrowkeys are pressed
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > vel:
            x -= vel
        if keys[pygame.K_RIGHT] and x < 1000 - width - vel:
            x += vel
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 800 - height - vel:
            y += vel

        #Adds background
        win.blit(background, (0,0))
        #dispays white blood cell
        win.blit(whiteImg, (x,y))
        for i in range(num_of_virus):
            #Draw virus image
            virus(virusImg[i],virusX[i], virusY[i])
            #Moves the virus Down
            virusY[i] +=virusY_change[i]
            collision = collides(x,y,virusX[i],virusY[i])
            if collision:
                pop = mixer.Sound("pop.wav")
                pop.set_volume(0.1)
                pop.play()
                virusX[i] = random.randint(100,900)
                virusY[i] = -50
                score_value+=1
            if virusY[i]> 825:
                virusX[i] = random.randint(100,900)
                virusY[i] = -50
                lives -= 1
            if high_score < score_value:
                high_score = score_value
        # checks if you have any lives left
        if lives<0:
            game_over() # displays game over screen 
            #Shows the score
        show_score(scoreX,scoreY, score_value, high_score)
        show_lives(boardX,boardY+50, lives)
        # This updates the screen so we can see our rectangle
        pygame.display.update() # refresh screen
main_menu() #displays main menu
#End loop
pygame.quit()  # If we exit the loop this will execute and close our game
# music from https://www.youtube.com/watch?v=R0mKiSFPfdM
# sound effects from https://www.youtube.com/watch?v=3hPVv6boahw   &     https://www.youtube.com/watch?v=bug1b0fQS8Y
# white blood cell and virus from https://www.flaticon.com/
# background image from https://stock.adobe.com/promo/firstmonthfree?as_campaign=TinEye&as_content=promo&tduid=90ddef9477c753734f577ff77fc349ea&as_channel=affiliate&as_campclass=redirect&as_source=arvato
# font from https://www.dafont.com/naughty-cartoons.font