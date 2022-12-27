import pygame
import math
import random

SIZE = (1200, 900)
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Spinski Triangle')

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
CList = [RED, GREEN, BLUE, WHITE, YELLOW, PINK]


def draw(x, y, col):
    pygame.draw.circle(WIN, col, (x, y), 1, 1)
    pygame.display.update()


def calc(x0, y0, x1, y1):
	return round((x0+x1)/2,2), round((y0+y1)/2)

def spinski(List, x, y):
	while True:
		pos =  random.randint(0,2)
		col = random.randint(0, 5)
		x0 = List[pos][0]
		y0 = List[pos][1]
		draw(x0, y0, RED)

		xmid, ymid = calc(x0, y0, x, y)
		x = xmid
		y = ymid

		draw(x, y, CList[col])
		draw(x0, y0, RED)
		

def main():
	List = []
	x = 0
	y = 0
	Side = 800
	run = True
	count = 0
	while run:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 0
		
			if pygame.mouse.get_pressed()[0]:
				if count==0:
					x0, y0 = pygame.mouse.get_pos()

					x1 = x0 - Side*math.sin(math.pi/6)
					x2 = x0 + Side*math.sin(math.pi/6)

					y1 = y0 + Side*math.cos(math.pi/6)
					y2 = y1

					draw(x0, y0, BLUE)
					draw(x1, y1, BLUE)
					draw(x2, y2, BLUE)

					List.append([x0, y0])
					List.append([x1, y1])
					List.append([x2, y2])
					count+=1
				
				elif count==1:
					x, y = pygame.mouse.get_pos()
					draw(x, y, BLUE)
					count+=1

		
			if pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				draw(pos[0], pos[1], BLACK)


			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					print(x, y)
					spinski(List, x, y)
					run = False


if __name__ == "__main__":
	main()
