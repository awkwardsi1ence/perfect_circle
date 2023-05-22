import pygame
import math


pygame.init()

width = 800
height = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Perfect Circle Game")

circle_x = width // 2
circle_y = height // 2
radius = 200

error_distance = 20
error_speed = 2

percentage = 100

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    mouse_x, mouse_y = pygame.mouse.get_pos()

    distance = math.sqrt((mouse_x - circle_x) ** 2 + (mouse_y - circle_y) ** 2)

    percentage = int((1 - abs(distance - radius) / radius) * 100)

    if distance < radius - error_distance or distance > radius + error_distance:
        pygame.draw.circle(screen, RED, (circle_x, circle_y), radius, 3)
    else:
        pygame.draw.circle(screen, WHITE, (circle_x, circle_y), radius, 3)

    color = (255, int(255 * (100 - percentage) / 100), int(255 * (100 - percentage) / 100))
    color = tuple(max(0, min(255, c)) for c in color)
    pygame.draw.circle(screen, color, (circle_x, circle_y), radius)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Perfectness: {percentage}%", True, WHITE)
    screen.blit(text, (20, 20))

    pygame.display.flip()

pygame.quit()
