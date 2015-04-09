import pygame

class Player:
    
    xLoc = 0
    yLoc = 0
    
    def __init__(self):
        self.rect = pygame.Rect(176, 100, 50, 50)
        self.setLoc(176, 100)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    def setLoc(self, x, y):
        self.xLoc = x
        self.yLoc = y
	
    def getLoc(self):
		return (self.rect.x, self.rect.y)
       

    class Weapon:
        damage = 0
        def __init__(self, dam):
            self.damage = dam

        def getDamage(self):
            return self.damage()

        
        



if __name__ == "__main__":
    pass
