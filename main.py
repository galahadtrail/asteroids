import pygame
from constants import *

def main():
	pygame.init()
	py_time = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill(BLACK)
		pygame.display.flip()
		dt = py_time.tick(60) / 1000


if __name__ == "__main__":
	main()
