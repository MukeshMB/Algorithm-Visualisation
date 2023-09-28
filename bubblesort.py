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
    def __init__(self, row, y, color):
        self.x = row * width
        self.y = y
        self.color = color
    
    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, width, HEIGHT - self.y))
        pygame.draw.rect(WIN, BLACK, (self.x, 0, width, self.y))
        pygame.draw.line(WIN, BLACK, (self.x + width, 0), (self.x + width, HEIGHT))
        pygame.draw.line(WIN, BLACK, (self.x, 0), (self.x, HEIGHT))
        pygame.display.update()
        
        

def draw_all(Grid):
    for node in Grid:
        node.draw()
        
        
def bubblesort(Grid):
    for i in range(len(Grid)):
        for j in range(len(Grid)-i-1):
            if Grid[j].y < Grid[j+1].y:
                temp = Grid[j+1].y
                Grid[j+1].y = Grid[j].y
                Grid[j].y = temp
                Grid[j].color = RED
                Grid[j].draw()
                Grid[j].color = BLUE
                Grid[j].draw()
        Grid[len(Grid)-1-i].color = GREEN
        Grid[len(Grid)-1-i].draw()
        
        
def main():
    Grid = []
    for i in range(N):
        Grid.append(block(i, HEIGHT, BLACK))

    print('-------------------------------------------------------------------------------------')
    print('| Draw Vertical Bars [BLUE] and then press [SPACEBAR] to start Bubblesort Algorithm |')
    print('-------------------------------------------------------------------------------------')

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                    
            elif pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                x = x // width
                if x < N:
                    Grid[x].y = y
                    Grid[x].color = BLUE
                    Grid[x].draw()
            
            elif pygame.mouse.get_pressed()[1]:
                x, y = pygame.mouse.get_pos()
                x = x // width
                if x < N:
                    Grid[x].y = HEIGHT
                    Grid[x].color = BLACK
                    Grid[x].draw()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bubblesort(Grid)
                    draw_all(Grid)
        
        
if __name__ == "__main__":
    main()
        
