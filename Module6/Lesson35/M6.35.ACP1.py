import pygame

pygame.init()

info = pygame.display.Info()
W = info.current_w
H = info.current_h

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

bg = pygame.image.load("house_background (1).png")
bg = pygame.transform.scale(bg, (W, H))

font = pygame.font.SysFont("arial", 35, True)

dog = pygame.Rect(W//2, H//2, 60, 60)

food = [
    pygame.Rect(W//8, H*4//5, 40, 40),
    pygame.Rect(W*3//8, H*3//4, 40, 40),
    pygame.Rect(W//2, H*4//5, 40, 40),
    pygame.Rect(W*2//3, H*3//4, 40, 40),
    pygame.Rect(W*7//8, H*4//5, 40, 40),
    pygame.Rect(W//6, H//2, 40, 40),
    pygame.Rect(W*5//6, H//2, 40, 40)
]

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        dog.x -= 6
    if keys[pygame.K_RIGHT]:
        dog.x += 6
    if keys[pygame.K_UP]:
        dog.y -= 6
    if keys[pygame.K_DOWN]:
        dog.y += 6

    dog.left = max(0, dog.left)
    dog.right = min(W, dog.right)
    dog.top = max(0, dog.top)
    dog.bottom = min(H, dog.bottom)

    for f in food[:]:
        if dog.colliderect(f):
            food.remove(f)

    screen.blit(bg, (0, 0))

    pygame.draw.circle(
        screen,
        (255, 0, 0),
        dog.center,
        30
    )

    for f in food:
        pygame.draw.ellipse(
            screen,
            (0, 150, 255),
            f
        )

    text = font.render(
        f"Food: {7-len(food)}/7",
        True,
        (40, 40, 40)
    )

    screen.blit(text, (20, 20))

    if not food:

        message = font.render(
            "Well done! All food collected!",
            True,
            (255, 255, 255)
        )

        screen.blit(
            message,
            message.get_rect(
                center=(W//2, H//2)
            )
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()