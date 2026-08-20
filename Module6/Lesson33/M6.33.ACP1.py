import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini Sprite Adventure")

clock = pygame.time.Clock()

# Sprite
sprite = pygame.Rect(375, 275, 50, 50)

# Starting colour
colour = (50, 150, 255)

running = True

while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard controls
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        sprite.x -= 5

    if keys[pygame.K_RIGHT]:
        sprite.x += 5

    if keys[pygame.K_UP]:
        sprite.y -= 5

    if keys[pygame.K_DOWN]:
        sprite.y += 5

    # Keep sprite inside the screen using min() and max()
    sprite.x = max(0, min(sprite.x, 800 - sprite.width))
    sprite.y = max(0, min(sprite.y, 600 - sprite.height))

    # Change colour when a boundary is touched
    # The colour stays until another boundary is touched
    if sprite.left == 0:
        colour = (255, 80, 80)       # Red

    elif sprite.right == 800:
        colour = (80, 255, 80)       # Green

    elif sprite.top == 0:
        colour = (180, 80, 255)      # Purple

    elif sprite.bottom == 600:
        colour = (255, 200, 50)      # Yellow

    # Background
    screen.fill((30, 35, 45))

    # Draw solid sprite
    pygame.draw.rect(screen, colour, sprite)

    # Update display
    pygame.display.flip()

    # Keep the game running at 60 FPS
    clock.tick(60)

pygame.quit()