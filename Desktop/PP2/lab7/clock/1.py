import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 900, 800

clock_img = pygame.image.load('mickey.png')
left_hand_img = pygame.image.load('minutes.png')
right_hand_img = pygame.image.load('seconds.png')

clock_rect = clock_img.get_rect(center = (WIDTH//2, HEIGHT//2))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = pygame.time.get_ticks() // 1000

    minute_angle = current_time % 60 * 6
    second_angle = current_time % 6

    rotated_left_hand = pygame.transform.rotate(left_hand_img, -second_angle)
    rotated_right_hand = pygame.transform.rotate(right_hand_img, -minute_angle)

    screen.fill((255,255,255))
    screen.blit(clock_img, clock_rect.topleft)
    screen.blit(rotated_left_hand, (clock_rect.centerx - rotated_left_hand.get_rect().width // 2, clock_rect.centery - rotated_left_hand.get_rect().height // 2))
    screen.blit(rotated_right_hand, (clock_rect.centerx - rotated_right_hand.get_rect().width // 2, clock_rect.centery - rotated_right_hand.get_rect().height // 2))

    pygame.display.flip()