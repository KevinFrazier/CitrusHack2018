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
        self.image = pygame.image.load(image2)

'''
MapGrid
variables: length, width,'
functions:
moveObject(position):
'''
class Tile:
    def __init__(self,H,W,background, character, positionX,positionY):
        self.height = H
        self.width = W
        self.posX = positionX
        self.posY = positionY
        #background image (string of image in directory)
        self.background = 0

        #character object
        self.character = 0

        self.isfilled = False

    def changeBackground(self,background):
        self.background = pygame.image.load(background)
        self.background = pygame.transform.scale(self.background, (self.width,self.height))

    def changeCharacter(self,character):
        self.character = character
        if character is 0:
            return
        else:
            self.character.image = pygame.transform.scale(self.character.image, (self.width,self.height))

    def checkFilled(self):
        return self.isfilled

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
                temp = Tile(tilesize,tilesize,0,0,column,row)
                temp.changeBackground('Square.jpg')
                self.grid[row].append(temp) # Append a cell

    def moveCharacter(self, pos1X,pos1Y, pos2X,pos2Y):
        destination = self.grid[pos2X][pos2Y]
        source = self.grid[pos1X][pos1Y]
        if(destination.isfilled is True):
            print("FILLED")
            return False
        else:
            destination.changeCharacter(source.character)
            destination.isfilled = True
            source.changeCharacter(0)
            source.isfilled = False
            return True

#attackCharacter(whats atacking, whats being attacked)
    def attackCharacter(self, victim, attacker):
        #in range
        if attacker.character.range >= (abs(victim.posX - attacker.posX) + abs(victim.posY - attacker.posY)):
            #attack
            victim.character.hp -= attacker.character.atk
            if(victim.character.hp <= 0):
                print("DEAD")
            else:
                print("Victim's HP: ", victim.character.hp)
                #remove from map
            return True
        else:
            return False


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

GameMap = MapGrid(50, 50, 20)
grid = GameMap.grid

clock = pygame.time.Clock()

def main():


    character1 = Character('Montblanc.jpg',0,0,0,0,0,0)
    character2 = Character('Circle.png', 1, 1, 1, 1, 1,1 )
    interchange = False
    # Set row 1, cell 5 to one. (Remember rows and
    # column numbers start at zero.)
    # Initialize pygame
    Tile1 = grid[1][2]
    Tile1.changeCharacter(character1)
    Tile1.isfilled = True
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

                # if grid[row][column].isfilled is True:
                #     print("IS FUCKIN FILLED ALREADY")
                # else:
                #     grid[row][column].isfilled = True
                #
                #     # if interchange is False:
                #     grid[row][column].changeCharacter(character2)
                GameMap.moveCharacter(Tile1.posX,Tile1.posY,row,column)
                Tile1 = grid[column][row]
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
                temp = grid[row][column]
                if temp.checkFilled() is True:
                    screen.blit(temp.character.image, ((column*GameMap.tileHeight), (row*GameMap.tileWidth)))

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__== "__main__":
  main()
