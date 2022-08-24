import pygame

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('nQueen')

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
PURPLE = (128, 0, 128)
YELLOW = (102, 102, 0)
MAGENTA = (0, 230, 230)


class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.color = WHITE
        self.total_rows = total_rows
        self.vis = 0

    def get_pos(self):
        return self.row, self.col

    def make_start(self):
        self.color = GREEN

    def make_end(self):
        self.color = RED

    def reset(self):
        self.color = WHITE

    def make_road(self):
        self.color = BLACK

    def make_path(self):
        self.color = BLUE

    def make_visited(self):
        self.color = MAGENTA

    def make_line(self):
        self.color = ORANGE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))



def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            grid[i].append(Node(i, j, gap, rows))

    return grid


def draw_line(win,  rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, BLACK, (i * gap, 0), (i * gap, width))
        pygame.display.update()


def draw(win, grid, rows, width):
    for row in grid:
        for node in row:
            node.draw(win)

    draw_line(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width//rows
    x, y = pos
    return x // gap, y // gap


def safe(grid, row, col):
    for i in range(row):
        if(grid[i][col].vis):
            return 0
    i = row
    j = col
    while i > -1 and j > -1:
        if(grid[i][j].vis):
            return 0
        i -=1
        j -=1
    i = row
    j = col
    while i > -1 and j < len(grid):
        if(grid[i][j].vis):
            return 0
        i -=1
        j +=1
    return 1
    
    
def nQueen(grid, row):
    if row >= len(grid):
        clk = pygame.time.Clock()
        clk.tick(1)
        return 0
    
    for col in range(len(grid)):
        grid[row][col].make_end()
        draw(WIN, grid, grid[0][0].total_rows, grid[0][0].width)
        if(safe(grid, row, col)):
            grid[row][col].make_start()
            grid[row][col].vis = 1
            draw(WIN, grid, grid[0][0].total_rows, grid[0][0].width)
            
            nQueen(grid, row+1)
            
            grid[row][col].reset()
            grid[row][col].vis = 0
            draw(WIN, grid, grid[0][0].total_rows, grid[0][0].width)
        
        grid[row][col].reset()
        draw(WIN, grid, grid[0][0].total_rows, grid[0][0].width)
            
        

def main(win, width):
    rows = 20
    grid = make_grid(rows, width)
    run = True
    draw(win, grid, rows, width)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    nQueen(grid, 0)


if __name__ == "__main__":
    main(WIN, WIDTH)


