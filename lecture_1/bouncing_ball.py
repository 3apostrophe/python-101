import pygame
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Colors
WHITE = (255, 255, 255)
BALL_COLOR = (255, 100, 100)

# Ball settings
ball_radius = 20
ball_x = random.randint(ball_radius, WIDTH - ball_radius)
ball_y = random.randint(ball_radius, HEIGHT - ball_radius)
ball_speed_x = 5
ball_speed_y = 4

clock = pygame.time.Clock()
running = True

# Game loop
while running:
    screen.fill(WHITE)

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce on walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_speed_x *= -1
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_speed_y *= -1

    # Draw ball
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), ball_radius)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
