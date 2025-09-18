# player_hp.py
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, initial_hp):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill((89, 35, 127))  # Blue rectangle for player
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hp = initial_hp
        self.max_hp = initial_hp

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def is_alive(self):
        return self.hp > 0

    def draw_hp_bar(self, screen, x, y, width, height):
        # Draw background for HP bar
        pygame.draw.rect(screen, (100, 100, 100), (x, y, width, height))
        # Draw current HP
        current_hp_width = (self.hp / self.max_hp) * width
        pygame.draw.rect(screen, (255, 0, 0), (x, y, current_hp_width, height))
        # Draw border
        pygame.draw.rect(screen, (0, 0, 0), (x, y, width, height), 2)

    def update(self):
        # Add any player specific updates here, e.g., movement logic
        pass

# Example usage in a main game file:
# import pygame
# from player_hp import Player

# pygame.init()
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Player HP Example")

# player = Player(100, 400, 50, 50, 100)
# all_sprites = pygame.sprite.Group()
# all_sprites.add(player)

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 player.take_damage(10)
#             if event.key == pygame.K_h:
#                 player.heal(5)

#     screen.fill((255, 255, 255)) # White background
#     all_sprites.draw(screen)
#     player.draw_hp_bar(screen, 50, 50, 200, 20)

#     pygame.display.flip()

# pygame.quit()
