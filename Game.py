import pygame
from GameSequence import GameSequence
from Player import Player
from Tile import Tile
from MapGrid import MapGrid
from Character import Character
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
'''
MapGrid
variables: length, width
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

    GameMap = MapGrid(10, 10, 100)
    grid = GameMap.grid

    clock = pygame.time.Clock()
    totalUnits = 0
    character1 = Character('IronOcto.png', 100, 10, 1, 1, 1, 3,totalUnits) #image, hp, atk, mp, abilities, movement, range
    totalUnits += 1
    character2 = Character('NinjaOcto.png', 100, 10, 1, 1, 1, 3,totalUnits)
    totalUnits += 1
    character3 = Character('MegaOcto.png',100, 10, 1, 1, 1, 3,totalUnits)
    #player1 init
    player1 = grid[1][2]
    player1.changeCharacter(character1)
    player1.isfilled = True

    # player2 init
    player2 = grid[2][3]
    player2.changeCharacter(character2)
    player2.isfilled = True

    player3 = grid[5][4]
    player3.changeCharacter(character3)
    player3.isfilled = True

    P1 = Player(1)
    P2 = Player(2)

    P1.addMember(player1.character)
    P1.addMember(player3.character)
    P2.addMember(player2.character)
    print("P1: ")
    print(P1.getTeam())
    print("P2: ")
    print(P2.getTeam())
    theGame= GameSequence((P1, P2))
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
    printPlayer = False
    while not done:
        currentPlayer = theGame.getCurrentPlayer()

        if(not printPlayer):
            print(currentPlayer.player)
            print("TEAM: ")
            print(currentPlayer.getTeam)
            printPlayer = True

        # print("WHOS TURN: ")
        # print(currentPlayer.player)
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            elif event.type is pygame.KEYDOWN:
                if event.key is pygame.K_x: #MOVE
                    if currentPlayer.getChosenTile() is not None:
                        theGame.changeMode(0)
                if event.key is pygame.K_z: #ATTACK
                    if currentPlayer.getChosenTile() is not None:
                        theGame.changeMode(1)
                if event.key is pygame.K_c: #END TURN
                    print("ENDING TURN")
                    theGame.changeTurn()
                    theGame.startTurn()

                if event.key is pygame.K_q:
                    printPlayer = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # User clicks the mouse. Get the position
                pos = pygame.mouse.get_pos()
                # Change the x/y screen coordinates to grid coordinates
                column = pos[0] // GameMap.tileWidth
                row = pos[1] // GameMap.tileHeight
                clickedTile = grid[row][column]


                #if trying to attack


                if theGame.currentMode is 1:
                    if currentPlayer.getChosenTile() is not None:
                        if clickedTile.isfilled is True and currentPlayer.isInTeam(clickedTile.character) is False:
                            print("Attacking")
                            result = GameMap.attackCharacter(clickedTile, currentPlayer.getChosenTile())
                            if result:
                                theGame.changeMode(2)
                        else:
                            theGame.changeMode(2)
                            currentPlayer.getChosenTile().changeHighlighted(False)
                            currentPlayer.highlightedTile = None
                    else:
                        theGame.changeMode(2)
                        currentPlayer.getChosenTile().changeHighlighted(False)
                        currentPlayer.highlightedTile = None

                #trying to move
                elif theGame.currentMode is 0:
                    if currentPlayer.getChosenTile() is not None:
                        if grid[row][column].isfilled is False:
                            print("Moving")
                            result =  GameMap.moveCharacter(currentPlayer.getChosenTile(), currentPlayer.getChosenTile().posX,
                                              currentPlayer.getChosenTile().posY, column, row)
                            print(result)
                            if result:
                                theGame.changeMode(2)
                        else:
                            theGame.changeMode(2)
                            currentPlayer.getChosenTile().changeHighlighted(False)
                            currentPlayer.highlightedTile = None
                    else:
                        theGame.changeMode(2)
                        currentPlayer.getChosenTile().changeHighlighted(False)
                        currentPlayer.highlightedTile = None

                elif theGame.currentMode is 2:
                    print("IS FILLED")
                    #hes trying to click on a unit
                    currentTile = grid[row][column]
                    print("player's team: ")
                    print(currentPlayer.getTeam())
                    if currentPlayer.getChosenTile() is not None:
                        theGame.changeMode(2)
                        currentPlayer.getChosenTile().changeHighlighted(False)
                        currentPlayer.highlightedTile = None
                    elif currentPlayer.isInTeam(currentTile.character):
                            theGame.changeMode(2)
                            if currentPlayer.getChosenTile() is not None:
                                currentPlayer.getChosenTile().changeHighlighted(False)
                            currentPlayer.highlightedTile = None
                            currentTile.changeHighlighted(True)
                            currentPlayer.lookAtTile(currentTile)
                            theGame.changeMode(2)
                    elif clickedTile.isfilled is False:
                        print("did nothing")
                    else:
                        print("======================EDGE CASE==============================")
                        theGame.changeMode(2)
                        if(currentPlayer.getChosenTile() is not None):
                            currentPlayer.getChosenTile().changeHighlighted(False)
                        currentPlayer.highlightedTile = None

                else:
                    print("WTF")
                #  else:
                # if theGame.currentMode is not 2:
                #     if currentPlayer.getChosenTile() is not None:
                #         theGame.changeMode(2)
                #         currentPlayer.getChosenTile().changeHighlighted(False)
                #         currentPlayer.highlightedTile = None

                #     if GameMap.attackCharacter(player2, player1) is False:
                #         print("Not in range")
                # else:
                #     GameMap.moveCharacter(player1.posX, player1.posY, column, row)
                #     player1 = grid[row][column]
                print("Click ", pos, "Grid coordinates: ", row, column)

        # Set the screen background
        screen.fill((255,255,255))

        #drawing!
        # Draw the grid
        for row in range(GameMap.gridHeight):
            for column in range(GameMap.gridWidth):

                temp = grid[row][column]
                #Attack

                '''
                highlight the tiles within the attack range
                '''

                #Move
                if temp.isHighlighted() is True:
                    # print("HIGHLIGHTED")
                    temp.changeBackground('green.jpg')
                    screen.blit(temp.background,
                                     [GameMap.tileWidth * column, GameMap.tileHeight * row, GameMap.tileWidth,
                                      GameMap.tileHeight])
                    temp.changeBackground('Square with outline.png')
                else:
                    screen.blit(temp.background, ((column * GameMap.tileWidth), (row * GameMap.tileHeight)) )
                    #pygame.draw.rect(screen,(255,255,255),[GameMap.tileWidth * column,GameMap.tileHeight * row,GameMap.tileWidth,GameMap.tileHeight])

                if temp.isFilled() is True:
                    if(currentPlayer.isInTeam(temp.character)):
                        if(currentPlayer.player is 1):
                            temp.changeBackground('blue.png')
                        else:
                            temp.changeBackground('red.jpg')
                    screen.blit(temp.background, ((column * GameMap.tileWidth), (row * GameMap.tileHeight)))
                    screen.blit(temp.character.image, ((column * GameMap.tileWidth), (row * GameMap.tileHeight)))
                    temp.changeBackground('Square with outline.png')

        currentTile = currentPlayer.getChosenTile()
        if(currentTile is not None):
            if theGame.currentMode is 0:
                # print("in here")
                currentTile.changeBackground('blue.png')
                position = currentPlayer.getChosenTile().getPosition()
                # print("movement:")
                # print(currentPlayer.getChosenTile().character.movement)
                for i in range(currentTile.character.movement):
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] - i-1), GameMap.tileHeight * position[1],
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] + i+1), GameMap.tileHeight * position[1],
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * position[0], GameMap.tileHeight * (position[1] - i -1),
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * position[0], GameMap.tileHeight * (position[1] + i +1),
                                      GameMap.tileWidth, GameMap.tileHeight])

                for i in range(currentTile.character.movement - 1):
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] + i+1), GameMap.tileHeight * (position[1] - i -1),
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] + i+1), GameMap.tileHeight * (position[1] + i+1) ,
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] - i-1), GameMap.tileHeight * (position[1] + i+1),
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] - i-1), GameMap.tileHeight * (position[1] - i-1),
                                      GameMap.tileWidth, GameMap.tileHeight])

                currentTile.changeBackground('green.jpg')
                screen.blit(currentTile.background,
                            [GameMap.tileWidth * position[0], GameMap.tileHeight * position[1], GameMap.tileWidth,
                                  GameMap.tileHeight])

                screen.blit(currentTile.character.image,
                            ((position[0] * GameMap.tileWidth), (position[1] * GameMap.tileHeight)))
                currentTile.changeBackground('Square with outline.png')

            if theGame.currentMode is 1:
                # print("in here")
                currentTile.changeBackground('red.jpg')
                position = currentPlayer.getChosenTile().getPosition()
                # print("range:")
                # print(currentPlayer.getChosenTile().character.range)
                for i in range(currentTile.character.range):
                    screen.blit(currentTile.background,
                                     [GameMap.tileWidth * (position[0] - i -1), GameMap.tileHeight * position[1],
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] + i +1), GameMap.tileHeight * position[1],
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * position[0], GameMap.tileHeight * (position[1] - i-1),
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * position[0], GameMap.tileHeight * (position[1] + i+1),
                                      GameMap.tileWidth, GameMap.tileHeight])

                for i in range(currentTile.character.range - 1):
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] + i+1), GameMap.tileHeight * (position[1] - i-1),
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] + i+1), GameMap.tileHeight * (position[1] + i+1),
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] - i-1), GameMap.tileHeight * (position[1] + i+1),
                                      GameMap.tileWidth, GameMap.tileHeight])
                    screen.blit(currentTile.background,
                                [GameMap.tileWidth * (position[0] - i-1), GameMap.tileHeight * (position[1] - i -1),
                                      GameMap.tileWidth, GameMap.tileHeight])

                currentTile.changeBackground('green.jpg')
                screen.blit(currentTile.background,
                            [GameMap.tileWidth * position[0], GameMap.tileHeight * position[1], GameMap.tileWidth,
                                  GameMap.tileHeight])

                screen.blit(currentTile.character.image,
                            ((position[0] * GameMap.tileWidth), (position[1] * GameMap.tileHeight)))
                currentTile.changeBackground('Square with outline.png')

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

def main():
    startGame()


if __name__ == "__main__":
    main()