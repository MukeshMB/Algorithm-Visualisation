import pygame

# FRAME CONSTRUCTION
def init_display():
	WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	WIDTH = 9 * pygame.display.Info().current_w // 10
	HEIGHT = 9 * pygame.display.Info().current_h // 10
	pygame.quit()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Bubblesort')

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
    
    def reset(self):
        self.color = BLUE

    def draw(self, x):
        x = x * width
        pygame.draw.rect(WIN, self.color, (x, self.y, width, HEIGHT-self.y))
        pygame.draw.rect(WIN, BLACK, (x, 0, width, self.y))
        pygame.draw.line(WIN, BLACK, (x + width, 0), (x + width, HEIGHT))
        pygame.draw.line(WIN, BLACK, (x, 0), (x, HEIGHT))
        pygame.display.update()
        
        
def selectionsort(Grid):
    for i in range(len(Grid)):
        Grid[i].make_start()
        Grid[i].draw(i)

        for j in range(i, len(Grid)):
            if(Grid[i].y < Grid[j].y):
                Grid[j].make_end()
                Grid[j].draw(j)

                Grid[i].y, Grid[j].y = Grid[j].y, Grid[i].y

                Grid[j].reset()
                Grid[j].draw(j)
                Grid[i].draw(i)
                
            
def main():
    Grid = []

    for i in range(N):
        Grid.append(block(WIDTH, BLACK))
    
    print('-----------------------------------------------------------------------------------------')
    print('| Draw Vertical Bars [BLUE] and then press [SPACEBAR] to start Selection sort Algorithm |')
    print('-----------------------------------------------------------------------------------------')
    
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
                    selectionsort(Grid)

                    for i in range(len(Grid)):
                        Grid[i].draw(i)             
        
        
if __name__ == "__main__":
    main()
        
