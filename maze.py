#создай игру "Лабиринт"!
from pygame import *
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
        if keys_pressed[K_d] and self.rect.x < 635:
            self.rect.x += self.speed    
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'

        if self.rect.x >= 645:
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed

        else:
            self.rect.x -= self.speed

class Wall(sprite.Sprite):
    def __init__ (self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color1
        self.color_2 = color2
        self.color_3 = color3
        self.wall_x = wall_x
        self.wall_y = wall_y
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption('Лабиринт')

background = transform.scale(image.load('background.jpg'), (700,500))

player = Player('hero.png', 50, 50, 4)
monster = Enemy('cyborg.png', 470, 200, 3)
final = GameSprite('treasure.png', 550, 400, 0)
wall1 = Wall(30, 200, 110, 50, 160, 450, 10)
wall2 = Wall(30, 200, 110, 100, 400, 350, 10)
wall3 = Wall(30, 200, 110, 10, 30, 10, 380)

clock = time.Clock()
FPS = 60
game = True
finish = False

font.init()
font = font.SysFont("Arial", 70)
win = font.render('WIN!', True, (100, 100, 200))
lose = font.render('LOSE!', True, (100, 100, 200))

mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.blit(background, (0,0))
        player.reset()
        monster.reset()
        final.reset()
        
        player.update()
        monster.update()

        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()

        if sprite.collide_rect(player, monster) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3):
            finish = True
            window.blit(lose, (200,200))
            kick.play()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (200,200))
            money.play()

    clock.tick(FPS)
    display.update()




