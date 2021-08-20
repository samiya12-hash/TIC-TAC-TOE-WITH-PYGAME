#IMPORT

from turtle import color
import pygame, sys
import numpy as np
# IT WILL HELP US IN THE CONSOLE

#INITIALIZE PYGAME
pygame.init()

#CONSTANTS (I WILL BE USING THEM THROUGHOUT THE CODE. THE VALUES HAVE BEEN OBTAINED THROUGH EXPERIMENTATION)

WIDTH = 800
HEIGHT= WIDTH
LINE_WIDTH= 10
BOARD_ROWS=3
BOARD_COLUMNS=3
SQUARE_SIZE=WIDTH//BOARD_COLUMNS
CIRCLE_RADIUS= WIDTH//10
CIRCLE_WIDTH=15
CROSS_WIDTH= 25
SPACE= SQUARE_SIZE/4

#COLORS (FOR SCREEN, FIGURES AND TEXT)
BACKGROUND_COLOR= (28,170,156)
LINE_COLOR=(23,145,135)
CIRCLE_COLOR=(239, 231, 200)
TEXT_COLOR= (236, 42,23)
CROSS_COLOR= (66,66,66)


# GAME SCREEN

screen = pygame.display.set_mode( (WIDTH,HEIGHT) )
pygame.display.set_caption('TIC-TAC-TOE')  # TITLE
screen.fill (BACKGROUND_COLOR) #SCREEN COLOR

#CONSOLE

board = np.zeros( (BOARD_ROWS, BOARD_COLUMNS) )
print(board)
# THIS WILL SHOW A TIC-TACT-TOE BOARD SIMILAR TO A MATRIX IN THE TERMINAL AND ALL THE ENTRIES WILL BE 0.

# DEFINING FUNCTIONS (WHICH I WILL CALL LATER)

#LINES
def draw_lines():
    
    #pygame.draw.line (SCREEN, LINE COLOR, STARTING POSITION, ENDING POSITION, WIDTH)
    
    # 2 HORIZONTAL LINES
    pygame.draw.line( screen, LINE_COLOR, (0,SQUARE_SIZE), (WIDTH,SQUARE_SIZE), LINE_WIDTH )
    pygame.draw.line( screen, LINE_COLOR, (0,2*SQUARE_SIZE), (WIDTH,2*SQUARE_SIZE), LINE_WIDTH )
   
    # 2 VERTICAL LINES
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE,0), (SQUARE_SIZE,HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2*SQUARE_SIZE,0), (2*SQUARE_SIZE,HEIGHT), LINE_WIDTH)

draw_lines() 
# NOW THE draw_lines() FUNCTION IS CALLED ADN THE LINES WILL BE DRAWN ON THE SCREEN.

# PYGAME HAS A UNIQUE CO-ORDINATE SYSTEM. THE UPPER LEFT CORNER IS (0,0). THE ABSCISSA (X-COORDINATE) INCREASES AS WE GO RIGHT AND THE ORDINATE (Y-COORDINATE) INCREASES AS WE GO DOWN.

# FIGURES ( X AND O )

def draw_figures():
   
    for row in range(BOARD_ROWS):
   
        for column in range(BOARD_COLUMNS):
   
            if board[row][column]== 1:
   
                # pygame.draw.figure (screen, color, coordinate in integer, radius, width)
                pygame.draw.circle( screen, CIRCLE_COLOR , (int(column* SQUARE_SIZE + SQUARE_SIZE//2 ), int( row*  SQUARE_SIZE+SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH )
   
            elif board[row][column]== 2:
                
                # FOR CROSSES, WE HAVE TO DRAW 2 LINES.
                # pygame.draw.line (screen, color, starting co-ordinate, ending co-ordinate, wdith)
                pygame.draw.line( screen, CROSS_COLOR, (column* SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE- SPACE), (column * SQUARE_SIZE + SQUARE_SIZE//2 + SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH )
                pygame.draw.line( screen, CROSS_COLOR, (column* SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (column * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE- SPACE), CROSS_WIDTH )
                # WE USED THE SPACE SO THAT THE LINES DON'T TOUCH THE BORDERS OF A SQUARE.   

# MARK SQUARES (THESE ARE USED TO MARK THE SQUARES SELECTED BY PLAYERS )

def mark_square(row, column, player):
    board[row][column]= player

# TO CHECK IF IT IS WORKING OR NOT, PRINT THE BOARD AFTER MARKING A SQUARE.
   
# AVAILABLE SQUARES (USED TO CHECK IF A SQUARE IS AVAILABLE )
  
def available_square(row, column):
    return board[row][column]== 0

# TO FIND OUT IF A SQUARE IS AVAILABLE, TYPE- print(availble_square(co-ordinate)) AND CHECK THE TERMINAL (RESPONSE WILL BE TRUE OR FALSE)

def board_is_full():
    # FIRST LOOP THROUGH ALL THE ROWS
    for row in range(BOARD_ROWS):  
        #SECOND LOOP THROUGH ALL THE COLUMNS
        for column in range(BOARD_COLUMNS): 
            if board[row][column] ==0:  
            # IF IT IS 0, THAT MEANS THERE IS AN EMPTY SQUARE. SO, THE BOARD IS NOT FULL. 
               return False
        return True
        # IF IT IS NOT 0, THEN THERE IS NO EMPTY SQUARE. SO, THE BOARD IS FULL.

# THESE LINES HAVE BEEN USED TO CHECK IF THE BOARD IS FULL OR NOT. TO CHECK IF IT IS WORKING, print(is_board_full()) AFTER MARKING ALL SQUARES                 
                 
                    
# CHECK WINNING CONDITIONS

def check_win (player):
   
    # VERTICAL WIN CHECK- LOOPING THROUGH THE COLUMNS
    for column in range(BOARD_COLUMNS):
        if board[0][column]==player and board[1][column]==player and board[2][column]==player:
            draw_vertical_winning_line (column, player)
            return True
   
    # HORIZONTAL WIN CHECK - LOOPING THROUGH THE ROWS
    for row in range(BOARD_ROWS):
        if board[row][0]==player and board[row][1]==player and board[row][2]==player:
          draw_horizontal_winning_line(row, player)
          return True
   
    # ASCENDING DIAGONAL WIN CHECK - LOOPING THROUGH THE ASCENDING DIAGONAL
    if board[2][0]==player and board[1][1]==player and board[0][2]==player:
       draw_ascending_diagonal(player)
       return True
   
    # DESCENDING DIAGONAL WIN CHECK - LOOPING THROUGH THE DESCENDING DIAGONAL
    if board[0][0]==player and board[1][1]== player and board[2][2]==player:
       draw_descending_diagonal(player)
       return True
    
    return False


# WINNING LINES    

def draw_vertical_winning_line (column, player):
    posX=column * SQUARE_SIZE + SQUARE_SIZE//2
    # CO-ORDINATES OF VERTICAL WINNING LINE
    if player==1:
        color = CIRCLE_COLOR
    elif player==2:
        color = CROSS_COLOR
    # NOW THE WINNING LINE WILL BE OF THE SAME COLOR AS THE WINNING SIGN    

    pygame.draw.line(screen, color, (posX,15), (posX, HEIGHT-15), LINE_WIDTH)

def draw_horizontal_winning_line (row, player):
    posY=row * SQUARE_SIZE + SQUARE_SIZE//2

    if player==1:
        color = CIRCLE_COLOR
    elif player==2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH-15,posY), LINE_WIDTH)

def draw_ascending_diagonal(player):
    
    if player==1:
        color = CIRCLE_COLOR
    elif player==2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT-15), (WIDTH-15, 15), LINE_WIDTH)

def draw_descending_diagonal(player):
    
    if player==1:
        color = CIRCLE_COLOR
    elif player==2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15,15), (WIDTH-15,HEIGHT-15), LINE_WIDTH)

# RESTART FUNCTION (TO RESTART THE GAME AFTER A ROUND IS OVER)
def restart():
    #SETTING SCREEN AGAIN
    screen.fill(BACKGROUND_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for column in range(BOARD_COLUMNS):
            board[row][column]=0

# QUIT FUNCTION (TO QUIT THE GAME AFTER A ROUND IS OVER)
def quit():
    event.type==pygame.QUIT
    pygame.quit()
    sys.quit()

    



# ASSIGNING VARIABLES
player = 1
game_over= False
# THE GAME WILL BE STOPPED IF IT IS OVER.

# TIME TO CALL THE FUNCTIONS

# MAIN LOOP

while True:
   
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
           sys.exit()
              
        
        if event.type== pygame.MOUSEBUTTONDOWN and not game_over: 
             # THE GAME IS GOING ON (GAME_OVER= FALSE)

            mouseX = event.pos[0] # X
            mouseY = event.pos[1] # Y

            clicked_row = int(mouseY // SQUARE_SIZE) 
            clicked_column = int(mouseX // SQUARE_SIZE) 

            # LINKING OUR CONSOLE WITH THE SCREEN          

            if available_square ( clicked_row, clicked_column ):

                # TAKE INPUTS ONLY WHEN SQUARES ARE AVAILABLE
               
                if player==1:
                    mark_square( clicked_row, clicked_column, 1 )
                    # PLAYER-1 HAS MARKED A SQUARE
                    if check_win ( player ):
                        game_over=True
                        font = pygame.font.SysFont(None, 40)
                        img = font.render('CIRCLE WON. Press q to quit OR r to restart', True, TEXT_COLOR)
                        screen.blit(img, (WIDTH//6, 20))
                    # CHECKING IF PLAYER-1 HAS WON OR NOT
                    # IF PLAYER-1 WINS, THE WRITTEN TEXT WILL APPEAR ON THE SCREEN IN THE POSITION MENTIONED     
                    
                        player = 2
                    
                    # NOW, WE ARE SWITCHING TO PLAYER-2 
                
                elif player==2:
                    mark_square( clicked_row, clicked_column, 2 )     
                    if check_win( player ):
                       game_over=True
                       font = pygame.font.SysFont(None, 40)
                       img = font.render('CROSS WON. Press q to quit OR r to restart', True, TEXT_COLOR)
                       screen.blit(img, (WIDTH//6, 20))
                      
                    
                    player = 1
                    # NOW, WE ARE SWITCHING BACK TO PLAYER-1. IN THIS WAY, WE CAN KEEP SWITCHING BETWEEN THE PLAYERS AFTER A MOVE.
                
                # WHAT HAPPENS IF THE BOARD IS FULL? 3 POSSIBILITIES-
                if  board_is_full(): 
                   game_over= True
                   font=pygame.font.SysFont(None,40)
                   if check_win(1): img=font.render('CIRCLE WON. Press q to quit OR r to restart', True, TEXT_COLOR)
                   # 1) PLAYER-1 OR CIRCLE WON BY CLICKING THE LAST REMAINING SQUARE.
                   elif check_win(2):img=font.render('CROSS WON. Press q to quit OR r to restart', True, TEXT_COLOR)
                   # 2) PLAYER-2 OR CROSS WON BY CLICKING THE LAST REMAINING SQUARE.
                   else: img=font.render('DRAW. Press q to quit OR r to restart', True, TEXT_COLOR)
                   # 3) NONE OF THEM WON BY CLICKING THE LAST REMAINING SQUARE
                   screen.blit(img,(WIDTH//6,20))
                
                draw_figures()

                
        # ASSIGNING KEYS FOR RESTARTING OR QUITTING THE GAME       
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r:
                restart()  # CALLING THE RESTART FUNCTION
                player=1
                game_over=False

            # NOW, IF WE PRESS 'r', THE GAME WILL RESTART FROM PLAYER-1 (AS ASSIGNED) AND THE GAME IS NOT OVER; IT'S JUST BEGINNING           

            if event.key==pygame.K_q:
                quit()   # CALLING THE QUIT FUNCTION

            # NOW, IF WE PRESS 'q', WE CAN QUIT THE GAME.
        
    pygame.display.update()
    
    # NOW THE SCREEN AND GAME WHICH WE HAVE UPDATED THROUGHOUT THE CODE WILL BE DISPLAYED




               

