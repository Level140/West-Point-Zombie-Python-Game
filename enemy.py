import pygame

class Enemy:
    
    xLoc = 0
    yLoc = 0
    health = 100
	
    def __init__(self):
        self.rect = pygame.Rect(0, 0, 50, 50)
        self.setLoc(175, 100)
        
    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
    
    def track(self, pLoc):
        ax = pLoc[0]
        ay = pLoc[1]
        bx = self.rect.x
        by = self.rect.y
        stepx = (bx-ax)
        stepy = (by-ay)
        self.move(stepx, stepy)
    
    def setLoc(self, x, y):
        self.xLoc = x
        self.yLoc = y
	
    def getLoc(self):
        return (self.xLoc, self.yLoc)
        



if __name__ == "__main__":
    pass
