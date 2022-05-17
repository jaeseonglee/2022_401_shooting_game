# +
# 220516
import pygame
import sys
import random
from time import sleep
from pygame.locals import QUIT,Rect

padWidth = 440       # 480                              # 게임화면의 가로크기
padHeight = 780      # 640                              # 게임화면의 세로크기
explosionSound = ['explosion01.wav','explosion02.wav','explosion03.wav','explosion04.wav']
numberImage = ['0.png','1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png']
start_img = pygame.image.load('start.png')              # 시작 버튼
explane_img = pygame.image.load('explane.png')          # 조작 설명 버튼
exit_img = pygame.image.load('exit.png')                # 종료 버튼
option_img = pygame.image.load('option.png')            # 옵션 버튼
die_home_img = pygame.image.load('home.png')            # 죽은 화면에서 메인
die_again_img = pygame.image.load('again.png')          # 죽은 화면에서 다시 시작
keyboard_img = pygame.image.load('keyboard.png')        # 설명 이미지
background = pygame.image.load('background.jpeg')       # 게임 배경
background22 = pygame.image.load('background22.jpeg')   # 게임 배경
background33 = pygame.image.load('background33.png')    # 게임 배경
mainbackground = pygame.image.load('mainbackground.png')# 메인배경
winbackground = pygame.image.load('winbackground.jpg')  # 승리시 배경
backspace_img = pygame.image.load('back.png') #뒤로가기 
explane_start_img = pygame.image.load('start.png') #설명창에서 게임시작
bonobono_img = pygame.image.load('bonobono.png') #나레이션 보노보노 얼굴
porori_img = pygame.image.load('porori.png')
textbox_img = pygame.image.load('textbox.png') #텍스트박스
spacebar_img = pygame.image.load('spacebar.png') #스페이스바
nuguriboss_img = pygame.image.load('nuguriboss.png') 
win_img = pygame.image.load('win.png') 
lose_img = pygame.image.load('lose.png') 

#이미지 크기조절
winbackground = pygame.transform.scale(winbackground, (480, 820))
background33 = pygame.transform.scale(background33, (480, 820))
start_img = pygame.transform.scale(start_img, (150,50))
option_img = pygame.transform.scale(option_img, (150,50))
explane_img = pygame.transform.scale(explane_img, (150,50))
exit_img = pygame.transform.scale(exit_img, (150,50))
die_home_img = pygame.transform.scale(die_home_img, (150,50))
die_again_img = pygame.transform.scale(die_again_img, (150,50))
spacebar_img = pygame.transform.scale(spacebar_img, (150,100))
textbox_img = pygame.transform.scale(textbox_img, (440,250))
porori_img = pygame.transform.scale(porori_img, (100,150))
bonobono_img = pygame.transform.scale(bonobono_img, (100,150))
nuguriboss_img = pygame.transform.scale(nuguriboss_img, (100,150))
keyboard_img = pygame.transform.scale(keyboard_img, (150, 130))
backspace_img = pygame.transform.scale(backspace_img, (150, 40))
win_img = pygame.transform.scale(win_img, (300, 230))
lose_img = pygame.transform.scale(lose_img, (300, 230))

screen = pygame.display.set_mode((padWidth, padHeight))

FPSCLOCK = pygame.time.Clock()  

num = 1 # 볼륨 초기값

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False
        
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
        return action

start_button = Button(140, 250, start_img, 1.2)
explane_button = Button(140, 330, explane_img, 1.2)
option_button = Button(140, 390, option_img, 1.2)
exit_button = Button(140, 460, exit_img, 1.2)
back_button = Button(10, 10, backspace_img, 1.2)
start_explane_button = Button(280, 10, start_img, 1.0)
die_again_button = Button(250, 330, die_again_img, 1.2)
die_home_button = Button(30, 330, die_home_img, 1.2)

def mainscreen():  #메인화면
    run = True
    initGame()
    while run :
        screen.blit(mainbackground,(-140, -150))
        
        if start_button.draw():
            #runGame()
            nar1()
        if explane_button.draw():
            explanescreen()
        if option_button.draw():
            option()
        if exit_button.draw():  #종료하기 눌렀을 때 종료
            pygame.quit()  
            sys.exit()
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT :  #종료
                run = False
        pygame.display.update()  #반복할 때마다 업데이트

def explanescreen():   #조작설명화면
    myfont = pygame.font.Font('CookieRun Black.ttf',20)
    message1 = myfont.render("좌 우 위 아래 이동",True,(0,0,0))
    myfont = pygame.font.Font('CookieRun Black.ttf',20)
    message2 = myfont.render("공격하기",True,(0,0,0))

    running = True # 게임이 진행중인지 확인하기
    while running:
        screen.blit(mainbackground, (-140, -150))
        screen.blit(keyboard_img, (20, 100)) #조작설명
        screen.blit(spacebar_img, (20, 300)) #조작설명
        
        
        if back_button.draw():
            mainscreen()
        if start_explane_button.draw():
            nar1()        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT :  #종료
                run = False
        
        screen.blit(message1, (260, 130))
        screen.blit(message2, (300, 330))     
        pygame.display.update() 

def option():   #조작설명화면
    global num 
    running = True # 게임이 진행중인지 확인하기
    while running:
        screen.blit(mainbackground, (-140, -150))
    
        
        number = pygame.image.load(numberImage[num]) # 숫자 이미지 파일
        numberSize = number.get_rect().size # 숫자 크기
        numberX = numberSize[0]
        numberY = numberSize[1]
        numBot = Button(130, 150, number, 1.0) # 숫자 버튼
        
        drawObject(valume, 10, 150) # 볼륨 그리기
        
        if back_button.draw():
            mainscreen()
        if start_explane_button.draw():
            nar1()
        if numBot.draw(): # 볼륨 조절
            num += 1
            if num == 10:
                num = 0
            pygame.mixer.music.set_volume(0.1*num)
            sleep(0.3)
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT :  #종료
                run = False
        
        pygame.display.update()     

    

def die():  #죽었을 때 화면
    
    running = True # 게임이 진행중인지 확인하기
    while running:

        screen.blit(background33, (0, 0)) 
        
        if  die_again_button.draw():
            runGame() 
        if die_home_button.draw():
            mainscreen()
           
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT :  # 종료
                run = False
                
                
        screen.blit(lose_img, (80, 100))      
        FPSCLOCK.tick(30)    
        pygame.display.update() 
        
        
        


def clear():
    running = True
    while running:
        screen.blit(winbackground, (0,0))
        
        
        if die_again_button.draw():
            runGame()
        if die_home_button.draw():
            mainscreen()
            sleep(1)
        
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT :  #종료
                run = False
                
        screen.blit(win_img, (105, 180)) 
        pygame.display.update() 
         


def writeClear(text):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 50)
    text = font.render(str(text), True, (0,0,0))
    gamePad.blit(text,(padWidth/2,padHeight/3))





def nar1():
    myfont = pygame.font.Font('CookieRun Black.ttf',20)
    message1 = myfont.render("포로리야~ 놀자~",True,(255,255,255))
    message2 = myfont.render("TAB",True,(255,255,255))
    
    while True:
        screen.blit(mainbackground,(0,0)) #background 의 화면을 스크린에 복사 
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_TAB: # 전투기 왼쪽으로 이동       
                    nar2()
                    
        screen.blit(textbox_img, (0, 540))           
        screen.blit(bonobono_img, (10, 580))           
        screen.blit(message1, (100, 580))
        screen.blit(message2, (340, 715))
        pygame.display.update()
        FPSCLOCK.tick(30)           

def nar2():
    myfont = pygame.font.Font('CookieRun Black.ttf',20)
    message1 = myfont.render("(으아ㅏㅏㅏㅏㅏㅏㅅ!!)",True,(255,255,255))
    message2 = myfont.render("TAB",True,(255,255,255))
    
    while True:
        screen.blit(mainbackground,(0,0)) #background 의 화면을 스크린에 복사 
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_TAB: # 전투기 왼쪽으로 이동       
                    nar3()
                    
        screen.blit(textbox_img, (0, 540))
        screen.blit(porori_img, (10, 580))           
        screen.blit(message1, (100, 580))
        screen.blit(message2, (340, 715))
        pygame.display.update()
        FPSCLOCK.tick(30)           



def nar3():
    myfont = pygame.font.Font('CookieRun Black.ttf',20)
    message1 = myfont.render("무슨 일이야!!",True,(255,255,255))
    message2 = myfont.render("TAB",True,(255,255,255))
    
    while True:
        screen.blit(mainbackground,(0,0)) #background 의 화면을 스크린에 복사 
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_TAB: # 전투기 왼쪽으로 이동       
                    nar4()
                    
                    
        screen.blit(textbox_img, (0, 540))           
        screen.blit(bonobono_img, (10, 580))           
        screen.blit(message1, (100, 580))
        screen.blit(message2, (340, 715))
        pygame.display.update()
        FPSCLOCK.tick(30)  

def nar4():
    myfont = pygame.font.Font('CookieRun Black.ttf',20)
    message1 = myfont.render("살려…ㅈ……",True,(255,255,255))
    message2 = myfont.render("TAB",True,(255,255,255))
    
    while True:
        screen.blit(mainbackground,(0,0)) #background 의 화면을 스크린에 복사 
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_TAB: # 전투기 왼쪽으로 이동       
                    nar5()
                    
                    
        screen.blit(textbox_img, (0, 540))           
        screen.blit(porori_img, (10, 580))           
        screen.blit(message1, (100, 580))
        screen.blit(message2, (340, 715))
        pygame.display.update()
        FPSCLOCK.tick(30)    

def nar5():

    myfont = pygame.font.Font('CookieRun Black.ttf',40)
    message1 = myfont.render("포로리를 구출하세요",True,(255, 255, 255))
    message2 = myfont.render("  GAME START",True,(255,255,255))
    
    while True:
        
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            pygame.time.delay(2000)   
            runGame()
            
               
        screen.blit(background22,(-60,-40)) #background 의 화면을 스크린에 복사             
        screen.blit(message1, (80, 200))
        screen.blit(message2, (80, 250))
        pygame.display.update()
        FPSCLOCK.tick(30)          

        


        
def bossdie():
    myfont = pygame.font.Font('CookieRun Black.ttf',20)
    message1 = myfont.render("보노보노 대단해...포로리를 풀어주겠어",True,(255,255,255))
    message2 = myfont.render("TAB",True,(255,255,255))
    
    while True:
        screen.blit(mainbackground,(0,0)) #background 의 화면을 스크린에 복사 
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            #pygame.time.sleep(2000)   
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_TAB: 
                    #pygame.time.delay(2000) 
                    clear()
                    
                    
                    
        screen.blit(textbox_img, (0, 540))           
        screen.blit(nuguriboss_img, (10, 580))           
        screen.blit(message1, (100, 580))
        screen.blit(message2, (340, 715))
        pygame.display.update()
        FPSCLOCK.tick(30)        
        
        
        
def bosswin():
    myfont = pygame.font.Font('CookieRun Black.ttf',20)
    message1 = myfont.render("보노보노 상대가 안되는구만",True,(255,255,255))
    message2 = myfont.render("TAB",True,(255,255,255))
    
    while True:
        screen.blit(mainbackground,(0,0)) #background 의 화면을 스크린에 복사 
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            #pygame.time.sleep(2000)   
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_TAB: # 전투기 왼쪽으로 이동       
                    die()
                    
                    
                    
        screen.blit(textbox_img, (0, 540))           
        screen.blit(nuguriboss_img, (10, 580))           
        screen.blit(message1, (100, 580))
        screen.blit(message2, (340, 715))
        pygame.display.update()
        FPSCLOCK.tick(30)        

        
        
        

# 게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x,y))

# 운석을 맞춘 점수 계산
def writeScore(count):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('Score:' + str(count), True, (0,0,0))
    gamePad.blit(text,(10,0))

# 레벨 메세지 출
def writeLevel(level):
    global gamePad
    font = pygame.font.Font('NanumGothic.ttf', 20)
    text = font.render('level:' + str(level), True, (0,0,0))
    gamePad.blit(text,(10,30))

# 게임 메시지 출력
def writeMessage(text):
    global gamePad, gameOverSound
    textfont = pygame.font.Font('NanumGothic.ttf', 80)
    text = textfont.render(text, True, (255,0,0))
    textpos = text.get_rect()
    textpos.center = (padWidth/2 , padHeight/2)
    gamePad.blit(text, textpos)
    pygame.display.update()
    pygame.mixer.music.stop()  #  배경 음악 정지
    gameOverSound.play()  # 게임 오버 사운드 재생
    pygame.mixer.music.play(-1) # 배경 음악 재생
    runGame()

def initGame():
    global gamePad, clock, background1, background2, fighter,rock, missile, explosion, missileSound,\
        gameOverSound, heart, item, valume, num, boss, boss_attack, explosion, power
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')            # 게임이름
    background1 = pygame.image.load('background.jpeg')  # 배경 그림
    background1 = pygame.transform.scale(background1, (padWidth, padHeight))
    
    
    background2 = background1.copy()                    # 배경 2
    background2 = pygame.transform.flip(background2, 0,180)
    
    fighter = pygame.image.load('fighter.png')          # 전투기 그림
    rock = pygame.image.load('nuguri.png')              # 운석 그림
    missile = pygame.image.load('missile.png')          # 미사일 그림
    explosion = pygame.image.load('explosion.png')      # 폭발 그림
    heart = pygame.image.load('heart.png')              # 하트 그림
    item = pygame.image.load('Super.png')               # 아이템 그림
    valume = pygame.image.load('valume.png')            # 볼륨 그림
    power = pygame.image.load('power.png')              # 필살기 가능 그림
    pygame.mixer.music.load('music.wav')                # 배경 음악
    pygame.mixer.music.play(-1)                         # 배경 음악 재생
    pygame.mixer.music.set_volume(0.1*num)              # 배경 음악 볼륨 조절
    missileSound = pygame.mixer.Sound('missile.wav')    # 미사일 사운드
    missileSound.set_volume(0.1*num)                    # 미사일 사운드 볼륨 조절
    gameOverSound = pygame.mixer.Sound('gameover.wav')  # 게임 오버 사운드
    gameOverSound.set_volume(0.1*num)                   # 게임 오버 볼륨 조절
    clock = pygame.time.Clock()
    
    
    
    boss = pygame.image.load('./boss.png')
    boss = pygame.transform.scale(boss,(padWidth / 5.0 , padHeight / 10.0))
    boss_attack = pygame.image.load('./temp.png')
    boss_attack = pygame.transform.scale(boss_attack,(36, 36))

def runGame():
    global gamePad, clock, background1, backgroud2, fighter,rock, missile, explosion, missileSound, heart, item, num, boss, boss_attack, explosion, power
    
    isShot = False
    shotCount = 0
    level = 1
    SuperCount = 0
    
    # 백그라운드 Y 위치
    backgroud1_y = 0
    backgroud2_y = -padHeight
    
    # 무기 좌표 리스트
    missileXY = []
    
    # 하트 좌표 리스트
    #heartXY = [[padWidth - 50 , 5],[padWidth - 100 , 5],[padWidth - 150 , 5],[padWidth - 200 , 5],[padWidth - 250 , 5]]
    heartXY = [[padWidth - 50 , 5],[padWidth - 50 , 55],[padWidth - 50 , 105],[padWidth - 50 , 155],[padWidth - 50 , 205]]

    destroySound = pygame.mixer.Sound(random.choice(explosionSound))
    destroySound.set_volume(0.1*num)
    
    # 운석 랜덤 생성
    rockSize = rock.get_rect().size # 운석 크기
    rockWidth = rockSize[0]
    rockHeight = rockSize[1]
    
    # 운석 초기 위치 설정
    rockX = random.randrange(0, padWidth - rockWidth)
    rockY = 0
    rockSpeed = 2
    
    # 운석 좌표 리스트
    rockXY = []

    # 운석
    rockCount = 0

    # 전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]
    
    # 전투기 초기 위치
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0
    fighterY = 0
    
    # 하트 크기
    heartSize = heart.get_rect().size
    heartWidth = heartSize[0]
    heartHeight = heartSize[1]
    
    # 하트 카운트 1
    def heartCount(count):
        heartXY.remove(heartXY[count])
    # 하트 카운트 2
    count = 4
    
    # 아이템 
    itemSize = item.get_rect().size
    itemWidth = itemSize[0]
    itemHeight = itemSize[1]
    itemXY = []
    itemCount = 0
    
    #########################
    # 보스 이미지 변수
    bossHP = 150
    boss_image_Size = boss.get_rect().size
    boss_Width = boss_image_Size[0]
    boss_Height = boss_image_Size[1]
    bossX = boss_Width * 2
    bossY = -boss_Height
    
    boss_image = False
    boss_x_cnt = 0
    boss_move_r = True
    
    
    # 보스 공격 변수  
    boss_attack_startX = padWidth / 2.0
    boss_attack_startY = 50
    boss_attackX = boss_attack_startX
    boss_attackY = boss_attack_startY
    boss_attackXY = []

    boss_attack_Size = boss_attack.get_rect().size
    boss_attack_Width = boss_attack_Size[0]
    boss_attack_Height = boss_attack_Size[1]
    
    boss_attack_pattern = 0
    boss_attack_cnt = 0
    boss_attack_speed = 3
    boss_now = False
    
    #######################
    
    
    
    
    
    # 아이템 생성
    def tempItem():
        itemXY.append([random.randrange(0, padWidth - itemWidth),random.randrange(padHeight/2, padHeight - itemHeight)])

    onGame = False
    while not onGame:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]: # 게임 프로그램 종료
                pygame.quit()
                sys.exit()
            if event.type in [pygame.KEYDOWN]:
                if event.key == pygame.K_LEFT: # 전투기 왼쪽으로 이동
                    fighterX -= 5
                
                elif event.key == pygame.K_RIGHT: # 전투기 오른쪽으로 이동
                    fighterX += 5
                    
                elif event.key == pygame.K_UP: # 전투기 위쪽으로 이동
                    fighterY -= 5
                    
                elif event.key == pygame.K_DOWN: # 전투기 아래쪽으로 이동
                    fighterY += 5
                    
                elif event.key == pygame.K_ESCAPE: # ESC 누를시 메뉴
                    die()
                    
                elif event.key == pygame.K_SPACE: # 미사일 발사
                    missileSound.play()  # 미사일 사운드 재생
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight/3
                    missileXY.append([missileX,missileY])
                
                elif event.key == pygame.K_z: # 필살기
                    if SuperCount >= 10:
                        missileSound.play()
                        for i in range(30):
                            missileXY.append([random.randrange(0, padWidth - fighterWidth),random.randrange(0, padHeight - 31)])
                        SuperCount -= 10
                
            if event.type in [pygame.KEYUP]: # 방향키를 떼면 전투기 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    fighterY = 0
        
        # 배경 화면 그리기
        backgroud1_y += 2
        backgroud2_y += 2      

        if backgroud1_y == padHeight:
            backgroud1_y = -padHeight
        
        
        if backgroud2_y == padHeight:
            backgroud2_y = -padHeight
            
        
        drawObject(background1, 0, backgroud1_y) 
        drawObject(background2, 0, backgroud2_y)
        
        if SuperCount >= 10:
            drawObject(power, 30, 700)
            SuperCount = 10
        
        # 점수에 따라 운석 추가
        
        if shotCount < 10:
            rockCount += 1
            level = 1
        elif shotCount < 20:
            rockCount += 1.1
            level = 2
        elif shotCount < 30:
            rockCount += 1.3
            level = 3
        elif shotCount < 40:
            rockCount += 1.5
            level = 4
        elif shotCount < 50:
            rockCount += 1.7
            level = 5
        elif shotCount < 60:
            rockCount += 1.9
            level = 6
        elif shotCount < 70:
            rockCount += 2.1
            level = 7
        elif shotCount < 80:
            rockCount += 2.3
            level = 8
        elif shotCount < 90:
            rockCount += 2.4
            level = 9
        else:
            level = 10

        ############## 변경점
        if level >= 10 and not boss_now  :
            boss_now = True
            rockXY = []
        
        
        
        if rockCount > 59 and not boss_now   :
            rockX = random.randrange(0, padWidth - rockWidth)
            rockXY.append([rockX,rockY])
            rockCount = 0 
            itemCount += 1
        
        ##########
        # 시간에 따른 아이템 증가
        if itemCount == 30:
            tempItem()
            itemCount = 0
        
        # 운석 로직
        if len(rockXY) != 0 and not boss_now :  ############################# 변경점  
            for i, bxy in enumerate(rockXY): # 운석 요소에 대해 반복함
                bxy[1] += rockSpeed # 운석의 y 좌표 + speed (아래로 이동)
                rockXY[i][1] = bxy[1]
                
                if bxy[1] >= padHeight: # 운석이 화면 밖을 벗어나면
                    try:
                        rockXY.remove(bxy) # 운석 제거
                        rockX = random.randrange(0, padWidth - rockWidth)
                        heartCount(count)
                        count -= 1
                        if count < 0:
                            bosswin()
                    except:
                        pass
        
        # 운석 그리기
        if len(rockXY) != 0 and not boss_now :
            for bx, by in rockXY:
                drawObject(rock, bx, by)
                
        # 전투기 위치 재조정
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth
            
        y += fighterY
        if y < padHeight/2:
            y = padHeight/2
        elif y > padHeight - fighterHeight:
            y = padHeight - fighterHeight
        
        for bxy in rockXY: # 운석과 충돌시 하트 사라짐
            if y < bxy[1] and y + fighterHeight > bxy[1] or \
                y + fighterHeight > bxy[1] + rockHeight and y < bxy[1] + rockHeight:
                if (bxy[0] > x and bxy[0] < x + fighterWidth) or \
                    (bxy[0] + rockWidth > x and bxy[0] + rockWidth < x + fighterWidth) or\
                        bxy[0] < x < bxy[0] + rockWidth:
                    rockXY.remove(bxy)
                    heartCount(count)
                    count -= 1
                    if count < 0:
                        bosswin()
        
        # 아이템 그리기                
        if itemXY != 0:
            for bx, by in itemXY:
                drawObject(item, bx, by)
        
        # 아이템 충돌 이벤트
        for bxy in itemXY:
            if y < bxy[1] and y + fighterHeight > bxy[1] or \
                y + fighterHeight > bxy[1] + itemHeight and y < bxy[1] + itemHeight:
                if (bxy[0] > x and bxy[0] < x + fighterWidth) or \
                    (bxy[0] + itemWidth > x and bxy[0] + itemWidth < x + fighterWidth):
                    itemXY.remove(bxy)
                    for i in range(10,475,30):
                        missileXY.append([i,padHeight- 25])
             
        drawObject(fighter, x, y) # 비행기를 게임 화면의 (x,y) 좌표에 그림
        
        if len(missileXY) != 0: 
            for i, bxy in enumerate(missileXY): # 미사일 요소에 대해 반복함
                bxy[1] -= 10 # 총알의 y 좌표 -10 (위로 이동)
                missileXY[i][1] = bxy[1]
                
                
                #  미사일이 운석을 맞추었을 경우
                for i in rockXY:
                    if bxy[1] < i[1]:
                        if bxy[0] > i[0] and bxy[0] < i[0] + rockWidth or \
                            bxy[0] < i[0] and bxy[0] + 30 > i[0]:
                            missileXY.remove(bxy)
                            drawObject(explosion, i[0], i[1]) # 운석 폭발 그리기
                            rockXY.remove(i)
                            destroySound.play()
                            rockX = random.randrange(0, padWidth - rockWidth)
                            shotCount += 1
                            SuperCount += 1
                            rockSpeed += 0.02
                            if rockSpeed >= 10:
                                rockSpeed = 10
                        
                ########################################
                if bxy[1] < boss_Height and boss_now :
                    if bxy[0] > bossX and bxy[0] < bossX  + boss_Width or \
                            bxy[0] < bossX and bxy[0] + boss_Width > bossX :
                        
                        bossHP -= 1
                        #print(bossHP)
                        missileXY.remove(bxy)
                        # drawObject(explosion, bossX , boss_Height * 0.3) # 보스 피격 
                            
                ########################################
                        
                    
                if bxy[1] <= 0: # 미사일이 화면 밖을 벗어나면
                    try:
                        missileXY.remove(bxy) # 미사일 제거
                    except:
                        pass
                    
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)
        
        # 운석 맞춘 점수 표시
        writeScore(shotCount*30)
        
        # 레벨 표시
        writeLevel(level)
        
        
        
        
        
        
        ########################################
        
        # 보스전 
        # 보스 체력
        if bossHP <= 0 :  # 보스를 깻을 
            boss_attack_pattern = 0
            boss_attackXY = []
            bossX = -1000
            bossY = -1000
            drawObject(boss, bossX, bossY)
            bossdie()
            
        elif bossHP > 0 and not boss_image and boss_now : # 보스 전 시
            bossY += 0.5
            drawObject(boss, bossX, bossY)
            
            if bossY >= 0:
                boss_image = True
                boss_attack_pattern = 1
        # 보스 등장  
        elif bossHP > 0 and boss_image and boss_now: 
            # 보스 이동
            if boss_x_cnt >= 100 :
                boss_move_r = False
                boss_x_cnt -= 1
            elif boss_x_cnt <= -100 :
                boss_move_r = True
                boss_x_cnt += 1
            elif boss_move_r :
                boss_x_cnt += 2
            else :
                boss_x_cnt -= 2
            bossX = boss_Width * 2 + boss_x_cnt
            drawObject(boss, bossX , 0)



        # 보스 공격
        if boss_image : 
            boss_attackY += boss_attack_speed 
            
            if boss_attack_pattern == 1 :
                if len(boss_attackXY) == 0 :
                    boss_attackX = boss_attack_startX + 75
                    for i in range(12) :  # 사용되는 공격 12개
                        boss_attackXY.append([boss_attack_startX, boss_attack_startY])
                        
                for i in range(12) :
                    if boss_attackXY[i] == [0,0] :
                        continue
                    
                    elif i in [0,1,2] :
                        boss_attackXY[i] = [boss_attackX + 25 * i, boss_attackY + 60 + 20 * i]
                    elif i in [3,4,5] and boss_attackY > boss_attack_startY + 20 :    
                        boss_attackXY[i] = [boss_attackX - 75 + 25 * (i % 3), boss_attackY + 45 + 20 * (i % 3)]
                    elif i in [6,7,8] and boss_attackY > boss_attack_startY + 40 :
                        boss_attackXY[i] = [boss_attackX - 150 + 25 * (i % 3), boss_attackY + 30 + 20 * (i % 3)]
                    elif boss_attackY > boss_attack_startY + 60 :
                        boss_attackXY[i] = [boss_attackX - 225 + 25 * (i % 3), boss_attackY + 15 + 20 * (i % 3)]
                        
                if boss_attackY > padHeight * 1.2 : 
                    boss_attackX = boss_attack_startX - 30
                    boss_attackY = boss_attack_startY
                    boss_attack_pattern = 2
                    boss_attack_speed = 5
                    boss_attackXY = []
            
            elif boss_attack_pattern == 2 :
                if len(boss_attackXY) == 0 :
                    for i in range(7) :  # 사용되는 공격 7개
                        boss_attackXY.append([boss_attack_startX, boss_attack_startY])
                        
                for i in range(7) :
                    if boss_attackXY[i] == [0,0] :
                        continue
                    elif i == 0 :
                        boss_attackXY[i] = [boss_attackX, boss_attackY + 40]
                    elif i in [1, 2] and boss_attackY > boss_attack_startY + 20  :
                        boss_attackXY[i] = [boss_attackX + 50 * (1 if i % 2 == 0  else -1), boss_attackY + 30]
                    elif i in [3, 4] and boss_attackY > boss_attack_startY + 40  :
                        boss_attackXY[i] = [boss_attackX + 100 * (1 if i % 2 == 0  else -1), boss_attackY + 20]
                    elif boss_attackY > boss_attack_startY + 60  :
                        boss_attackXY[i] = [boss_attackX + 150 * (1 if i % 2 == 0  else -1), boss_attackY + 10]
   
                if boss_attackY > padHeight * 1.2 :
                    if boss_attack_cnt != 2 :
                        boss_attackX = boss_attack_startX - 55 * (1 if boss_attack_cnt % 2 == 0  else -1)
                        boss_attackY = boss_attack_startY
                        boss_attack_cnt += 1
                    else :
                        boss_attackX = boss_attack_startX + 60
                        boss_attackY = boss_attack_startY
                        boss_attack_pattern = 3
                        boss_attack_cnt = 0
                    boss_attackXY = []
                        
            elif boss_attack_pattern == 3 :
                if len(boss_attackXY) == 0 :
                    boss_attack_speed = 3
                    for i in range(28) :  # 사용되는 공격 24개
                        boss_attackXY.append([boss_attack_startX, boss_attack_startY])
                        
                for i in range(28) :
                    if boss_attackXY[i] == [0,0] :
                        continue
                    elif i in range(3) :
                        boss_attackXY[i] = [boss_attackX + (20 * (i % 3) ) , boss_attackY + 10 * (-1 if i % 2 == 0 else 1) ]
                    elif i in range(3,6) :
                        boss_attackXY[i] = [boss_attackX - 40 - (20 * (i % 3) ) , boss_attackY - 40 - 10 * (1 if i % 2 == 0 else -1) ]
                    elif i in range(6,9) and boss_attackY > boss_attack_startY + 50 :
                        boss_attackXY[i] = [boss_attackX + 20 + (20 * (i % 3) ) , boss_attackY - 80 + 10 * (-1 if i % 2 == 0 else 1) ]
                    elif i in range(9,12) and boss_attackY > boss_attack_startY + 50 :
                        boss_attackXY[i] = [boss_attackX - 200 - (20 * (i % 3) ) , boss_attackY - 60 - 10 * (1 if i % 2 == 0 else -1) ]
                    elif i in range(12,15) and boss_attackY > boss_attack_startY + 100 :
                        boss_attackXY[i] = [boss_attackX + 100 + (20 * (i % 3) ) , boss_attackY - 120 + 10 * (-1 if i % 2 == 0 else 1) ]
                    elif i in range(15,18) and boss_attackY > boss_attack_startY + 100 :
                        boss_attackXY[i] = [boss_attackX - 130 - (20 * (i % 3) ) , boss_attackY - 180 - 10 * (1 if i % 2 == 0 else -1) ]
                    elif i in range(18,21) and boss_attackY > boss_attack_startY + 150 :
                        boss_attackXY[i] = [boss_attackX - 270 + (20 * (i % 3) ) , boss_attackY - 150 + 10 * (-1 if i % 2 == 0 else 1) ]
                if boss_attackY > padHeight * 1.2 + 300 :
                    boss_attackX = boss_attack_startX
                    boss_attackY = boss_attack_startY
                    boss_attack_pattern = 1
                    boss_attack_speed = 3
                    boss_attackXY = []
                
        for i, bay in enumerate(boss_attackXY) :
            if y < bay[1] and y + fighterHeight > bay[1] or \
                y + fighterHeight > bay[1] + boss_attack_Height and y < bay[1] + boss_attack_Height:
                
                if (bay[0] > x and bay[0] < x + fighterWidth) or \
                    (bay[0] + boss_attack_Width > x and bay[0] + boss_attack_Width < x + fighterWidth) or\
                        bay[0] < x < bay[0] + boss_attack_Width :
                    boss_attackXY[i] = [0, 0]
                    #print("피격")
                    heartCount(count)
                    count -= 1
                    if count < 0:
                        bosswin()
                    
        for bax, bay in boss_attackXY:            
            if (bax == 0 and bay == 0 ) or (bax == boss_attack_startX and bay == boss_attack_startY) :
                continue           
            drawObject(boss_attack, bax, bay)
            
        
        
        ########################################
        
        for bx, by in heartXY:  # 하트 그리기
            drawObject(heart, bx, by)
            
        pygame.display.update() # 게임화면을 다시 그림
        clock.tick(60) # 게임화면의 초당 프레임수를 60으로 설정
    pygame.quit() # pygame 종료


if __name__ == "__main__":
    mainscreen()

