import pygame
import random

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

# Load the sprites
player = pygame.image.load("player.png")
enemy = pygame.image.load("enemy.png")

# Player position
player_x = 375
player_y = 500

# Create 7 enemies
enemies = []

for i in range(7):
    enemy_x = random.randint(0, 750)
    enemy_y = random.randint(50, 400)
    enemies.append([enemy_x, enemy_y])

# Score
score = 0

# Game loop
running = True

while running:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= 2

    if keys[pygame.K_RIGHT]:
        player_x += 2

    if keys[pygame.K_UP]:
        player_y -= 2

    if keys[pygame.K_DOWN]:
        player_y += 2

    # Keep the player on the screen
    if player_x < 0:
        player_x = 0

    if player_x > 750:
        player_x = 750

    if player_y < 0:
        player_y = 0

    if player_y > 550:
        player_y = 550

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the player
    screen.blit(player, (player_x, player_y))

    # Draw the enemies
    for enemy_position in enemies:
        screen.blit(enemy, (enemy_position[0], enemy_position[1]))

    # Check for collisions
    player_rect = player.get_rect(topleft=(player_x, player_y))

    for enemy_position in enemies:

        enemy_rect = enemy.get_rect(
            topleft=(enemy_position[0], enemy_position[1])
        )

        if player_rect.colliderect(enemy_rect):
            score += 1

            # Move the enemy to a new random position
            enemy_position[0] = random.randint(0, 750)
            enemy_position[1] = random.randint(50, 400)

    # Update the screen
    pygame.display.update()

pygame.quit()