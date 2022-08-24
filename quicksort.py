import pygame

HEIGHT = 1200
WIDTH = 800
WIN = pygame.display.set_mode((HEIGHT, WIDTH))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class block:
    def __init__(self, row, y, width, color):
        self.x = row * width
        self.y = y
        self.color = color
        self.width = width
    
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, WIDTH - self.y))
        pygame.draw.rect(WIN, BLACK, (self.x, 0, self.width, self.y))
        pygame.draw.line(WIN, BLACK, (self.x + self.width, 0), (self.x + self.width, WIDTH))
        pygame.draw.line(WIN, BLACK, (self.x, 0), (self.x, WIDTH))
        pygame.display.update()
        
        

def draw_all(Grid):
    for node in Grid:
        node.draw()
        
        
def partition(array, low, high):
    pivot = array[high]
    array[high].color = RED
    array[high].draw()   
    i = low - 1
    for j in range(low, high):
        if array[j].y <= pivot.y:
            i += 1
            (array[i].y, array[j].y) = (array[j].y, array[i].y)
            array[i].draw()
            array[j].draw()
            
  
    (array[i + 1].y, array[high].y) = (array[high].y, array[i + 1].y)
    array[i].draw()
    array[j].draw()
    array[high].color = BLUE
    array[high].draw()    
    return i + 1
  
  
def quick_sort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)

    
  
     
        

def main():
    n = 200
    width = HEIGHT // n
    Grid = []
    clk = pygame.time.Clock()
    for i in range(n+1):
        Grid.append(block(i, WIDTH, width, BLACK))
    
    while True:
        for event in pygame.event.get():
            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x = x // width
                Grid[x].y = y
                Grid[x].color = BLUE
                Grid[x].draw()
                
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    quick_sort(Grid, 0, n)
                    draw_all(Grid)
        
        

main()
        