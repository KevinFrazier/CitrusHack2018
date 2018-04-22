from Player import Player
class GameSequence:
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

    def getCurrentPlayer(self):
        return self.players[self.currentTurn]

    def changeTurn(self):
        self.players[self.currentTurn].changeTurn(False)
        self.currentTurn += 1
        self.currentTurn = self.currentTurn % len(self.players)

    def endTurn(self):
        self.players[self.currentTurn].changeTurn(False)
