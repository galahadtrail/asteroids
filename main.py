import pygame
from constants import *
from player import Player
from asteroid import Asteroid

def main():
	pygame.init()
	py_time = pygame.time.Clock()
	dt = 0
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Player.containers = (updatable, drawable)
	Asteroid.containers = (asteroids, updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill(BLACK)

		for drw in drawable:
			drw.draw(screen)

		for upd in updatable:
			upd.update(dt)

		pygame.display.flip()
		dt = py_time.tick(60) / 1000


if __name__ == "__main__":
	main()
