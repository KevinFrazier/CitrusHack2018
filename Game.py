import pygame
import sys
import itertools

'''
Task List:
-heroes 
    make the class
    design -> (circles)
    appropriately put it in map grid
    then graphics
    
Map ->
 make grid
 design (2D grid of 45 degrees, skewed squared)
 scaling
 cosmetics
 put into graphics
 
'''


'''
characters
variables: hp, atk, mp, abilities (array),  weakness, movement, range,
other variables: sprite, animation 
'''
class Character:
    def __init__(self, image2, hp2,atk2, mp2, abilities2, movement2, range2):
        self.hp = hp2
        self.atk = atk2
        self.mp = mp2
        self.abilities = abilities2
        self.movement = movement2
        self.range = range2
        self.image = image2

'''
MapGrid
variables: length, width,'
functions:
moveObject(position):
'''
class Tile:
    def __init__(self,H,W,background, character):
        self.height = H
        self.width = W
        self.background = 0
        self.character = 0
        self.isfilled = False
    def changeBackground(self,background):
        self.background = pygame.image.load(background)
        self.background = pygame.transform.scale(self.background, (self.width,self.height))
    def changeCharacter(self,character):
        self.character = pygame.image.load(character)
        self.character = pygame.transform.scale(self.character, (self.width, self.height))


class MapGrid:
    def __init__(self, H, W, tilesize):
        self.gridHeight = H
        self.gridWidth = W
        self.tileWidth = tilesize
        self.tileHeight = tilesize
        self.grid = []
        for row in range(self.gridHeight):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.gridWidth):
                temp = Tile(tilesize,tilesize,0,0)
                self.grid[row].append(temp)  # Append a cell


#colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
#graphics
'''

x 1. make grid
x . put objects in grid
3. manipulating objects in grid
'''

"""
 Example program to show using an array to back a grid on-screen.

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20


# This sets the margin between each cell
MARGIN = 5
GameMap = MapGrid(50, 50, 20)
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = GameMap.grid
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
def main():
    character1 = Character('Montblanc.jpg',0,0,0,0,0,0)
    character2 = Character('Circle.png', 1, 1, 1, 1, 1,1 )
    interchange = False
    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)
    grid[1][5] = 1

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [GameMap.tileWidth*GameMap.gridWidth,
                   GameMap.tileHeight*GameMap.gridHeight]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("Array Backed Grid")

    # Loop until the user clicks the close button.
    done = False
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // (GameMap.tileWidth)
                row = pos[1] // (GameMap.tileHeight)
                # Set that location to one

                grid[row][column] = 1
                if(interchange == False):
                    grid[row][column].changeCharacter(character1)

                print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(GameMap.gridHeight):
            for column in range(GameMap.gridWidth):
                color = BLACK

                pygame.draw.rect(screen,
                                 color,
                                 [(GameMap.tileWidth) * column,
                                  (GameMap.tileHeight) * row,
                                  GameMap.tileWidth,
                                  GameMap.tileHeight])
                if grid[row][column] == 1:
                    screen.blit(image,((column*GameMap.tileHeight)
                                        , (row*GameMap.tileWidth)))

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__== "__main__":
  main()
