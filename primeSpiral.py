from cmath import sqrt
import pygame

HEIGHT = 700
WIDTH = 700
WIN  = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Prime Spiral')

RED = (255, 170, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Node:
    def __init__(self, row, col, width, color):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = color
    
    def draw(self):
        pygame.draw.circle(WIN, self.color, (self.x, self.y), 5)
    


def fill_node(width):
    Grid = []
    for i in range(HEIGHT//width):
        Grid.append([])
        for j in range(WIDTH//width):
            Grid[i].append(Node(i, j, width, WHITE))
    
    return Grid

    
def draw_screen(Grid):
    for row in Grid:
        for node in row:
            node.draw()
            pygame.display.update() 


def prime(x):
    if(x==1):
        return False
    if(x<4):
        return True
    if(x%2==0):
        return False
    for i in range(3, x-1, 2):
        if(x%i==0):
            return False
    return True

    

def main():
    width = 20
    midx = HEIGHT // width // 2
    midy = WIDTH // width // 2
    n = 4 * midx * midy
    Grid = fill_node(width)
    clk = pygame.time.Clock()
    
    dir = 0
    step = 1
    init = 0
    i = 1
    while i <= n:
        Grid[midx][midy].draw()
        pygame.display.update()
        clk.tick(50)
        if(prime(i)):
            Grid[midx][midy].color = BLUE
            Grid[midx][midy].draw()
            pygame.display.update()
            
        if(dir==0):
            if(init==step):
                dir = 1
                init = 0
            else:
                init += 1
                midx += 1
                i += 1
                
            
        elif(dir==1):
            if(init==step):
                dir = 2
                step += 1
                init = 0
            else:
                init += 1
                midy -=1
                i += 1
                
        
        elif(dir==2):
            if(init==step):
                dir = 3
                init = 0
            else:
                init += 1
                midx -= 1
                i += 1
                
        
        elif(dir==3):
            if(init==step):
                dir = 0
                step += 1
                init = 0
            else:
                init += 1
                midy += 1
                i += 1
                
                
                
        
main()