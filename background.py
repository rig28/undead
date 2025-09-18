import pygame
    pygame.init()
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("pygame background")
    background_image = pygame.image.load("pixel.jpg").convert()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Blit the background image
        screen.blit(background_image, (0, 0))

        # Update the display
        pygame.display.flip()

    pygame.quit()
