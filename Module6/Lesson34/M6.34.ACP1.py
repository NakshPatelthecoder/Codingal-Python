import pygame

pygame.init()

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Smart Traffic Signal Simulator")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (80, 80, 80)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
YELLOW = (255, 200, 0)
BLUE = (0, 100, 255)

class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((60, 30))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 235

        self.velocity = 3

    def update(self):
        self.rect.x += self.velocity

car = Car()

car_group = pygame.sprite.Group()
car_group.add(car)

signal_colour = GREEN

CHANGE_SIGNAL = pygame.USEREVENT + 1

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == CHANGE_SIGNAL:

            if signal_colour == GREEN:
                signal_colour = RED
            else:
                signal_colour = GREEN

            if signal_colour == RED:
                car.image.fill(RED)
            else:
                car.image.fill(BLUE)

    car_group.update()

    if car.rect.right >= 750:

        car.velocity = 0

        pygame.event.post(pygame.event.Event(CHANGE_SIGNAL))

        car.rect.x = 50

        car.velocity = 3

    screen.fill(WHITE)

    pygame.draw.rect(screen, GREY, (0, 200, 800, 100))

    for x in range(0, 800, 80):
        pygame.draw.rect(screen, WHITE, (x, 245, 40, 5))

    pygame.draw.rect(screen, BLACK, (680, 50, 80, 150))

    pygame.draw.circle(screen, RED, (720, 85), 20)
    pygame.draw.circle(screen, YELLOW, (720, 125), 20)
    pygame.draw.circle(screen, GREEN, (720, 165), 20)

    pygame.draw.circle(screen, signal_colour, (720, 125), 10)

    car_group.draw(screen)

    pygame.display.update()

    clock.tick(60)

pygame.quit()