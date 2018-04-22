import GameSequence
import Game

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