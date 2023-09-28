import pygame
import random

# FRAME CONSTRUCTION
def init_display():
	WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	WIDTH = pygame.display.Info().current_w
	HEIGHT = 9 * pygame.display.Info().current_h // 10
	pygame.quit()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Quicksort')

	return WIN, WIDTH, HEIGHT

# INIT FRAME
WIN, WIDTH, HEIGHT = init_display()

# INIT @params
width = 5
N = WIDTH // width

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE = (64, 224, 208)
PURPLE = (128, 0, 128)


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
    
    def make_large(self):
        self.color = PURPLE
    
    def make_small(self):
        self.color = TURQUOISE

    def draw(self, x):
        x = x * width
        pygame.draw.rect(WIN, self.color, (x, self.y, width, HEIGHT-self.y))
        pygame.draw.rect(WIN, BLACK, (x, 0, width, self.y))
        pygame.draw.line(WIN, BLACK, (x + width, 0), (x + width, HEIGHT))
        pygame.draw.line(WIN, BLACK, (x, 0), (x, HEIGHT))
        pygame.display.update()
        
        
def partition(arr, low, high):
    index = random.randint(low, high)
    pivot = arr[index]
    pivot.make_end()
    pivot.draw(index)

    arr[high].y, pivot.y = pivot.y, arr[high].y
    arr[high].make_end()
    arr[high].draw(high)

    pivot.reset()
    pivot.draw(index)

    i = low
    for j in range(low, high):
        if arr[j].y > arr[high].y:
            arr[i].y, arr[j].y = arr[j].y, arr[i].y
            arr[i].make_small()
            arr[i].draw(i)
            arr[j].make_large()
            arr[j].draw(j)

            i += 1
        
        else:
            if j != index:
                arr[j].make_large()
                arr[j].draw(j)
    
    arr[i].y, arr[high].y = arr[high].y, arr[i].y
    arr[i].make_start()
    arr[i].draw(i) 

    for j in range(low, high+1):
        if j != i:
            arr[j].reset()
            arr[j].draw(j)

    return i
  
  
def quickSort(arr, low, high):
    if low <= high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    
def main():
    Grid = []

    for i in range(N):
        Grid.append(block(WIDTH, BLACK))
    
    print('-----------------------------------------------------------------------------------')
    print('| Draw Vertical Bars [BLUE] and then press [SPACEBAR] to start QuicSort Algorithm |')
    print('-----------------------------------------------------------------------------------')
    
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
                    quickSort(Grid, 0, N-1)

                    for i in range(len(Grid)):
                        Grid[i].draw(i)
        

if __name__ == "__main__":
    main()
   
