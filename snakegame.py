import pygame
import sys 
import os 
import random 
import math 
import turtle
import time
pygame.init()
pygame.display.set_caption(" snake game ")
pygame.font.init()
random.seed()

# we will declare global constant definition 
speed = 0.36 
SNAKE_SIZE  = 9 
APPLE_SIZE = SNAKE_SIZE
SEPARATION  = 10 
SCREEN_HEIGTH =800
SCREEN_WIDTH = 800 
FPS = 25 
KEY = { "UP" : 1  , "DOWN"  : 2 , "LEFT" : 3 , "RIGHT" : 4 }
# we will install screen 

screen = pygame.display.set_mode((   SCREEN_WIDTH , SCREEN_HEIGTH)  ,  pygame.HWSURFACE)

#we will ahve  used hw surface stands for hardware surface refers to using memory on  the video card for storing 
#draws as opposed to main memory 

# resources 
score_font = pygame.font.Font(None , 38)
score_numb_font = pygame.font.Font(None , 28)
game_over_font = pygame.font.Font(None , 48)
play_again_font = score_numb_font
score_mg = score_font.render(" score : " , 1 , pygame.Color("green"))
score_mg_size = score_font.size("score")

background_color =pygame.Color(0 , 0 , 0 )  # background of screen as black 
black = pygame.Color(0 , 0 , 0 )

# for clock at the left corner 

gameclock = pygame.time.Clock()


def checkcollision( posA , As , posB , Bs) :   # As is the size of a bs is the size of b 
    if ( posA.x + Bs and posA.x and posA.y < posB.y + Bs and posA.y + As > posB.y ) : 
        return True
    return False





def checkLimits(snake) : 
    if (snake.x > SCREEN_WIDTH) : 
        snake.x = SNAKE_SIZE
    if ( snake.x < 0 ) :
        snake.x =SCREEN_WIDTH - SNAKE_SIZE  
    if (snake.y > SCREEN_HEIGTH) : 
        snake.y = SNAKE_SIZE 
    if (snake.y < 0) : 
        snake.y = SCREEN_HEIGTH - SNAKE_SIZE 

# we will make class for food of the snake lets name it apple 

class Apple : 
    def __init__(self , x , y , state) :
        self.x = x 
        self.y = y 
        self.state = state 
        self.color = pygame.color.Color("orange") # color of food 
    def draw(self , screen )  :
        pygame.draw.rect(screen , self.color , (self.x , self.y , APPLE_SIZE , APPLE_SIZE ) , 0)


class segment : 
# initially snake will move in up direction
    def __init__(self , x , y ) : 
        self.x = x 
        self.y = y 
        self.direction = KEY["UP"]
        self.Color = "white"

class snake : 
    # initially snake will move in up direction
    def __init__(self , x , y ) : 
        self.x = x 
        self.y = y 
        self.direction = KEY["UP"]
        self.stack = []
        self.stack.append(self)
        blackbox = segment(self.x ,self.y + SEPARATION)
        blackbox.direction = KEY["UP"]
        blackbox.Color = "NULL"
        self.stack.append(blackbox)
# we will define moves of the snake 
    def move(self) : 
        last_element = len(self.stack) - 1 
        while (last_element != 0 ) : 
            self.stack[last_element].direction = self.stack[last_element].direction 
            self.stack[last_element].x = self.stack[last_element - 1 ].x 
            self.stack[last_element].y = self.stack[last_element - 1 ].y
            last_element-=1 
        if (len(self.stack) < 2) : 
            last_segment = self
        else : 
            last_segment = self.stack.pop(last_element)
        last_segment.direction = self.stack[0].direction 
        if (self.stack[0].direction == KEY["UP"]) :
            last_segment.y = self.stack[0].y - (speed * FPS)
        if (self.stack[0].direction == KEY["DOWN"]) :
            last_segment.y = self.stack[0].y + (speed * FPS)
        if (self.stack[0].direction == KEY["LEFT"]) :
            last_segment.x = self.stack[0].x  +  (speed * FPS)
        if (self.stack[0].direction == KEY["RIGHT"]) :
            last_segment.y = self.stack[0].x  + (speed * FPS)
        self.stack.insert(0 ,last_segment)

    def gethead(self) :   # head of snake 
        return(self.stack[0]) # it will be always 0 index 

# now when snake its food it will graw so far tha we will add that food to satck 
    def grow(self) : 
        last_element = len(self.stack) - 1 
        self.stack[last_element].direction = self.stack[last_element].direction
        if (self.stack[last_element].direction == KEY["UP"]) :
            newsegment = segment(self.stack[last_element].x , self.stack[last_element].y - SNAKE_SIZE)
            blackbox = segment(newsegment.x , newsegment.y + SEPARATION)


        elif (self.stack[last_element].direction == KEY["DOWN"]) :
            newsegment = segment(self.stack[last_element].x , self.stack[last_element].y + SNAKE_SIZE)
            blackbox = segment(newsegment.x , newsegment.y + SEPARATION)
        

        elif (self.stack[last_element].direction == KEY["LEFT"]) :
            newsegment = segment(self.stack[last_element].x -   SNAKE_SIZE , self.stack[last_element].y )
            blackbox = segment(newsegment.x - SEPARATION , newsegment.y )
        

        elif (self.stack[last_element].direction == KEY["RIGHT"]) :
            newsegment = segment(self.stack[last_element].x +   SNAKE_SIZE, self.stack[last_element].y - SNAKE_SIZE)
            blackbox = segment(newsegment.x + SEPARATION , newsegment.y )
        blackbox.color = "NULL"
        self.stack.append(newsegment)
        self.stack.append(blackbox)

    def iteratesegments ( self , delta) : 
        pass
    
    def setdirection(self , direction) : 
        if (self.direction == KEY["RIGHT"] and direction == KEY["LEFT"] or self.direction == KEY["LEFT"] and direction == KEY["RIGHT"]) :
            pass
        elif( self.direction == KEY["RIGHT"] and direction == KEY["DOWN"] or self.direction == KEY["UP"] and direction == KEY["DOWN"]) : 
            pass
        else  : 
            self.direction == direction


    def get_react(self) : # get the rectangle shape 
        rect= (self.x , self.y)
        return rect


    def getx(self) : 
        return self.x 
    

    def gety(self) : 
        return self.y
    
    def setx(self , x ) : 
        self.x= x 
    def sety(self , y ) : 
        self.y = y 
    # we will make the function of crashing when snake eats it self 

    def checkcrashing(self) : 
        counter = 1 
        while (counter < len(self.stack) - 1 ) : 
            if (checkcollision(self.stack[0], SNAKE_SIZE  , self.stack[counter] , SNAKE_SIZE) and self.stack[counter].color != "NULL")  : 
                return True
            counter +=1 
        return False
    
    #we will draw the snake 
    def draw(self , screen ) : 
        pygame.draw.rect(screen , pygame.Color("green" , (self.stack[0].x) , self.stack[0].y , SNAKE_SIZE , SNAKE_SIZE) , 0)
        counter = 1 
        while (counter < len(self.stack)) : 
            if (self.stack[counter].color == "NULL") :
                counter+=1 
            continue
        pygame.draw.rect(screen , pygame.color.Color("yellow") , (self.stack[counter].x , self.stack[counter].y , SNAKE_SIZE , SNAKE_SIZE)  , 0  )
        counter +=1 










# we will define keys 

def getkey() :
    for event in pygame.event.get() : 
        if event.type == pygame.KEYDOWN  : 
            if event.key == pygame.K_UP : 
                return KEY["UP"]
            elif event.key  == pygame.K_DOWN  : 
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT  : 
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT : 
                return KEY["RIGHT"]
            # for exit 
            elif event.key == pygame.K_ESCAPE : 
                return "exit"
            # if we t to continue playing again 
            elif event.key == pygame.K_y :
                return "YES" 
            # if dont want to play 
            elif event.key == pygame.K_n : 
                return "NO "
        if event.type == pygame.QUIT :
            sys.exit(0)


def  endgame () : 
    message = game_over_font.render(" GAME OVER " , 2 , pygame.Color("white"))
    message_play_again = play_again_font.render(" Play Again ? (T/N)" , 1 , pygame.Color("green"))
    screen.blit(message , (320 , 240))
    screen.blit(message_play_again,  ( 320 + 12 , 240 + 40 ))


    pygame.display.flip()
    pygame.display.update()


    mKey = getkey()
    while (mKey != "exit") : 
        if (mKey == "YES") : 
            main()
        elif (mKey == "NO") : 
            break
        mKey = getkey()
        gameclock.tick(FPS)
    sys.exit(0)


def drawScore(score): 
    score_numb =  score_numb_font.render(str(score) , 1 , pygame.Color("red"))
    screen.blit(score_mg , ( SCREEN_WIDTH - score_mg_size[0] - 60 , 10))
    screen.blit(score_numb , (SCREEN_WIDTH - 45  , 14))

def drawGameTime(gametime): 
    game_time = score_font.render("Time : " , 1 , pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(game_time/1000) , 1 , pygame.Color("white"))
    screen.blit(game_time , (30 , 10 ))
    screen.blit(game_time_numb , (105,14))

def exitscreen(): 
    pass

def respawnApple(apples , index , sx  , sy ) : 
    radius = math.sqrt ((SCREEN_WIDTH/2*SCREEN_WIDTH/2 + SCREEN_HEIGTH/2 *SCREEN_HEIGTH/2) ) / 2 
    angle = 999
    while(angle> radius) : 
        angle = random.uniform(0 , 800) * math.pi*2 
        x = SCREEN_WIDTH/2 + radius * math.cos(angle)
        y = SCREEN_HEIGTH / 2 + radius + math.sin(angle)
        if (x  == sx and y == sy ) : 
            continue 
    newApple = Apple( x, y , 1 )
    apples[index] = newApple 


def respawnApples( apples , quantity , sx ,sy ) :
    counter = 0 
    del apples[:]
    radius = math.sqrt((SCREEN_WIDTH/2*SCREEN_WIDTH/2 + SCREEN_HEIGTH/2*SCREEN_HEIGTH/2))/2
    angle = 999 
    while (counter< quantity) : 
        while (angle> radius) : 
            angle = random.uniform(0,800) * math.pi*2 
            x = SCREEN_WIDTH/2 + radius *  math.cos(angle)
            y = SCREEN_HEIGTH/2 + radius *  math.sin(angle)
            if ( x- APPLE_SIZE == sx or x + APPLE_SIZE == sx) and  ( y - APPLE_SIZE ==  sy or y + APPLE_SIZE == sy  or radius - angle <= 10 ) :
                continue
        apples.append(Apple(x , y , 1 ))
        angle = 999 
        counter +=1 
        




def main(): 
    score = 0
# initialisation of snake 




    mysnake = snake (SCREEN_WIDTH/2 ,  SCREEN_HEIGTH/2)
    mysnake.setdirection( KEY["UP"])
    mysnake.move()
    start_segments = 3  # initially we will be having 3 segmenet long snake 
    while (start_segments > 0) : 
        mysnake.grow()
        mysnake.move()
        start_segments -=1 



    # food 
    max_apples = 1 # 1 apple when snak eeats 
    eaten_apple = False # as snake will eat food aplle will be disappear 
    apples = [ Apple( random.randint(60 , SCREEN_WIDTH) ,random.randint(60 , SCREEN_HEIGTH) , 1 )]
    respawnApples(apples , max_apples , mysnake.x , mysnake.y) 



    starttime = pygame.time.get_ticks()
    endgame = 0

    while (endgame !=1 ) : 
        gameclock.tick(FPS)


        # input 
        keypress =  getkey 
        if keypress == "exit" : 
            endgame = 1 


        # to check collision 
        checkLimits(mysnake)
        if (mysnake.checkcrashing() == True) :
            endgame()


    for myApple in apples : 
        if ( myApple.state == 1 ) : 
            if (checkcollision(mysnake.gethead() , SNAKE_SIZE , myApple , APPLE_SIZE) == True) :
                mysnake.grow()
                myApple.state = 0 
                score += 10
                eaten_apple = True



            # update positon 
            if (keypress) : 
                mysnake.setdirection(keypress) 
            mysnake.move()


            # respawning food 
            if (eaten_apple == True) : 
                eaten_apple = False
                respawnApple( apples , 0 , mysnake.gethead().x  , mysnake.gethead().y)


            screen.fill(background_color)
            for myApple in apples : 
                if (myApple.state == 1 ) : 
                    myApple.draw(screen)


            mysnake.draw(screen)
            drawScore(score)
            gametime = pygame.time.get_ticks() - starttime
            drawGameTime(gametime)
            pygame.display.flip()
            pygame.display.update()



main()







