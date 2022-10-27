import math
import pygame

WIDTH = 800
HEIGHT = 1200

WIN = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('Fourier Series')

RED = (255, 0, 0)
GREEN = (0, 255, 3)
BLUE = (0, 0, 255)
UN = (14, 156, 199)
BLACK = (0, 0, 0)
WHITE =  (255, 255, 255)
ORANGE = (255, 165, 0)
TURQUOISE = (64, 224, 208)
PURPLE = (128, 0, 128)
YELLOW = (102, 102, 0)
MAGENTA = (102, 102, 105)


class dot:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color

	def draw(self):
		pygame.draw.circle(WIN, self.color, (self.x, self.y), radius=5)

		
		
class circle:
	def __init__(self, x, y, r, w, theta, color):
		self.x = x
		self.y = y
		self.r = r
		self.w = w
		self.theta = theta
		self.dot = []
		self.color = color
	
	def draw(self):
		self.theta += self.w 
		x1 = self.x + self.r * math.cos(self.theta)
		y1 = self.y + self.r * math.sin(-self.theta)
		pygame.draw.circle(WIN, self.color, (self.x, self.y), radius=self.r)
		pygame.draw.line(WIN, GREEN, (self.x, self.y), (x1, y1), width=7)
	
	def radiate(self, mx, rad):
		self.theta += self.w 
		x1 = self.x + self.r * math.cos(self.theta)
		y1 = self.y + self.r * math.sin(-self.theta)
		pygame.draw.circle(WIN, self.color, (self.x, self.y), radius=self.r)
		pygame.draw.line(WIN, GREEN, (self.x, self.y), (x1, y1), width=7)
		pygame.draw.line(WIN, RED, (x1, y1), (rad + mx, y1), width=7)
	


def wave(List):
	mx = 0
	for i in range(len(List)):
		mx += List[i].r
		if i == len(List)-1:
			List[i].radiate(mx, List[0].x)
			for point in List[i].dot:
				point.draw()
				point.x += 5

		else:
			List[i].draw()
			x1 = List[i].x + List[i].r * math.cos(List[i].theta)
			y1 = List[i].y + List[i].r * math.sin(-List[i].theta)
			List[i+1].x = x1
			List[i+1].y = y1
		


def fill_dot(List, col):
	mx = 0
	for i in List:
		mx += i.r

	y1 = List[-1].y + List[-1].r * math.sin(-List[-1].theta)
	List[-1].dot.append(dot(mx + List[0].x , y1, col))


while True:
	amp = 4/math.pi
	rad = 100
	frq = 60
 
	List = [] 
	List.append(circle(300, 450, amp*rad, math.pi/frq, 0, MAGENTA))
	List.append(circle(300+amp*rad, 450, amp*rad/2, 2*math.pi/frq, 0, PURPLE))
	List.append(circle(300+amp*rad/2, 450, amp*rad/3, 3*math.pi/frq, 0, UN))
	List.append(circle(300+amp*rad/3, 450, amp*rad/4, 4*math.pi/frq, 0, TURQUOISE))
	List.append(circle(300+amp*rad/4, 450, amp*rad/5, 5*math.pi/frq, 0, YELLOW))
	List.append(circle(300+amp*rad/5, 450, amp*rad/6, 6*math.pi/frq, 0, BLUE))
	List.append(circle(300+amp*rad/6, 450, amp*rad/7, 7*math.pi/frq, 0, ORANGE))
	List.append(circle(300+amp*rad/7, 450, amp*rad/8, 8*math.pi/frq, 0, BLACK))
	
	fill_dot(List, BLUE)
 
	while True:
		wave(List)
		#print('----------------------------------------------------------------------------')
		#print(f'| wavelength = {List[0].r} unit | \n | angular velocity = {math.pi/50} rad/s |')
		#print('----------------------------------------------------------------------------')
		pygame.display.update()
		WIN = pygame.display.set_mode((HEIGHT, WIDTH))
		fill_dot(List, BLUE)
		


	

		

