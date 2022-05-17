import pygame
import sys
from time import sleep

BLACK = ( 0, 0 , 0)
padWidth = 480           # 게임화면의 가로크기
padHeight = 640          # 게임화면의 세로크기

explosionSound = ['explosion01.wav','explosion02.wav','explosion03.wav','explosion04.wav']

# 게임에 등장하는 객체를 드로잉
def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x,y)) 

    
    
    
def initGame():
    global gamePad, clock, background, fighter, missile, missileSound, gameOverSound, boss, boss_attack, explosion
    
    
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting') # 게임이름
    background = pygame.image.load('background.png') # 배경 그림
    fighter = pygame.image.load('fighter.png') # 전투기 그림
    missile = pygame.image.load('./missile.png') # 미사일 그림
    explosion = pygame.image.load('explosion.png') # 폭발 그림
    
    boss = pygame.image.load('./boss.png')
    boss = pygame.transform.scale(boss,(padWidth / 5.0 , padHeight / 10.0))
    boss_attack = pygame.image.load('./temp.png')
    boss_attack = pygame.transform.scale(boss_attack,(24 , 12))
    
    
    #pygame.mixer.music.load('music.wav')                  # 배경 음악
    #pygame.mixer.music.play(-1)                           # 배경 음악 재생
    #missileSound = pygame.mixer.Sound('missile.wav')      # 미사일 사운드
    #gameOverSound = pygame.mixer.Sound('gameover.wav')    # 게임 오버 사운드
    
    clock = pygame.time.Clock()
    pygame.init()

    
def runGame():
    global gamePad, clock, background, fighter, missile, missileSound, boss, boss_attack, bossHP, explosion
    
    
    isShot = False
    shotCount = 0
    level = 1
    
    # 무기 좌표 리스트
    missileXY = []
    
    # 보스 이미지 변수
    bossHP = 100
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
    

    # 전투기 크기
    fighterSize = fighter.get_rect().size
    fighterWidth = fighterSize[0]
    fighterHeight = fighterSize[1]
    
    # 전투기 초기 위치
    x = padWidth * 0.45
    y = padHeight * 0.9
    fighterX = 0

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
                
                elif event.key == pygame.K_SPACE: # 미사일 발사
                    #missileSound.play()  # 미사일 사운드 재생
                    missileX = x + fighterWidth/2
                    missileY = y - fighterHeight
                    missileXY.append([missileX,missileY])
            
            if event.type in [pygame.KEYUP]: # 방향키를 떼면 전투기 멈춤
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    fighterX = 0    
        
        drawObject(background, 0, 0 ) # 배경 화면 그리기
        
        # 전투기 위치 재조정
        x += fighterX
        if x < 0:
            x = 0
        elif x > padWidth - fighterWidth:
            x = padWidth - fighterWidth
        
        
        drawObject(fighter, x, y) # 비행기를 게임 화면의 (x,y) 좌표에 그림
        
        # 미사일 발사 화면에 그리기
        if len(missileXY) != 0: 
            for i, bxy in enumerate(missileXY): # 미사일 요소에 대해 반복함
                bxy[1] -= 10 # 총알의 y 좌표 -10 (위로 이동)
                missileXY[i][1] = bxy[1]
                
                if bxy[1] < boss_Height :
                    if bxy[0] > bossX and bxy[0] < bossX  + boss_Width or \
                            bxy[0] < bossX and bxy[0] + boss_Width > bossX :
                        
                        bossHP -= 1
                        print(bossHP)
                        missileXY.remove(bxy)
                        drawObject(explosion, bossX , boss_Height * 0.3) # 보스 피격 
                    
                
                if bxy[1] <= 0: # 미사일이 화면 밖을 벗어나면
                    try:
                        missileXY.remove(bxy) # 미사일 제거
                    except:
                        pass
        if len(missileXY) != 0:
            for bx, by in missileXY:
                drawObject(missile, bx, by)
        
        
        
        # 보스전 
        # 보스 체력
        if bossHP == 0 :
            boss_attack_pattern = 0
            boss_attackXY = []
            bossX = -1000
            bossY = -1000
            
        elif bossHP > 0 and not boss_image :
            bossY += 0.5
            drawObject(boss, bossX, bossY)
            
            if bossY >= 0:
                boss_image = True
                boss_attack_pattern = 1
        # 보스 등장  
        elif bossHP > 0 and boss_image : 
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
                        
                if boss_attackXY[11][1] > padHeight * 1.2 : 
                    boss_attackX = boss_attack_startX - 30
                    boss_attackY = boss_attack_startY
                    boss_attack_pattern = 2
                    boss_attack_speed = 3.5
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
                    print("피격")
                    
        for bax, bay in boss_attackXY:            
            if (bax == 0 and bay == 0 ) or (bax == boss_attack_startX and bay == boss_attack_startY) :
                continue           
            drawObject(boss_attack, bax, bay)
            
            
       
        
        
                
        pygame.display.update() # 게임화면을 다시 그림
        
        clock.tick(60) # 게임화면의 초당 프레임수를 60으로 설정
    

    pygame.quit() # pygame 종료
    