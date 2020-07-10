#sound issue:try to convert with audicity wav 16bit


if __name__=='__main__':        

    import pygame
    import os
    import random
    import math
    from pygame import mixer

    #getting address of resource folder
    current_path = os.path.dirname(__file__) # Where your .py file is located
    resource_path = os.path.join(current_path, 'resources') # The resource folder path
    image_path = os.path.join(resource_path, 'images') # The image folder path
    music_path= os.path.join(resource_path, 'music')
    count=0

    #initialize pygame
    pygame.init()#has to be added in every game

    game_start=False
    #introduction text
    introhead=pygame.font.Font("freesansbold.ttf",84)
    introbody=pygame.font.Font("freesansbold.ttf",26)
    def intro():
        head=introhead.render("Predator",True,(255,0,0))
        screen.blit(head,(50,100))
        body=introbody.render("you have to kill the space bugs and prevent there incursion",True,(255,255,255))
        screen.blit(body,(50,260))
        rulehead=introbody.render("RULES",True,(255,0,0))
        screen.blit(rulehead,(50,300))
        rulebody=introbody.render("don't let them cross the border and use 'space bar' to fire and 'arrow keys'",True,(255,255,255))
        screen.blit(rulebody,(50,340))
        rulebody2=introbody.render(" to navigate the ship and your ship must not get close to the bugs",True,(255,255,255))
        screen.blit(rulebody2,(50,400))
        rulebody3=introbody.render("if you miss then you have to wait until the previous bullet goes out of screen",True,(255,255,255))
        screen.blit(rulebody3,(50,450))
        
        startnote=introbody.render("press 'ENTER' key to start the game",True,(0,153,0))
        screen.blit(startnote,(100,550))
        

    #background music
    #pygame.mixer.music.load(os.path.join(music_path,"background.mp3"))
    #pygame.mixer.music.play(-1)

    laser=pygame.mixer.Sound(os.path.join(music_path,"laser.wav"))
    explosion=pygame.mixer.Sound(os.path.join(music_path,"explosion.wav"))
    #scoring
    score=0
    font=pygame.font.Font("freesansbold.ttf",32)
    fontx=10
    fonty=10

    def show_font(fontx,fonty):
        scoreval=font.render("score:"+str(score),True,(255,255,255))
        screen.blit(scoreval,(fontx,fonty))
        
    #gameover text
    overtext=pygame.font.Font("freesansbold.ttf",128)
    def gameover():

        text=overtext.render("GAME OVER",True,(255,255,255))
        screen.blit(text,(100,current_h/3))
    #    game_start=False
        
        



    #creating game screen
    #screeninfo = pygame.display.Info()#creates  information object containing of currenth and currentw
    current_w=1200
    current_h=700
    screen = pygame.display.set_mode((current_w-50,current_h))#screeninfo.current_w-50,screeninfo.current_h-100
    #print(screeninfo.current_w)
    #title bar
    pygame.display.set_caption("Predator")
    #title bar logo
    icon=pygame.image.load(os.path.join(image_path,'predator.png'))
    pygame.display.set_icon(icon)


    #background image
    background=pygame.image.load(os.path.join(image_path,"background.jpg"))
    background=pygame.transform.scale(background,(current_w,current_h))

    explosionimg=pygame.image.load(os.path.join(image_path,"explosion.png"))
    explosionimg=pygame.transform.scale(explosionimg,(50,50))

    crashimg=pygame.image.load(os.path.join(image_path,"crash.png"))
    crashimg=pygame.transform.scale(crashimg,(80,80))

    #player image
    xchange=0
    ychange=0
    x=(current_w/2)-70
    y=current_h-250
    mainimage=pygame.image.load(os.path.join(image_path,'ship.png'))
    def main_image(x,y):
        screen.blit(mainimage,(x,y))#blit function draw images 
        #(screeninfo.current_w/2)-70,screeninfo.current_h-250)

    #enemy
    enemy=pygame.image.load(os.path.join(image_path,"enemy1.png"))
    enemy=pygame.transform.scale(enemy,(50,50))
       
    enemyimg=[]
    enemyy=[]
    enemyx=[]
    num_of_enemy=10
    enemy_xchange=[]
    enemy_ychange=[]
    for i in range(num_of_enemy):
        
        enemyimg.append(enemy)
        #enemyimg.append(pygame.image.load(os.path.join(image_path,"enemy1.png")))
    #enemyimg[i]=pygame.transform.scale(enemyimg[i],(50,50))
        enemyx.append(random.randint(50,current_w-50)+random.randint(1,9))
        enemyy.append(random.randint(50,current_h-300)+random.randint(1,9))
        enemy_xchange.append(2)
        enemy_ychange.append(25)
    def enemy_image(enemyx,enemyy,i):
        
        screen.blit(enemyimg[i],(enemyx,enemyy))
        
        
    #bullet
    bullet=pygame.image.load(os.path.join(image_path,"bullet.png"))
    #bullet=pygame.transform.scale(enemy,(50,50))
    bulletx=0
    bullety=0
    bullet_ychange=5
    bullet_state="ready"#ready=u cant see the bullet on screen.fire=bullet is travelling on screen


    def bullet_fire(x,y):
        global bullet_state 
        bullet_state="fire"
        screen.blit(bullet,(x+17,y-15))     
        
    #collison detection function,we will use distance formula to find the distance between two objects
    def collison(x,y,x1,y1):
        distance=math.sqrt(math.pow((x-x1),2)+math.pow((y-y1),2))
        
        if distance<27:
            return True
        else:
            return False    

    def crash(x,y,x1,y1):
        distance=math.sqrt(math.pow((x-x1),2)+math.pow((y-y1),2))
        if distance<50:
            screen.blit(crashimg,(x,y))
            return True
        else:
            return False      

    #anything that you wnat to keep showing on the screen is tp be placed insides this loop

    #for keeping the screen as long as we dont press quit or close button


    running = True
    while running:#has to be added in every game
        
        if game_start:
            
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    running=False
                #for spaceship
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_LEFT:
                        xchange=-3        
                    if event.key==pygame.K_RIGHT:
                        xchange=3
                    if event.key==pygame.K_UP:
                        ychange=-3 
                    if event.key==pygame.K_DOWN:
                        ychange=3 
                #if event.type==pygame.KEYDOWN:    
                    if event.key==pygame.K_SPACE: #preparing bullet
                        if bullet_state=="ready":
                            bulletx=x
                            bullety=y
                            bullet_fire(bulletx,bullety)  
                        
                            laser.play()
                        
                if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        xchange=0        
                    if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                        ychange=0 
                
            #bullet movement 
                                
            #screen.fill((0,0,0))#rgb value
            screen.blit(background,(0,0))
            #space ship movement
            x=x+xchange
            y=y+ychange
            if x>current_w-120:
                x=current_w-120
            elif y>current_h-160:
                y=current_h-160
            elif x<5:
                x=5
            elif y<5:
                y=5              
                
                
            #enemy movement
            for i in range(num_of_enemy):
                crashed=crash(enemyx[i],enemyy[i],x+15,y+15)
                if crashed or enemyy[i]>current_h-250:
                    screen.blit(crashimg,(x,y))
                    x=2000
                    y=2000
                    if count==0:
                        explosion.play()
                        count=1 
                
                    for j in range(num_of_enemy):
                        enemyy[j]=2000
                    
                    gameover()
                    
                    
                
                enemyx[i]+=enemy_xchange[i]
                if enemyx[i]>current_w-120:
                    
                    enemyx[i]=current_w-120
                    enemy_xchange[i]=-1*(enemy_xchange[i])
                    enemyy[i]=enemyy[i]+enemy_ychange[i]
            
                elif enemyx[i]<5:
                    enemyx[i]=5
                    enemyy[i]=enemyy[i]+enemy_ychange[i]
                    enemy_xchange[i]=-1*enemy_xchange[i]
                elif enemyy[i]>current_h-200:
                    
                    enemy_image(enemyx[i],enemyy[i],i)
                        
                
                
                #collison detector
                enemyhit=collison(enemyx[i],enemyy[i],bulletx,bullety)
                if enemyhit:
                    explosion.play()
                    screen.blit(explosionimg,(bulletx,bullety))
                    bullety=y
                    bullet_state="ready"
                    score=score+1
                    
                    enemyx[i]=random.randint(50,current_w-50)
                    enemyy[i]=random.randint(50,current_h-400)
                enemy_image(enemyx[i],enemyy[i],i)     
        

            red=(0,0,255)            
            pygame.draw.line(screen,red,(0,current_h-200),(current_w-10,current_h-200))    
        
            main_image(x,y)
            
            #bullet movement
            if bullety<=0:
                bullety=y
                bullet_state="ready"
            if bullet_state=="fire":
                bullet_fire(bulletx,bullety)
                bullety=bullety-bullet_ychange
                #bullet_image(bulletx,bullety)
            show_font(fontx,fonty)  
        else:
            intro()
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    running=False
                #for spaceship
                if event.type==pygame.KEYDOWN:
                
                    if event.key==pygame.K_RETURN:
                        game_start=True
                        
                                
        pygame.display.update()       #has to be added in every pygame code 


