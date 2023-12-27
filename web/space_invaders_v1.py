import pygame
pygame.init()

win_width, win_height = 800, 600
win = pygame.display.set_mode((win_width, win_height))

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 5

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, 50, 50))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel

class Invader:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 2

    def draw(self, win):
        pygame.draw.rect(win, (0, 255, 0), (self.x, self.y, 50, 50))

    def move(self):
        self.x += self.vel
        if self.x <= 0 or self.x >= win_width - 50:
            self.vel *= -1
            self.y += 50

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 10

    def draw(self, win):
        pygame.draw.rect(win, (0, 0, 255), (self.x, self.y, 5, 10))

    def move(self):
        self.y -= self.vel

def game_loop():
    clock = pygame.time.Clock()
    player = Player(375, 550)
    invaders = [Invader(i, j) for i in range(100, 700, 100) for j in range(50, 200, 50)]
    bullets = []

    running = True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(Bullet(player.x, player.y))

        player.move()
        for invader in invaders:
            invader.move()
        for bullet in bullets:
            bullet.move()

        for bullet in bullets:
            for invader in invaders:
                if bullet.x in range(invader.x, invader.x + 50) and bullet.y in range(invader.y, invader.y + 50):
                    bullets.remove(bullet)
                    invaders.remove(invader)
                    break

        for invader in invaders:
            if invader.y >= win_height - 50:
                running = False
                break

        win.fill((0, 0, 0))
        player.draw(win)
        for invader in invaders:
            invader.draw(win)
        for bullet in bullets:
            bullet.draw(win)
        pygame.display.update()

    pygame.quit()

game_loop()