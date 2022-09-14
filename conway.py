import pygame

HEIGHT = 1200
WIDTH = 800
step = 20
n = WIDTH // step
m = HEIGHT // step

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Conway game of life')

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)


class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * step
        self.y = col * step
        self.width = step
        self.color = BLACK
        self.neighbour = []

    def make_live(self):
        self.color = GREEN

    def make_dead(self):
        self.color = BLACK
    
    def is_alive(self):
        return (self.color == GREEN)

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))
        pygame.draw.line(WIN, BLACK, (0, self.y), (HEIGHT, self.y))
        pygame.draw.line(WIN, BLACK, (self.x, 0), (self.x, WIDTH))
        pygame.display.update()

    def update_neighbours(self, grid):
        if (self.row < m - 1) and (grid[self.row + 1][self.col].is_alive()):
            self.neighbour.append(grid[self.row + 1][self.col])
            
        if (self.row > 0) and (grid[self.row - 1][self.col].is_alive()):
            self.neighbour.append(grid[self.row - 1][self.col])
            
        if (self.col < n - 1) and (grid[self.row][self.col + 1].is_alive()):
            self.neighbour.append(grid[self.row][self.col + 1])
            
        if (self.col > 0) and (grid[self.row][self.col - 1].is_alive()):
            self.neighbour.append(grid[self.row][self.col - 1])
            
        if (self.row > 0) and (self.col > 0) and (grid[self.row-1][self.col-1].is_alive()):
           self.neighbour.append(grid[self.row-1][self.col-1]) 
           
        if (self.row > 0) and (self.col < n-1) and (grid[self.row-1][self.col+1].is_alive()):
           self.neighbour.append(grid[self.row-1][self.col+1]) 
           
        if (self.row < m-1) and (self.col > 0) and (grid[self.row+1][self.col-1].is_alive()):
           self.neighbour.append(grid[self.row+1][self.col-1]) 
           
        if (self.row < m-1) and (self.col < n-1) and (grid[self.row+1][self.col+1].is_alive()):
           self.neighbour.append(grid[self.row+1][self.col+1]) 


def gof(Grid):
    run = True
    while run:
        x = 0
        for node in Grid:
            for each in node:
                each.neighbour.clear()
                each.update_neighbours(Grid)
        
        for node in Grid:
            for each in node:
                if(each.is_alive()):
                    if(len(each.neighbour)<2):
                        each.make_dead()
                        each.draw()
                    elif(len(each.neighbour)>3):
                        each.make_dead()
                        each.draw()
                    else:
                        x += 1
                else:
                    if(len(each.neighbour)==3):
                        each.make_live()
                        each.draw()
                        x += 1
        if x == 0:
            run = False
        
                           
def main():
    run = True
    Grid = []
    for i in range(m):
        Grid.append([])
        for j in range(n):
            Grid[i].append(Node(i, j))
            
            
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row = pos[0] // step
                col = pos[1] // step
                Grid[row][col].make_live()
                Grid[row][col].draw()
                
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row = pos[0] // step
                col = pos[1] // step
                Grid[row][col].make_dead()
                Grid[row][col].draw()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('Conway Game of Life Started')
                    gof(Grid)
                    run = False


if __name__ == "__main__":
    main()


