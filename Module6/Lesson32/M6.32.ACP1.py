import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wildlife Information Display")

background = pygame.image.load("jungle.jpeg")

wildlife = pygame.image.load("lion.jpeg")

background = pygame.transform.scale(background, (800, 600))

wildlife = pygame.transform.scale(wildlife, (300, 300))

font = pygame.font.Font(None, 50)

heading = font.render("The Lion in the Jungle", True, (255, 255, 255))

fact_font = pygame.font.Font(None, 30)

fact1 = fact_font.render("Lions have a tiny sharp spine", True, (255, 255, 255))
fact2 = fact_font.render("at the tip of their tail.", True, (255, 255, 255))

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    screen.blit(heading, (250, 30))

    screen.blit(wildlife, (50, 150))

    screen.blit(fact1, (400, 200))
    screen.blit(fact2, (400, 240))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()