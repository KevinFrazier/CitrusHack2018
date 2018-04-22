import Tile

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
                temp = Tile(tilesize, tilesize, 0, 0, column, row, True)
                temp.changeBackground('Square.jpg')
                self.grid[row].append(temp)  # Append a cell

    def moveCharacter(self, player, pos1X, pos1Y, pos2X, pos2Y):
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