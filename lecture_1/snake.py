import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Game window
BLOCK_SIZE = 20
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)


# Snake and Food
def draw_snake(snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, BLOCK_SIZE, BLOCK_SIZE])


def draw_food(x, y):
    pygame.draw.rect(screen, RED, [x, y, BLOCK_SIZE, BLOCK_SIZE])


def message(text, color):
    msg = font.render(text, True, color)
    screen.blit(msg, [WIDTH // 6, HEIGHT // 3])


# Main game loop
def game_loop():
    game_over = False
    game_close = False

    # Starting position
    x = WIDTH // 2
    y = HEIGHT // 2
    dx = 0
    dy = 0

    snake = []
    snake_length = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:

        while game_close:
            screen.fill(WHITE)
            message("You lost! Press Q to Quit or R to Restart", RED)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx = 0
                    dy = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx = 0
                    dy = BLOCK_SIZE

        x += dx
        y += dy

        # Check collision with borders
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            game_close = True

        screen.fill(BLACK)
        draw_food(food_x, food_y)

        snake.append([x, y])
        if len(snake) > snake_length:
            del snake[0]

        # Check self collision
        for segment in snake[:-1]:
            if segment == [x, y]:
                game_close = True

        draw_snake(snake)

        pygame.display.update()

        # Check if food eaten
        if x == food_x and y == food_y:
            food_x = (
                round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            )
            food_y = (
                round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE)
                * BLOCK_SIZE
            )
            snake_length += 1

        clock.tick(10)

    pygame.quit()
    sys.exit()


game_loop()
