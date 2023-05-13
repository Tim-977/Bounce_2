import pygame
from pygame import mixer

mixer.init()

class Ball:
    def __init__(self, pos, radius, color, vel=[0, 0], gravity=0.2):
        self.pos = pos
        self.radius = radius
        self.color = color
        self.vel = vel
        self.gravity = gravity

    def update(self, screen_size):
        self.vel[1] += self.gravity

        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

        if self.pos[0] - self.radius < 0 or self.pos[0] + self.radius > screen_size[0]:
            self.vel[0] *= -1

        if self.pos[1] + self.radius > screen_size[1]:
            self.vel[1] *= -0.9
            self.pos[1] = screen_size[1] - self.radius
            mixer.Channel(1).play(mixer.Sound("sound.mp3"))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.pos[0]), int(self.pos[1])), self.radius)



pygame.init()


WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bounce_2")

objects =[]

for i in range(1, 25 + 1):
    objects.append(Ball([16 + i * 30, i * 15], 15, (10 * i, 255 - i * 10, 255), [5, 0], 0.1))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    for object in objects:
        object.update((WIDTH, HEIGHT))

    screen.fill((0, 0, 0))

    for object in objects:
        object.draw(screen)

    pygame.display.update()

    clock.tick(120)
