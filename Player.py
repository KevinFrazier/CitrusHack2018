from Character import Character
from Tile import Tile
class Player:
    def __init__(self, ID):
        self.player = ID
        self.team = []
        self.isTurn = False
        self.highlightedTile = None

    def addMember(self, character):
        if isinstance(character, Character):
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
        print("checking...")
        if isinstance(character, Character):
            print("is character")
            for member in self.team:
                if member is character:
                    print("found!")
                    return True

        return False
    def getTeam(self):
        return self.team

    def lookAtTile(self,tile):
        # if(isinstance(tile,Tile)):
        if(isinstance(tile,Tile)):
            self.highlightedTile = tile
            print("highlighted: ")
            print(tile)
            return True
        return False

    def getChosenTile(self):
        return self.highlightedTile