import pygame
class Map:
    maps=[

#Start Map
[
"XXXXXXXXXXXXXXXXXXXXXXXXXXX",
"X     X                   X",
"X                         X",
"X       XXXXXXXXXXXX      X",
"X                         X",
"X       XXXXXXXXXXX       X",
"X            X     X  X   X",
"X              X    X  X  X",
"X     X              X  X X",
"X                     X  XX",
"X     X       X           X",
"X                  X      X",
"X     XXXXXXXXXXXXXX      X",
"X                         X",
"XXXXXXXXXXXXXXXXXXXXXXXXXXX"
],


[
" "
]
]
    
    def __init__(self):
        pass
        
    def drawMap(self,num):
      rectArray=[]
      for y in range(0,750/50):
        for x in range(0,1350/50):
          if self.maps[0][y][x]=="X":
            rectArray.append(pygame.Rect(x*50, y*50, 50, 50))
      return rectArray


    def getSize(self):
        return self.size

