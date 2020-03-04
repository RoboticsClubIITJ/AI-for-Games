import pygame

#-----------------------------------------Functions------------------------------------------------

# convertert coordinates of points to pixels values
def coor_to_px(coordinates):
    x, y = coordinates
    return (x * 200, y * 200)


# CreateMatrix function : takes a 3x3 matrix which stores cross/zero/empty, then outputs the tictactoe game 
# 0=empty 1=cross and 2=zero

def createMatrix(matrix):
    for x in range(3):
        for y in range(3):
            if matrix[y][x] == 0:
                screen.blit(box, coor_to_px((x, y)))
            elif matrix[y][x] == 1:
                screen.blit(cross, coor_to_px((x, y)))
            else:
                screen.blit(zero, coor_to_px((x, y)))


# Position to Coordinate: convert pixel coordinates to matrix coordinates(0,1 or 2)

def pos_to_coord(x, y):
    x = (x/200) % 3
    y = (y/200) % 3
    return int(x), int(y)

#-------------------------------------------/ Functions -----------------------------------------------

#------------------------------------------- Pygame utilities -----------------------------------------
pygame.init()

# Title and Icon
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load("./assets/icons/tic-tac-toe.png")
pygame.display.set_icon(icon)

width = 600
height = 600

# create the screen
screen = pygame.display.set_mode((width, height))

# loading Sprites

# empty box, cross and zero images stored
box = pygame.image.load('./assets/sprites/sprite_box.png')
cross = pygame.image.load('./assets/sprites/sprite_x.png')
zero = pygame.image.load('./assets/sprites/sprite_o.png')

# updates the screen, needs to be called in each loop
def update_screen():
    pygame.display.update()

# returns false if user chooses to quit the game
def check_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True