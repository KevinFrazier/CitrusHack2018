from Character import Character
class Player:
    def __init__(self, ID):
        self.player = ID
        self.team = []
        self.isTurn = False
        self.highlightedChar = None

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
    def lookAtChar(self,character):
        self.highlightedChar = character