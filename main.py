import pygame

pygame.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed THe Dragon")


FPS = 60
clock = pygame.time.Clock()

'''Create a constant that shores tracks player starting lives and give it a startng value of 5'''
'''Create a constant that shores tracks player starting velociy and give it a startng value of 10'''
'''Create a constant that shores tracks coin starting velocity and give it a startng value of 10'''
'''Create a constant that shores tracks coin starting velocity and give it a startng value of 10'''
'''Create a constant that shores tracks coin acceleration and give it a startng value of 0.5'''

'''Create a variable that tracks the score and give it a startng value of 0'''
'''Create a variable that tracks the player and set it equal to the constant that stores player starting lives'''
'''Create a variable that tracks the coin velocity and set it equal to the constant that coin starting velocity'''


GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
white = (255, 255, 255)
BLACK = (0, 0, 0)
'''create a variable called front and give it a value from the following:  pygame.font.Font('AttackGraffiti.ttf',32)'''

''' create a variable that tracks score text and give it a value following: font.render("Score: " + str(score), True, GREEN, DARK_GREEN)'''
''' create a variable that tracks score rect and give it a value from the following: score_text.get_rect() '''
''' title_rect.centerx + WINDOW_WIDTH / 2'''
''' title_rect.y = 10 '''

''' Same deal, variable name lives_text, "Lives: str(player_lives), True, GREEN, DARKGREEN '''
''' Same deal, variable name lives_rect, get from lives_text '''
''' Same deal, topright = (WINDOW_WIDTH - 10, 10)'''

'''
Variable: game_over_text
Rect: game_over_rect
PHRASE: "GAMEOVER",
Antialias: True
Color: GREEN,
Background: DARKGREED ,
Position: center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
'''

'''
Variable:  continue_text
Rect: continue_rect
PHRASE:  "Press any key to play again", 
Antialias: True
Color: GREEN, 
Background: DARKGREEN,
Position: center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 32),
'''



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    score_text = font.render("Score: " + str(score), True, GREEN, DARK_GREEN)
    lives_text = font.render("Lives: " + str(player_lives), True, GREEN, DARK_GREEN)


    display_surface.fill(BLACK)


    display_surface.blit(score_text, score_rect)
    display_surface.blit(title_text, title_rect)
    display_surface.blit(lives_text, lives_rect)

pygame.quit()