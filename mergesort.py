import pygame

# FRAME CONSTRUCTION
def init_display():
	WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	WIDTH = pygame.display.Info().current_w
	HEIGHT = 9 * pygame.display.Info().current_h // 10
	pygame.quit()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('Mergesort')

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


class block:
    def __init__(self, y, color):
        self.y = y
        self.color = color
    
    def make_start(self):
        self.color = GREEN
    
    def make_end(self):
        self.color = RED

    def draw(self, x):
        x = x * width
        pygame.draw.rect(WIN, self.color, (x, self.y, width, HEIGHT-self.y))
        pygame.draw.rect(WIN, BLACK, (x, 0, width, self.y))
        pygame.draw.line(WIN, BLACK, (x + width, 0), (x + width, HEIGHT))
        pygame.draw.line(WIN, BLACK, (x, 0), (x, HEIGHT))
        pygame.display.update()


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = []
    R = []

    for i in range(n1):
        L.append(arr[l + i].y)
        arr[l + i].make_end()
        arr[l + i].draw(l+i)
    
    for j in range(n2):
        R.append(arr[m + 1 + j].y)
        arr[m + 1 + j].make_end()
        arr[m + 1 + j].draw(m+1+j)

    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = l	 # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] >= R[j]:
            arr[k].y = L[i]
            i += 1
        else:
            arr[k].y = R[j]
            j += 1
        
        arr[k].make_start()
        arr[k].draw(k)
        k += 1
            
    while i < n1:
        arr[k].y = L[i]
        arr[k].make_start()
        arr[k].draw(k)
        i += 1
        k += 1

    while j < n2:
        arr[k].y = R[j]
        arr[k].make_start()
        arr[k].draw(k)
        j += 1
        k += 1


def mergeSort(arr, l, r):
	if l < r:
		m = (l+r) // 2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
        
       
def main():
    Grid = []

    for i in range(N):
        Grid.append(block(WIDTH, BLACK))
    
    print('-------------------------------------------------------------------------------------')
    print('| Draw Vertical Bars [BLUE] and then press [SPACEBAR] to start Mergesort Algorithm |')
    print('-------------------------------------------------------------------------------------')
    
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
                    mergeSort(Grid, 0, N-1)

                    for i in range(len(Grid)):
                        Grid[i].draw(i)
        
        
if __name__ == "__main__":
    main()
        
