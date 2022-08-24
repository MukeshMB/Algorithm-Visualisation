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
        pygame.draw.rect(WIN, self.color, (self.x, self.y,
                         self.width, WIDTH - self.y))
        pygame.draw.rect(WIN, BLACK, (self.x, 0, self.width, self.y))
        pygame.draw.line(WIN, BLACK, (self.x + self.width, 0),
                         (self.x + self.width, WIDTH))
        pygame.draw.line(WIN, BLACK, (self.x, 0), (self.x, WIDTH))
        pygame.display.update()


def draw_all(Grid):
    for node in Grid:
        node.draw()


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i].y
    
    
    for j in range(0, n2):
        R[j] = arr[m + 1 + j].y

    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = l	 # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k].y = L[i]
            arr[k].draw()
            i += 1
        else:
            arr[k].y = R[j]
            arr[k].draw()
            j += 1
            k += 1
            
    while i < n1:
        arr[k].y = L[i]
        arr[k].draw()
        i += 1
        k += 1

    while j < n2:
        arr[k].y = R[j]
        arr[k].draw()
        j += 1
        k += 1



def mergeSort(arr, l, r):
	if l < r:
		m = l+(r-l)//2
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)
        
       

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
                    mergeSort(Grid, 0, n)
                    draw_all(Grid)
        
        

main()
        