import pygame

# FRAME CONSTRUCTION
def init_display():
	WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	WIDTH = 9 * pygame.display.Info().current_w // 10
	HEIGHT = 9 * pygame.display.Info().current_h // 10
	pygame.quit()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('CONWAY GAME OF LIFE')

	return WIN, WIDTH, HEIGHT

# INIT FRAME
WIN, WIDTH, HEIGHT = init_display()

#INIT @Param
step = 30
n = WIDTH // step
m = HEIGHT // step

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
        pygame.draw.line(WIN, BLACK, (0, self.y), (WIDTH, self.y))
        pygame.draw.line(WIN, BLACK, (self.x, 0), (self.x, HEIGHT))
        pygame.display.update()

    def update_neighbours(self, grid):
        if (self.row < n - 1) and (grid[self.row + 1][self.col].is_alive()):
            self.neighbour.append(grid[self.row + 1][self.col])
            
        if (self.row > 0) and (grid[self.row - 1][self.col].is_alive()):
            self.neighbour.append(grid[self.row - 1][self.col])
            
        if (self.col < m - 1) and (grid[self.row][self.col + 1].is_alive()):
            self.neighbour.append(grid[self.row][self.col + 1])
            
        if (self.col > 0) and (grid[self.row][self.col - 1].is_alive()):
            self.neighbour.append(grid[self.row][self.col - 1])
            
        if (self.row > 0) and (self.col > 0) and (grid[self.row-1][self.col-1].is_alive()):
           self.neighbour.append(grid[self.row-1][self.col-1]) 
           
        if (self.row > 0) and (self.col < m-1) and (grid[self.row-1][self.col+1].is_alive()):
           self.neighbour.append(grid[self.row-1][self.col+1]) 
           
        if (self.row < n-1) and (self.col > 0) and (grid[self.row+1][self.col-1].is_alive()):
           self.neighbour.append(grid[self.row+1][self.col-1]) 
           
        if (self.row < n-1) and (self.col < m-1) and (grid[self.row+1][self.col+1].is_alive()):
           self.neighbour.append(grid[self.row+1][self.col+1]) 


def gof(Grid):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

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
                    if(len(each.neighbour)==3):
                        each.make_live()
                        each.draw()
        
                           
def main():
    run = True
    Grid = []
    for i in range(n):
        Grid.append([])
        for j in range(m):
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
                if row < n and col < m:
                    Grid[row][col].make_live()
                    Grid[row][col].draw()
                
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row = pos[0] // step
                col = pos[1] // step
                if row < n and col < m:
                    Grid[row][col].make_dead()
                    Grid[row][col].draw()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print('Conway Game of Life Started')
                    gof(Grid)
                    run = False


if __name__ == "__main__":
    main()

