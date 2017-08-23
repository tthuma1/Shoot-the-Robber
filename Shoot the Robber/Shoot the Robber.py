import pygame
import time
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
green = (0,200,0)
orange = (255,125,0)
yellow = (255,255,0)

bright_red = (255,0,0)
bright_orange = (255,180,0)
bright_green = (0,255,0)
dark_yellow = (200,200,0)

display_width = 800
display_height = 600

react_time = -100

largeText = pygame.font.SysFont("playbill",155)
mediumText = pygame.font.SysFont("playbill",42)
mediumText2 = pygame.font.SysFont("playbill",115)
smallText = pygame.font.SysFont("playbill",31)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Wild West")
clock = pygame.time.Clock()

shoot_sound = pygame.mixer.Sound("Gun_Shoot.wav")
kill_sound = pygame.mixer.Sound("Death_Yell.wav")
kill_sound2 = pygame.mixer.Sound("Death_Yell2.wav")
too_fast_sound = pygame.mixer.Sound("Too_Fast.wav")
clapping_sound = pygame.mixer.Sound("Clapping.wav")
pygame.mixer.music.load("Game_Music.wav")

pygame.mixer.music.play(-1)

bgImg = pygame.image.load("background.png")
bgImg1 = pygame.image.load("background1.png")
robbulImg = pygame.image.load("robbul.png")
sherbulImg = pygame.image.load("sherbul.png")
badgeImg = pygame.image.load("sheriff badge.png")
bloodImg = pygame.image.load("blood.png")
gameIcon = pygame.image.load("game icon.png")

pygame.display.set_icon(gameIcon)

def text_objects(text,font,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    global react_time
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            if msg == "Home":
                react_time = -100
            pygame.mixer.music.unpause()
            action()

    else:
        pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

    TextSurf, TextRect= text_objects(msg,smallText,black)
    TextRect.center = ((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurf,TextRect)

def how_to_play():
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                
        gameDisplay.blit(bgImg,(0,0))
        TextSurf, TextRect = text_objects("Wild West",largeText,black)
        TextRect.center = ((display_width/2),100)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("You are Sheriff in the Wild West.",mediumText,black) 
        TextRect.center = ((display_width/2),175)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("A robber robbed a bank so now you need to shoot him.",mediumText,black)
        TextRect.center = ((display_width/2),210)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("When a countdown on screen reaches 0 press Space to shoot the robber.",mediumText,black)
        TextRect.center = ((display_width/2),245)
        gameDisplay.blit(TextSurf, TextRect)        

        TextSurf, TextRect = text_objects("In the upper left corner is the react time that you need to beat him,",mediumText,black)
        TextRect.center = ((display_width/2),280)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("and in the upper right corner is the react time you had this round.",mediumText,black)
        TextRect.center = ((display_width/2),315)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("With every shoot the react time needed is shorter.",mediumText,black)
        TextRect.center = ((display_width/2),350)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("If you stay alive long enough, you will save the city.",mediumText,black)
        TextRect.center = ((display_width/2),385)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Good luck.",mediumText,black)
        TextRect.center = ((display_width/2),420)
        gameDisplay.blit(TextSurf, TextRect)
        
        button("Play",200,500,100,50,green,bright_green,game_loop)
        button("Back",500,500,100,50,dark_yellow,yellow,game_intro)

        pygame.display.update()
        clock.tick(15)
        
def quit_game():
    pygame.quit()
    quit()
    
def blit_text(text):
    TextSurf, TextRect = text_objects(text,largeText,black)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(1)

def blit_text2(msg,speed,x,y):
    font = pygame.font.SysFont("playbill", 35)
    text = font.render(msg+str(speed), True, black)
    gameDisplay.blit(text, (x,y))

def rob(x,y):
    gameDisplay.blit(robImg,(x,y))

def sher(x,y):
    gameDisplay.blit(sherImg,(x,y))

def win():

    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(kill_sound)
    
    TextSurf, TextRect = text_objects("You Won The Round", mediumText2, black)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        button("Next Round",200,400,100,50,green,bright_green,game_loop)
        button("Home",500,400,100,50,dark_yellow,yellow,game_intro)

        pygame.display.update()
        clock.tick(15)
        
def lose():

    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(kill_sound)

    TextSurf, TextRect = text_objects("You Lost", largeText, black)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        button("New Game",200,400,100,50,green,bright_green,game_loop)
        button("Home",500,400,100,50,dark_yellow,yellow,game_intro)

        pygame.display.update()
        clock.tick(15)

def draw():

    pygame.mixer.music.pause()
    pygame.mixer.Sound.play(kill_sound2)

    TextSurf, TextRect = text_objects("Draw", largeText, black)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    TextSurf, TextRect = text_objects("You both died", mediumText, yellow)
    TextRect.center = ((display_width/2),(display_height/2)+75)
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        button("New Game",200,400,100,50,green,bright_green,game_loop)
        button("Home",500,400,100,50,dark_yellow,yellow,game_intro)

        pygame.display.update()
        clock.tick(15)

def too_fast():
    pygame.mixer.Sound.play(too_fast_sound)

    TextSurf, TextRect = text_objects("You Shooted Too Fast", mediumText2, black)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    
    TextSurf, TextRect = text_objects("You automaticly lost because of cheating", mediumText, yellow)
    TextRect.center = ((display_width/2),(display_height/2)+75)
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        button("New Game",200,400,100,50,green,bright_green,game_loop)
        button("Home",500,400,100,50,dark_yellow,yellow,game_intro)

        pygame.display.update()
        clock.tick(15)


def victory():

    pygame.mixer.Sound.play(kill_sound)

    stopping = 0

    TextSurf, TextRect = text_objects("WOAH!", largeText, black)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    final_win()
                
        button("Next",350,400,100,50,green,bright_green,final_win)

        stopping += 1

        if stopping == 2:

            time.sleep(1)

            TextSurf, TextRect = text_objects("You did it!!!", mediumText, yellow)
            TextRect.center = ((display_width/2),(display_height/2)+75)
            gameDisplay.blit(TextSurf, TextRect)
            
        pygame.display.update()
        clock.tick(15)

def final_win():
    pygame.mixer.Sound.play(clapping_sound)
    pygame.mixer.music.unpause()

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_intro()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                
        gameDisplay.blit(bgImg,(0,0))
        TextSurf, TextRect = text_objects("Wild West",largeText,black)
        TextRect.center = ((display_width/2),100)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Congratulations, you beated the robber.",mediumText,black) 
        TextRect.center = ((display_width/2),175)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("And you made it through the game.",mediumText,black)
        TextRect.center = ((display_width/2),210)
        gameDisplay.blit(TextSurf, TextRect)

        TextSurf, TextRect = text_objects("Here\'s a new badge for doing such a great work.",mediumText,black)
        TextRect.center = ((display_width/2),245)
        gameDisplay.blit(TextSurf, TextRect)
        
        gameDisplay.blit(badgeImg,((display_width/2-105),270))
        
        button("Home",350,520,100,50,green,bright_green,game_intro)

        pygame.display.update()
        clock.tick(15)
    
def game_intro():
    intro = True
    
    while intro:    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        gameDisplay.blit(bgImg,(0,0))
        TextSurf, TextRect = text_objects("Wild West",largeText,black)
        TextRect.center = ((display_width/2),100)
        gameDisplay.blit(TextSurf, TextRect)

        button("Play",150,450,100,50,green,bright_green,game_loop)
        button("How To Play",350,450,100,50,dark_yellow,yellow,how_to_play)
        button("Quit",550,450,100,50,red,bright_red,quit_game)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    pygame.mixer.music.unpause()
    global react_time

    frame_count = 0
    frame_count2 = 0
    frame_count3 = 0
    
    frame_rate = 60
    
    start_time = 3
    start_time2 = 300
    
    old_react_time = react_time
    
    stop_count = 0
    plus_react_time = 0
    stop_sound = 0
    stop_sound2 = 0

    total_seconds3 = 0
    
    robbulx = 140
    bullet_changer = 0
    bullet_changes = 0
    sherbulx = 655

    shoot_er1 = 0
    shoot_er2 = 0
    
    game = True
    while game:
        gameDisplay.blit(bgImg1,(0,0))
        if shoot_er1 == 1:
            gameDisplay.blit(sherbulImg,(sherbulx,475))
        if shoot_er2 == 1:
            gameDisplay.blit(robbulImg,(robbulx,470))            
        #bullet(robbulx,470,sherbulx,475)

        #countdown
        total_seconds = start_time - (frame_count // frame_rate)
        #total_seconds2 = 0 - (frame_count2 // frame_rate)
        #print(total_seconds2)

        
        if total_seconds <= 0:
            total_seconds = 0
            total_seconds2 = start_time2 - (frame_count2 // frame_rate)
            #print(total_seconds2)
            total_seconds3 = start_time2 - (frame_count3 // frame_rate)
            #print(total_seconds2)
            if plus_react_time == 0:
                plus_react_time = 1
                old_react_time = react_time
                react_time += random.randrange(10,14)
            elif react_time > -3:
                react_time = -3
                
                #print(total_seconds2)
                total_seconds2 = 100
            if old_react_time <= -13 and total_seconds2 <= react_time-12:
                if stop_sound2 == 0:
                    pygame.mixer.Sound.play(shoot_sound)
                    pygame.mixer.music.pause()
                    stop_sound2 = 1
                    shoot_er2 = 1
                #print("abcdefg")
                #time.sleep(0.5)
                #sherbulx -= 10
                robbulx += 10
            elif old_react_time <= -8 and old_react_time >= -12 and total_seconds2 <= react_time-7:
                if stop_sound2 == 0:
                    pygame.mixer.Sound.play(shoot_sound)
                    pygame.mixer.music.pause()
                    stop_sound2 = 1
                    shoot_er2 = 1
                #print("123456789")
                #print(react_time)
                #time.sleep(0.5)
                #sherbulx -= 10
                robbulx += 10
            elif old_react_time >= -7  and total_seconds2 <= react_time-2:
                if stop_sound2 == 0:
                    pygame.mixer.Sound.play(shoot_sound)
                    pygame.mixer.music.pause()
                    stop_sound2 = 1
                    shoot_er2 = 1
                #print("a1b2c3d4")
                #print(react_time)
                #time.sleep(0.5)
                #sherbulx -= 10
                robbulx += 10

        output_string = "{0}".format(total_seconds)

        TextSurf, TextRect = text_objects(output_string,largeText,black)
        TextRect.center = ((display_width/2),150)
        gameDisplay.blit(TextSurf, TextRect)
        #countdown
        blit_text2("React time needed: ","{0}.{1:02} sec".format(abs(old_react_time)//100,abs(old_react_time)%100),0,0)
        blit_text2("Your react time: ","{0}.{1:02} sec".format(abs(total_seconds3)//100,abs(total_seconds3)%100),567,0)

        frame_count += 1
        frame_count2 += 100
        if stop_count != 1:
            frame_count3 += 100

        robbulx +=bullet_changer
        sherbulx -= bullet_changes

        if robbulx >= 720 and sherbulx > 75:
            #print(react_time)
            react_time = -100
            #print(sherbulx)
            gameDisplay.blit(bloodImg,(715,450))
            
            lose()
            game_loop()
            
        elif robbulx < 720 and sherbulx <= 75:
            gameDisplay.blit(bloodImg,(65,464))
            if old_react_time >= -3:
                victory()
            else:
                #gameDisplay.blit(bloodImg,(66,283))
            
                win()

        elif robbulx >= 720 and sherbulx <= 75:
            react_time = -100
            
            gameDisplay.blit(bloodImg,(65,464))
            gameDisplay.blit(bloodImg,(715,450))
            draw()
            game_loop()

            

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not total_seconds <= 0:
                    pygame.mixer.music.pause()
                    react_time = -100
                    #blit_text("Too Fast")
                    too_fast()
                elif event.key == pygame.K_SPACE:
                    shoot_er1 = 1
                    stop_count = 1
                    bullet_changes = 10
                    if stop_sound == 0:
                        stop_sound = 1
                        pygame.mixer.Sound.play(shoot_sound)
                        pygame.mixer.music.pause()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                        
        pygame.display.update()
        clock.tick(frame_rate)

game_intro()
pygame.quit()
quit()
