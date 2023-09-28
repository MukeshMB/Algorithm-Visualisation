import pygame

# FRAME CONSTRUCTION
def init_display():
	WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	WIDTH = pygame.display.Info().current_w
	HEIGHT = 9 * pygame.display.Info().current_h // 10
	pygame.quit()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Insertionsort')

	return WIN, WIDTH, HEIGHT

# INIT FRAME
WIN, WIDTH, HEIGHT = init_display()

# INIT @params
width = 5
N = WIDTH // width

# INIT Colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
PURPLE = (128, 0, 128)
YELLOW = (102, 102, 0)
MAGENTA = (102, 102, 105)


class block:
    def __init__(self, y, color):
        self.y = y
        self.color = color
    
    def make_start(self):
        self.color = GREEN
    
    def make_end(self):
        self.color = RED
    
    def make_visit(self):
        self.color = MAGENTA
    
    def make_visited(self):
        self.color = TURQUOISE
    
    def draw(self, x):
        x = x * width
        pygame.draw.rect(WIN, self.color, (x, self.y, width, HEIGHT-self.y))
        pygame.draw.rect(WIN, BLACK, (x, 0, width, self.y))
        pygame.draw.line(WIN, BLACK, (x + width, 0), (x + width, HEIGHT))
        pygame.draw.line(WIN, BLACK, (x, 0), (x, HEIGHT))
        pygame.display.update()
        

def insertionsort(Grid):
    for i in range(len(Grid)):
        j = i
        Grid[i].make_end()
        Grid[i].draw(i)
        temp = Grid[i].y

        while(j>0 and Grid[j-1].y > temp):
            Grid[j].y = Grid[j-1].y
            Grid[j].make_start()
            Grid[j].draw(j)
            Grid[j-1].make_visited()
            Grid[j-1].draw(j-1)
            j -= 1

        Grid[j].y = temp
        Grid[j].make_start()
        Grid[j].draw(j)
        Grid[i].make_start()
        Grid[i].draw(i)
        
        
def main():
    Grid = []

    for i in range(N):
        Grid.append(block(WIDTH, BLACK))
    
    print('------------------------------------------------------------------------------------')
    print('| Draw Vertical Bars [BLUE] and then press [SPACEBAR] to start Insertion Algorithm |')
    print('------------------------------------------------------------------------------------')
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x = x // width
                if x < N:
                    Grid[x].y = y
                    Grid[x].color = BLUE
                    Grid[x].draw(x)
                   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    insertionsort(Grid)

                    for i in range(len(Grid)):
                        Grid[i].draw(i)
        
        
if __name__ == "__main__":
    main()
        
