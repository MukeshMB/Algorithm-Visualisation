import random
import pygame

HEIGHT = 1200
WIDTH = 800
step = 20
n = WIDTH // step
m = HEIGHT // step

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Snake Game')

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

clk = pygame.time.Clock()

class Node:
    def __init__(self, row, col):
        self.x = row * step
        self.y = col * step
        self.width = step
        self.color = BLACK

    def make_green(self):
        self.color = GREEN
    
    def make_head(self):
        self.color = RED

    def reset(self):
        self.color = BLACK
    
    def make_food(self):
        self.color = BLUE
    
    def is_space(self):
        return self.color == BLACK

    def is_food(self):
        return self.color == BLUE

    def is_body(self):
        return self.color == GREEN
    
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))
        pygame.draw.line(WIN, BLACK, (self.x, self.y), (self.x+step, self.y))
        pygame.draw.line(WIN, BLACK, (self.x, self.y), (self.x, self.y+step))
        pygame.draw.line(WIN, BLACK, (self.x+step, self.y), (self.x+step, self.y+step))
        pygame.draw.line(WIN, BLACK, (self.x, self.y+step), (self.x+step, self.y+step))
        pygame.display.update()
        

def add(Grid):
    x = 0
    y = 0
    Grid[x][y].make_green()
    Grid[x][y+1].make_green()
    Grid[x][y+2].make_head()
    Grid[x][y].draw()
    Grid[x][y+1].draw()
    Grid[x][y+2].draw()
    snake = [Grid[x][y], Grid[x][y+1], Grid[x][y+2]]
    return snake
    
                    
def main():
    run = True
    Grid = []
    for i in range(m):
        Grid.append([])
        for j in range(n):
            Grid[i].append(Node(i, j))
            
    snake = add(Grid)
    x = 0
    y = 2
    dir = '' 
    
    x0 = -1
    y0 = -1
    speed = 20
    while run:
        clk.tick(speed)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and dir != 'd':
                    dir = 'u'
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and dir != 'u':
                    dir = 'd'
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and dir != 'l':
                    dir = 'r'
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and dir != 'r':
                    dir = 'l'
        
        if x0 == -1:
            x0 = random.randint(0, m-1)
            y0 = random.randint(0, n-1)
            if(Grid[x0][y0].is_space()):
                Grid[x0][y0].make_food()
                Grid[x0][y0].draw()
        
        
        if dir == 'u':
            y -= 1
            if y < 0:
                y = n - 1
        if dir == 'd':
            y += 1
            if y == n:
                y = 0
        if dir == 'l':
            x -= 1
            if x < 0:
                x = m - 1
        if dir == 'r':
            x += 1
            if x == m:
                x = 0
        
        
        if dir != '':
            if Grid[x][y].is_food():
                x0 = -1
            
            elif Grid[x][y].is_body():
                while snake[0] != Grid[x][y]:
                    snake[0].reset()
                    snake[0].draw()
                    snake.pop(0)
                snake[0].reset()
                snake[0].draw()
                snake.pop(0)
            
            elif not Grid[x][y].is_food():
                snake[0].reset()
                snake[0].draw()
                snake.pop(0)
                        
            snake[-1].make_green()
            snake[-1].draw()
            Grid[x][y].make_head()
            Grid[x][y].draw()
            snake.append(Grid[x][y])
            
        

if __name__ == "__main__":
    main()


