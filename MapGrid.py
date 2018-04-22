from Tile import Tile

class MapGrid:
    def __init__(self, h, w, tilesize):
        self.gridHeight = h
        self.gridWidth = w
        self.tileWidth = tilesize
        self.tileHeight = tilesize

        self.grid = []
        for row in range(self.gridHeight):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(self.gridWidth):
                temp = Tile(tilesize, tilesize, 0, 0, column, row, True)
                temp.changeBackground('Square.jpg')
                self.grid[row].append(temp)  # Append a cell

    def moveCharacter(self, player, fromX, fromY, toX, toY):
        destination = self.grid[toY][toX]
        source = self.grid[fromY][fromX]
        if destination.isfilled is True:
            return -1
        elif player.character.movement < (abs(fromX - toX) + abs(fromY - toY)):
            return 0
        else:
            destination.changeCharacter(source.character)
            destination.isfilled = True
            source.changeCharacter(0)
            source.isfilled = False
            return 1

    # attackCharacter(whats attacking, whats being attacked)
    def attackCharacter(self, victim, attacker):
        # in range
        if attacker.character.range >= (abs(victim.posX - attacker.posX) + abs(victim.posY - attacker.posY)):
            # attack
            victim.character.hp -= attacker.character.atk
            if victim.character.hp <= 0:
                self.deleteCharacter(victim)
                print("DEAD")
            else:
                print("Attacker's Atk: ", attacker.character.hp)
                print("Victim's HP: ", victim.character.hp)
            return True
        else:
            return False

    def deleteCharacter(self, victim):
        victim.changeCharacter(0)
        victim.isfilled = False
