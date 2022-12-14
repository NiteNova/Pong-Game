import pygame, sys 
import random




#---------------------Collisons and ball movement------------------
def ball_animation():
    global ball_speed_x, ball_speed_y, p1Score, p2Score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
  
    
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    
    if ball.left <= 0:
        p1Score += 1
        ball_restart()
    
    if ball.right >= screen_width:
        ball_restart()
        p2Score += 1
    

        
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        bloop.play()
#------------------------------------------------------------------



#---------------------player animation (How they move on the screen)-----------------
def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >=screen_height:
        player.bottom = screen_height
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >=screen_height:
        opponent.bottom = screen_height
#-------------------------------------------------------------------------------------




#-----------restarts the ball after a score in a random direction---------------------
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center= (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
#------------------------------------------------------------------------------------
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0 
opponent_speed =7

#Score System
p1Score = 0
p2Score = 0


#sound
pygame.mixer.init()
bloop = pygame.mixer.Sound("ping_pong_8bit_beeep.ogg")


# General set up
pygame.init()
clock = pygame.time.Clock()



# Setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')
                        
# Variables for the render section
ball = pygame.Rect(screen_width/ 2 - 15, screen_height/2 -15, 30,30)     
player = pygame.Rect(screen_width - 20, screen_height/2 - 70 ,10,140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)


#key inputs from the user and output to the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type ==pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
                
    #function calls
    ball_animation()
    player_animation() 
    opponent_ai()
        
    
    #Render Section
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2,screen_height))
    
    font = pygame.font.Font(None, 74) #use default font
    text = font.render(str(p1Score), 1, (255, 255, 255))
    screen.blit(text, (750, 10))
    text = font.render(str(p2Score), 1, (255, 255, 255))
    screen.blit(text, (500, 10))    
        
    #updating the window
    pygame.display.flip()
    clock.tick(60)
