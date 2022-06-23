from pickle import TRUE
import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


WIDTH = 900
n = 5
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('nQueen visualisation')

class Node:
	def __init__(self, row, col, width):
		self.row = row
		self.col = col
		self.width = width
		self.x = row * width
		self.y = col * width
		self.color = WHITE

	def make_start(self):
		self.color = GREEN

	def make_end(self):
		self.color = RED

	def reset(self):
		self.color = WHITE

	def make_visit(self):
		self.color = RED

	def draw(self):
		pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))


def make_grid(width):
	Grid = []
	for i in range(0, n):
		Grid.append([])
		for j in range(0, n):
			Grid[i].append(Node(i, j, width))

	return Grid


def draw_screen(Grid):
	for list in Grid:
		for node in list:
			node.draw()
			pygame.draw.line(WIN, (0, 0, 0), (node.x, 0), (node.x, WIDTH))
			pygame.draw.line(WIN, (0, 0, 0), (0, node.y), (WIDTH, node.y))
	pause()
	pygame.display.update()


def pause():
	clk = pygame.time.Clock()
	clk.tick(60)

	
def nQueen(Grid, ld, rd, cl, rw, row):
	if row >= n:
		print('\n------------------------------------------------------')
		print('| press [spacebar] to find another possible solution |')
		print('------------------------------------------------------')
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 0
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						return 0
		 
	for col in range(0, n):
		Grid[col][row].make_start()
		draw_screen(Grid)

		if not ld[col-row+n-1] and not rd[col+row] and not cl[row] and not rw[col]:
			ld[col-row+n-1] = True
			rd[col+row] = True
			cl[row] = True
			rw[col] = True
			Grid[col][row].make_visit()
			draw_screen(Grid)

			nQueen(Grid, ld, rd, cl, rw, row+1)

			ld[col-row+n-1] = False
			rd[col+row] = False
			cl[row] = False
			rw[col] = False
			Grid[col][row].reset()
			draw_screen(Grid)
		
		else:
			Grid[col][row].reset()
			draw_screen(Grid)
		
	
		


def main():
	width = WIDTH // n
	Grid = make_grid(width)

	start = None
	end = None
	run = True

	print('\n-----------------------------------')
	print('| press [spacebar] to start nQueen |')
	print('-----------------------------------')

	while run:
		draw_screen(Grid)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return -1
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					ld = [False] * (2*n + 1)
					rd = [False] * (2*n + 1)
					cl = [False] * n
					rw = [False] * n
					nQueen(Grid, ld, rd, cl, rw, 0)
					print('ends')
					
main()

