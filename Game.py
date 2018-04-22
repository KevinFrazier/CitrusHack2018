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
    def __init__(self, image, hp, atk, mp, abilities, movement, rge, id):
        self.hp = hp
        self.atk = atk
        self.mp = mp
        self.abilities = abilities
        self.movement = movement
        self.range = rge
        self.image = pygame.image.load(image)
        self.hasMoved = False
        self.ID = id

'''
MapGrid
variables: length, width
functions:
moveObject(position):
'''


class Player:
    def __init__(self, ID):
        self.player = ID
        self.team = []
        self.isTurn = False

    def addMember(self, character):
        if type(character) is "<class '__main__.Character'>":
            self.team.append(character)
            print("added team member")
            return True
        else:
            return False

    def changeTurn(self, BOOL):
        self.isTurn = BOOL
        return

    def isTurn(self):
        return self.isTurn

    def isInTeam(self, character):
        if type(character) is "<class '__main__.Character'>":
            for member in self.team:
                character


class GameSequenece:
    '''
    GameSequence summary: Keeps track of player turn sequence and Game end

    Functionalities
        -start game
        -must start turns
        -change turns
        -end turns
        -end game

    '''

    def __init__(self, ArrayofPlayers):
        if (len(ArrayofPlayers) < 2):
            return False

        self.players = ArrayofPlayers
        self.currentTurn = None

    def startGame(self):
        self.currentTurn = 0
        '''
        does some intro animaton -> starts game

        '''
        return

    def startTurn(self):
        self.players[self.currentTurn].changeTurn(True)
        '''
        maybe some camera change animation to player location
        '''
        return

    def getTurn(self):
        return self.currentTurn

    def changeTurn(self):
        self.players[self.currentTurn].changeTurn(False)
        self.currentTurn += 1
        self.currentTurn = self.currentTurn % len(self.players)

    def endTurn(self):
        self.players[self.currentTurn].changeTurn(False)


'''
MapGrid
variables: length, width,'
functions:
moveObject(position):
'''

def startGame():
    # colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    # graphics
    '''
    1. make grid
    2. put objects in grid
    3. manipulating objects in grid
    '''

    GameMap = MapGrid(50, 50, 20)
    grid = GameMap.grid

    clock = pygame.time.Clock()
    totalUnits = 0
    character1 = Character('Montblanc.jpg', 100, 10, 1, 1, 1, 3,totalUnits) #image, hp, atk, mp, abilities, movement, range
    totalUnits +=1
    character2 = Character('shara.jpg', 100, 10, 1, 1, 1, 3,totalUnits)
    character3 = Character('circle.png',)
    #player1 init
    player1 = grid[1][2]
    player1.changeCharacter(character1)
    player1.isfilled = True

    # player2 init
    player2 = grid[2][3]
    player2.changeCharacter(character2)
    player2.isfilled = True


    P1 = Player(1)
    P2 = Player(2)
    theGame= GameSequenece(P1, P2)
    theGame.startGame()
    #should be P1's turn
    theGame.startTurn()

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen
    WINDOW_SIZE = [GameMap.tileWidth * GameMap.gridWidth,
                   GameMap.tileHeight * GameMap.gridHeight]
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
                column = pos[0] // GameMap.tileWidth
                row = pos[1] // GameMap.tileHeight

                if grid[row][column].isfilled is True:
                    if GameMap.attackCharacter(player2, player1) is False:
                        print("Not in range")
                else:
                    GameMap.moveCharacter(player1.posX, player1.posY, column, row)
                    player1 = grid[row][column]
                print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
        screen.fill(BLACK)

        # Draw the grid
        for row in range(GameMap.gridHeight):
            for column in range(GameMap.gridWidth):
                color = BLACK

                pygame.draw.rect(screen,
                                 color,
                                 [GameMap.tileWidth * column,
                                  GameMap.tileHeight * row,
                                  GameMap.tileWidth,
                                  GameMap.tileHeight])
                temp = grid[row][column]
                if temp.isFilled() is True:
                    screen.blit(temp.character.image, ((column * GameMap.tileWidth), (row * GameMap.tileHeight)))

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

class Tile:
    def __init__(self, H, W, background, character, positionX, positionY):
        self.height = H
        self.width = W

        # background image (string of image in directory)
        self.background = background

        # character object
        self.character = character

        self.posX = positionX
        self.posY = positionY

        self.isfilled = False

    def changeBackground(self, background):
        self.background = pygame.image.load(background)
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def changeCharacter(self, character):
        self.character = character
        if character is 0:
            return
        else:
            self.character.image = pygame.transform.scale(self.character.image, (self.width, self.height))

    def isFilled(self):
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
                temp = Tile(tilesize, tilesize, 0, 0, column, row)
                temp.changeBackground('Square.jpg')
                self.grid[row].append(temp)  # Append a cell

    def moveCharacter(self, pos1X, pos1Y, pos2X, pos2Y):
        destination = self.grid[pos2Y][pos2X]
        source = self.grid[pos1Y][pos1X]
        if destination.isfilled is True:
            print("FILLED")
            return False
        else:
            destination.changeCharacter(source.character)
            destination.isfilled = True
            source.changeCharacter(0)
            source.isfilled = False
            return True

    # attackCharacter(whats attacking, whats being attacked)
    def attackCharacter(self, victim, attacker):
        # in range
        if attacker.character.range >= (abs(victim.posX - attacker.posX) + abs(victim.posY - attacker.posY)):
            # attack
            victim.character.hp -= attacker.character.atk
            if victim.character.hp <= 0:
                print("DEAD")
            else:
                print("Attacker's Atk: ", attacker.character.hp)
                print("Victim's HP: ", victim.character.hp)
                # remove from map
            return True
        else:
            return False

def main():
    startGame()


if __name__ == "__main__":
    main()