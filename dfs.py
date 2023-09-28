import pygame

# FRAME CONSTRUCTION
def init_display():
	WIN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
	WIDTH = 9 * pygame.display.Info().current_w // 10
	HEIGHT = 9 * pygame.display.Info().current_h // 10
	pygame.quit()
	WIN = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption('DFS TRAVERSAL')

	return WIN, WIDTH, HEIGHT


# INIT FRAME
WIN, WIDTH, HEIGHT = init_display()

# INIT @params
M = 50
width = WIDTH // M
N = HEIGHT // width

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


class Node:
	def __init__(self, row, col):
		self.row = row
		self.col = col
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
		pygame.draw.rect(WIN, self.color, (self.x, self.y, width, width))
		pygame.draw.line(WIN, (0, 0, 0), (self.x, 0), (self.x, HEIGHT))
		pygame.draw.line(WIN, (0, 0, 0), (0, self.y), (WIDTH, self.y))

	def update_neighbors(self, grid):
		if self.col < N-1 and not grid[self.row][self.col+1].is_barrier():
			self.neighbors.append(grid[self.row][self.col+1])
		if self.row < M-1 and not grid[self.row+1][self.col].is_barrier():
			self.neighbors.append(grid[self.row+1][self.col])
		if self.col > 0 and not grid[self.row][self.col-1].is_barrier():
			self.neighbors.append(grid[self.row][self.col-1])
		if self.row > 0 and not grid[self.row-1][self.col].is_barrier():
			self.neighbors.append(grid[self.row-1][self.col])
		

def make_grid():
	Grid = []
	for i in range(M):
		Grid.append([])
		for j in range(N):
			Grid[i].append(Node(i, j))

	return Grid


def fill_neighbors(Grid):
	for list in Grid:
		for node in list:
			node.neighbors.clear()
			node.update_neighbors(Grid)


def spill(Grid):
	for list in Grid:
		for node in list:
			if node.is_visited() or node.is_visit():
				node.reset()


def dfs(start, end, Grid):
	vis = []
	for row in Grid:
		list = []
		for col in row:
			list.append(False)
		vis.append(list)

	stack = [start]
	vis[start.row][start.col] = True

	par = {}
	Path = []
	curr = -1
	while len(stack):
		node = stack[-1]
		stack.remove(node)

		if not node.is_start() and not node.is_end():
			node.make_visited()
			node.draw()
		
		if node.is_end():
			key = end
			n = 0
			while key != start:
				key = par[key]
				n += 1
			if n < curr or curr == -1:
				curr = n
				for each in Path:
					each.make_visit()
					each.draw()
				
				Path.clear()
				key = end
				while key != start:
					key = par[key]
					if not key.is_start():
						Path.append(key)
						key.make_path()
						key.draw()

		for each in node.neighbors:
			if not vis[each.row][each.col]:
				stack.append(each)
				vis[each.row][each.col] = True
				par[each] = node
				if not each.is_start() and not each.is_end():
					each.make_visit()
					each.draw()
		
		pygame.display.update()


def main():
	Grid = make_grid()
	for list in Grid:
			for each in list:
				each.draw()

	pygame.display.update()

	start = None
	end = None
	run = True

	print('--------------------------------------------------------------------------------------------------------------------')
	print('| SELECT START NODE [GREEN], END NODE [RED], BARRIER NODE [BLACK] and then press [SPACEBAR] to start DFS Traversal |')
	print('--------------------------------------------------------------------------------------------------------------------')

	while run:
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
			if pygame.mouse.get_pressed()[0]:
				row, col = pygame.mouse.get_pos()
				row = row // width
				col = col // width
				spot = Grid[row][col]

				if not start and spot != end:
					start = spot
					start.make_start()
					start.draw()
				
				elif not end and spot != start:
					end = spot
					end.make_end()
					end.draw()
				
				elif spot != start and spot != end:
					spot.make_barrier()
					spot.draw()

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
				spot.draw()
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					print('[+] STARTED BFS TRAVERSAL [+]')
					fill_neighbors(Grid)
					dfs(start, end, Grid)	
					print('[+] DFS ENDS  [+]')


if __name__ == "__main__":
	main()

