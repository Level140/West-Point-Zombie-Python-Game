import pygame

class Player:
    
    xLoc = 0
    yLoc = 0
    
    def __init__(self):
        self.rect = pygame.Rect(175, 100, 50, 50)
        self.setLoc(175, 100)

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    def setLoc(self, x, y):
        self.xLoc = x
        self.yLoc = y
	
    def getLoc(self):
		return (self.xLoc, self.yLoc)
        



if __name__ == "__main__":
    pass
