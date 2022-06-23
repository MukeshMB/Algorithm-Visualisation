import pygame

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

WIDTH = 900
n = 30
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption('bfs visualisation')

class Node:
	def __init__(self, row, col, width):
		self.row = row
		self.col = col
		self.width = width
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []

	def make_start(self):
		self.color = GREEN

	def make_end(self):
		self.color = RED

	def reset(self):
		self.color = WHITE

	def make_barrier(self):
		self.color = BLACK
	
	def make_visited(self):
		self.color = MAGENTA
	
	def make_visit(self):
		self.color = BLUE

	def make_path(self):
		self.color = ORANGE

	def is_start(self):
		return self.color == GREEN

	def is_end(self):
		return self.color == RED
	
	def is_barrier(self):
		return self.color == BLACK

	def is_visited(self):
		return self.color == MAGENTA
	
	def is_visit(self):
		return self.color == BLUE
	
	def is_path(self):
		return self.color == ORANGE

	def draw(self):
		pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.width))

	def update_neighbors(self, grid):
		if self.col < n-1 and not grid[self.row][self.col+1].is_barrier():
			self.neighbors.append(grid[self.row][self.col+1])
		if self.row < n-1 and not grid[self.row+1][self.col].is_barrier():
			self.neighbors.append(grid[self.row+1][self.col])
		if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
			self.neighbors.append(grid[self.row][self.col-1])
		if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
			self.neighbors.append(grid[self.row-1][self.col])
		

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
	pygame.display.update()


def fill_neighbors(Grid):
	for list in Grid:
		for node in list:
			node.neighbors.clear()
			node.update_neighbors(Grid)


def pause():
	clk = pygame.time.Clock()
	clk.tick(60)


def spill(Grid):
	for list in Grid:
		for node in list:
			if node.is_visited() or node.is_visit():
				node.reset()


def dfs(start, node, end, Grid, vis, c, n):
	if n and c==n:
		n = c
		return 0

	for neig in node.neighbors:
		if neig != start and not vis[neig.row][neig.col]:
			if neig != end:
				vis[neig.row][neig.col] = True
				neig.make_visit()
				pause()
				draw_screen(Grid)
				dfs(start, neig, end, Grid, vis, c+1, n)
				neig.reset()
				draw_screen(Grid)
			else:
				n = c
				return 0

	return 0


def call_dfs(start, end, Grid):
	par = {}
	vis = []
	for row in Grid:
		list = []
		for col in row:
			list.append(False)
		vis.append(list)
	n = 0
	dfs(start, start, end, Grid, vis, 1, n)

def main():
	width = WIDTH // n
	Grid = make_grid(width)

	start = None
	end = None
	run = True

	print('-------------------------------------------')
	print('| press [spacebar] to start dfs traversal |')
	print('-------------------------------------------')

	while run:
		draw_screen(Grid)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				return -1
			
			if pygame.mouse.get_pressed()[0]:
				row, col = pygame.mouse.get_pos()
				row = row // width
				col = col // width
				spot = Grid[row][col]

				if not start and spot != end:
					start = spot
					start.make_start()
				
				elif not end and spot != start:
					end = spot
					end.make_end()
				
				elif spot != start and spot != end:
					spot.make_barrier()

			if pygame.mouse.get_pressed()[2]:
				row, col = pygame.mouse.get_pos()
				row = row // width
				col = col // width
				spot = Grid[row][col]
				if spot == start:
					start = None
				elif spot == end:
					end = None
				spot.reset()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					print('started bfs traversal')
					fill_neighbors(Grid)
					call_dfs(start, end, Grid)	

main()

