import pygame
import pyautogui

pygame.init()

    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Start")


    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pygame Background Image")

    background_image = pygame.image.load("pixel.jpg").convert()
    # Replace "your_image_file.png" with the actual path to your image.
    # .convert() optimizes the image for faster blitting.

start = "start"

player_hp = 100

print(player_hp)
