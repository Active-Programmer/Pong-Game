
import pygame,sys , random
pygame.init()

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 600

#colors

white = (255,255,255)
red1 = (20,150,150)
black = (0,0,0)
red = (255,255,255)

#variables for moving a ball
ball_speed_x = 1
ball_speed_y = 1

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Mr Shaan Pong Game")

#Game Rectangles

ball = pygame.Rect(SCREEN_WIDTH/2-15,SCREEN_HEIGHT/2-15,30,30)  # WDTH AND HRIGHT

player1 = pygame.Rect(SCREEN_WIDTH-20,SCREEN_HEIGHT/2-70,10,140,)

opponent = pygame.Rect(10,SCREEN_HEIGHT/2-70,10,140)

def ball_animations():
    global player_score,opponent_score
    global ball_speed_x,ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top<=0 or ball.bottom>=SCREEN_HEIGHT:
        ball_speed_y *= -1

    if ball.left<=0:
        player_score+=1
        ball_restart()
    if ball.right>=SCREEN_WIDTH:
        opponent_score+=1
        ball_restart()
    if ball.colliderect(player1) or ball.colliderect(opponent):
        ball_speed_x *= -1
def ball_restart():
        global ball_speed_x,ball_speed_y
        ball.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

        ball_speed_y *= random.choice((1,-1))
        ball_speed_x *= random.choice((1,-1))

#Score variables and font 

player_score = 0
opponent_score = 0

game_font = pygame.font.Font("freesansbold.ttf",32)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and player1.bottom<=600:
        player1.y +=2

    if keys[pygame.K_UP] and player1.bottom>=145:
        player1.y -=2

    if keys[pygame.K_LEFT] and opponent.top>=10:
        opponent.y -=2

    if keys[pygame.K_RIGHT] and opponent.bottom<=600:
        opponent.y +=2

    
    ball_animations()

    #visuals
    screen.fill((0,0,0))
    pygame.draw.rect(screen,white,player1)
    pygame.draw.rect(screen,white,opponent)
    pygame.draw.ellipse(screen,red,ball)
    pygame.draw.aaline(screen,red,(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT),1)

    #creating the font surface
    player_text = game_font.render(f"{player_score}",False,white)
    screen.blit(player_text,(600,300))
    opponent_text = game_font.render(f"{opponent_score}",False,white)
    screen.blit(opponent_text,(500,300))
    pygame.display.update()

pygame.quit()
quit()