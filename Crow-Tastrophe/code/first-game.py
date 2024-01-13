import os, sys, math

stdout = sys.stdout
sys.stdout = open(os.devnull, 'w')
import pygame
sys.stdout = stdout
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 800
pygame.init()
print(f'{math.cos(1)} \n {math.cos(1) * 2}')
def main(WIDTH, HEIGHT):
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT),  pygame.RESIZABLE)
    JUMPHEIGHT = -21
    FPS = 60
    clock = pygame.time.Clock()
    fontFuture = pygame.font.Font('Crow-Tastrophe/font(s)\KarmaFuture.otf', 50)
    fontSuture = pygame.font.Font('Crow-Tastrophe/font(s)\KarmaSuture.otf', 50)
    fontSuture_ForGameOver_Text = pygame.font.Font('Crow-Tastrophe/font(s)\KarmaFuture.otf', 150)

    player_gravity = 0
    run_whileLoop = True
    run_game = True   
    gameOver = False
    angle = 0
    timer = 0
    timeAlive = 0
    timer1 = 0

    def display_image(*spriteAndRectangle):
       WINDOW.blit(*spriteAndRectangle)

    def imageLoad(imageRelativePath, convertAlpha):
       if convertAlpha:
           return pygame.image.load(imageRelativePath).convert_alpha()
       else:
           return pygame.image.load(imageRelativePath).convert()

    def Display_timeAlive():
        currentTime = pygame.time.get_ticks() // 1000 - timeAlive
        color = (64, 64, 64)   
        colorForGameOver = (231, 76, 60)
        TimeAlive_Text = fontSuture.render(f'Time Alive : {currentTime}s', False, color)
        TimeAlive_TextRectangle = TimeAlive_Text.get_rect(center = (400, 75))
        display_image(TimeAlive_Text, TimeAlive_TextRectangle)

        return currentTime

    def surfaces():
        runningGame_background = imageLoad('Crow-Tastrophe\images\Sky.png', False)
        ground = imageLoad('Crow-Tastrophe\images\ground.png', False)
        topOfGround = HEIGHT - ground.get_size()[1]

        # scoreSuture = fontFuture.render('SCORE', False, (64, 64, 64))
        # scoreFuture = fontSuture.render('SCORE', False, (64, 64, 64))
        # scoreRectangle = scoreSuture.get_rect(center = (400, 75))
        
        gameOver_text = fontSuture_ForGameOver_Text.render('GAME OVER!', False, (255, 89, 41))
        gameOver_textRectangle = gameOver_text.get_rect(center = (WIDTH//2, HEIGHT//4))
        gameOver_textWidth, gameOver_textHeight = gameOver_text.get_size()
        aspectRatioOfGameOver_text = gameOver_textWidth / gameOver_textHeight
        newHeightOfGameOver_text = 120
        newWidthOfGameOver_text = 700

        gameName = fontSuture.render('CROW-TASTROPHE', False, (55, 55, 55))
        gameName_Rectangle = gameName.get_rect(center = (400, 500))

        retry_button = imageLoad('Crow-Tastrophe\images\gameState_assets/retry_button.png', True)
        # retry_button = 'soon to be used'
        retry_buttonRectangle = retry_button.get_rect(center = (400, 600))

        lizard = imageLoad('Crow-Tastrophe\images/lizard/lizard (1).png', True)
        lizard = pygame.transform.smoothscale(lizard, (99, 100))
        lizardRectangle = lizard.get_rect(midbottom = (704, 681))
        jumpOver_lizardDetection_rectangle = lizard.get_rect()
        lizardRectangle.width = 60
        lizardRectangle.height = 1

        player = imageLoad('Crow-Tastrophe\images/player/player_walk_1.png', True)
        player = pygame.transform.smoothscale(player, (90, 120))
        playerRectangle = player.get_rect(midbottom = (80, topOfGround))
        playerRectangle.width = 90
        playerRectangle.height = 120

        variables = {name: value for name, value in locals().items() if not name.startswith('__')}
        return variables
    variables = surfaces()
    
    while run_whileLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_whileLoop, run_game = False, False

            if run_game: 
                if event.type == pygame.MOUSEBUTTONDOWN and variables['playerRectangle'].bottom == variables['topOfGround']:
                    if variables['playerRectangle'].collidepoint(event.pos) or pygame.MOUSEBUTTONDOWN:
                        player_gravity = JUMPHEIGHT

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or pygame.K_UP or pygame.K_w:
                        if variables['playerRectangle'].bottom == variables['topOfGround']:
                            player_gravity = JUMPHEIGHT
            elif gameOver:
                mouse_position = pygame.mouse.get_pos()
                if variables['retry_buttonRectangle'].collidepoint(mouse_position) and event.type == pygame.MOUSEBUTTONDOWN:
                    run_game, gameOver = True, False
                    timeAlive = pygame.time.get_ticks() // 1000 
                    variables['lizardRectangle'].left = 850
                    variables['playerRectangle'].midbottom = (variables['playerRectangle'].midbottom[0], variables['topOfGround'])

        if run_game:
            display_image(variables['runningGame_background'], (0, 0))
            display_image(variables['ground'], (0, variables['topOfGround'] ))
            
            timeAlive_toDisplay_WhenGameOver = Display_timeAlive()

            # pygame.draw.rect(WINDOW, '#F0B27A', variables['scoreRectangle'], 0, 30)
            # display_image(variables['scoreSuture'], variables['scoreRectangle'])

            variables['lizardRectangle'].x += -5

            if variables['lizardRectangle'].right <= 0:
                variables['lizardRectangle'].left = 850

            display_image(variables['lizard'], variables['lizardRectangle'])

            player_gravity += 0.9
            variables['playerRectangle'] .y += player_gravity
            if variables['playerRectangle'].bottom >= variables['topOfGround']:
                variables['playerRectangle'].bottom = variables['topOfGround']  
            display_image(variables['player'], variables['playerRectangle'])

            if variables['lizardRectangle'].colliderect(variables['playerRectangle']):                        
                run_game, gameOver = False, True

        elif gameOver:
            WINDOW.fill(('black'))

            angle = math.sin(timer) * 3.3
            timer += 0.047

            angle1 = math.cos(timer1) * 3.3
            timer1 += 0.047
            print(f'{angle} \n {angle1} \n \n {timer} \n {timer1 }')


            rotated_gameOver_text = pygame.transform.rotate(variables['gameOver_text'], angle)
            rotated_rectangleOfgameOver_text = rotated_gameOver_text.get_rect(center = variables['gameOver_textRectangle'].center)
            
            maximum_zoom = 1.68
            minimum_zoom = 0.79
            zoom = minimum_zoom + (maximum_zoom - minimum_zoom) * ((math.sin(timer) + 1) / 11)
            print(minimum_zoom + (maximum_zoom - minimum_zoom) * ((math.sin(timer) + 1) / 11))

            rotated_retry_button = pygame.transform.rotozoom(variables['retry_button'], 0, zoom)
            rotated_rectangleOfRetry_button = rotated_retry_button.get_rect(center = variables['retry_buttonRectangle'].center)            
            
            display_image(rotated_retry_button, rotated_rectangleOfRetry_button)
            display_image(rotated_gameOver_text, rotated_rectangleOfgameOver_text)

        pygame.display.update()
        clock.tick(FPS)
class a():
    pass
main(WINDOW_WIDTH, WINDOW_HEIGHT)
# display_image(variables['start_button'], variables['start_buttonRectangle'])
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_SPACE]:
            #     print('LES JUMP')
            
            # if variables['playerRectangle'] .colliderect(variables['lizardRectangle'] ):
            #     pass
            # mousePositon = pygame.mouse.get_pos()
            # if variables['playerRectangle'] .collidepoint(mousepos):
            #     pass
