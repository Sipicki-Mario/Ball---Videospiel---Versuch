import pygame
import random

# Initialisierung von Pygame
pygame.init()

# Definiere Bildschirmgröße
screen_width = 800
screen_height = 600

# Farben
black = (0, 0, 0)
white = (255, 255, 255)

# Erstellen des Bildschirms
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ball Game")

# Spielerklasse
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height // 2)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

# Hindernis-Klasse
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(screen_width - self.rect.width)
        self.rect.y = random.randrange(screen_height - self.rect.height)

    def update(self):
        self.rect.y += 5
        if self.rect.top > screen_height:
            self.rect.y = 0
            self.rect.x = random.randrange(screen_width - self.rect.width)

# Spritegruppen
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

for i in range(10):
    obstacle = Obstacle()
    all_sprites.add(obstacle)
    obstacles.add(obstacle)

# Spiel-Loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, obstacles, False)
    if hits:
        running = False

    screen.fill(black)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()