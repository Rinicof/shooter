from pygame import *
from random import randint
from time import sleep




class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        # WASD
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 700:
            self.rect.x += self.speed
        
        # Стрелочки
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 700:
            self.rect.x += self.speed
       
    def fire(self):
        global kd
        if kd >= 3:
            time.delay(3)
            kd = 0
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)
        fire.play()
        kd += 1



class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y == 600:
            self.rect.y = 0
            self.rect.x = randint(50, 550)
            global miss
            miss += 1


class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y == 0:
            self.kill()


score = 0
miss = 0
kd = 0

window = display.set_mode((800, 600))
display.set_caption("BEST SHOOTER EVER")
background = transform.scale(image.load("galaxy.jpg"), (800, 600))
clock = time.Clock()
fps = 1050#ti
font.init()
font = font.Font(None, 50)
wintext = font.render('УРАААААААААА!!!',True, (255, 215, 0))
losetext = font.render('НЕЕЕЕЕЕЕТ!!!',True, (255, 215, 0))


mixer.init()
mixer.music.load("space.ogg")
#mixer.music.play()
fire = mixer.Sound("fire.ogg")

roketa = Player("rocket.png", 100, 500, 75, 75, 6)  #Игрок
enemy1 = Enemy("ufo.png", 50, 0, 75, 75, 1)  #Бот1
enemy2 = Enemy("ufo.png", 100, 0, 75, 75, 2)  #Бот2
enemy3 = Enemy("ufo.png", 200, 0, 75, 75, 2.5)  #Бот3
enemy4 = Enemy("ufo.png", 350, 0, 75, 75, 3)  #Бот4
enemy5 = Enemy("ufo.png", 500, 0, 75, 75, 3)  #Бот5
smekta1 = Enemy("asteroid.png", 50, 0, 75, 75, 5)  #Смекта1
smekta2 = Enemy("asteroid.png", 241, 0, 75, 75, 5)  #Смекта2
smekta3 = Enemy("asteroid.png", 300, 0, 75, 75, 5)  #Смекта3

monsters = sprite.Group()
monsters.add(enemy1)
monsters.add(enemy2)
monsters.add(enemy3)
monsters.add(enemy4)
monsters.add(enemy5)
asteroids =sprite.Group()
asteroids.add(smekta1)
asteroids.add(smekta2)
asteroids.add(smekta3)

bullets = sprite.Group()

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e. type == KEYDOWN:
            if e.key == K_SPACE:
                roketa.fire()
    clock.tick(fps)
    if not finish:
        killstext = font.render('Убито: ' + str(score), True, (255, 255, 255))
        misstext = font.render('Пропущенно: ' + str(miss), True, (255, 255, 255))
        sprites_list1 = sprite.spritecollide(roketa, monsters, True)
        sprites_list2 = sprite.groupcollide(monsters, bullets, True, True)
        sprites_list3 = sprite.spritecollide(roketa, asteroids, True)
        sprites_list4 = sprite.groupcollide(asteroids, bullets, True, True)
        window.blit(background, (0, 0))
        for i in sprites_list2:
            score += 1
            enemy = Enemy("ufo.png", randint(50, 500), 0, 75, 75, randint(1, 3))
            monsters.add(enemy)
        for i in sprites_list1: 
            miss += 1
            enemy = Enemy("ufo.png", randint(50, 500), 0, 75, 75, randint(1, 3))
            monsters.add(enemy)
        for i in sprites_list4:
            score += 1
            enemy = Enemy("asteroid.png", randint(50, 500), 0, 75, 75, randint(1, 3))
            asteroids.add(enemy)
        for i in sprites_list3: 
            miss += 1
            enemy = Enemy("asteroid.png", randint(50, 500), 0, 75, 75, randint(1, 3))
            asteroids.add(enemy)
        if score >= 50:
            sleep(0.5)
            window.blit(wintext, (200, 200))
            finish = True
            #game = False
        if miss >= 100:
            sleep(0.5)
            window.blit(losetext, (200, 200))
            finish = True

        
        roketa.reset()
        roketa.update()
        monsters.draw(window)
        monsters.update()
        asteroids.draw(window)
        asteroids.update()
        #smekta1.update()
        #smekta2.update()
        #smekta3.update()
        bullets.draw(window)
        bullets.update()
        window.blit(killstext, (0, 0))
        window.blit(misstext, (0, 30))

        display.update()





'''
import pygame as pg
from random import *
import time

class GameSprite(pg.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load(player_image), (75, 75))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = pg.key.get_pressed()
        # WASD
        if keys_pressed[pg.K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[pg.K_d] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys_pressed[pg.K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[pg.K_s] and self.rect.y < 500:
            self.rect.y += self.speed
        
        # Стрелочки
        if keys_pressed[pg.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[pg.K_RIGHT] and self.rect.x < 700:
            self.rect.x += self.speed
        if keys_pressed[pg.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[pg.K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed

class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 55:
            self.direction = 'right'
        if self.rect.x >= 800 - 85:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
              self.rect.x += self.speed

class Wall(pg.sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color1
        self.color_2 = color2
        self.color_3 = color3
        self.width = wall_width
        self.height = wall_height
        self.image = pg.Surface((self.width, self.height))
        self.image.fill((self.color_1, self.color_2, self.color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = pg.display.set_mode((800, 600))
pg.display.set_caption("Maze")
background = pg.transform.scale(pg.image.load("background.jpg"), (800, 600))
player = Player('bomz.png', 100, 100, 4.5)
cyborg = Enemy('cyborg3.png', 700, 150, 4)
zoloto = GameSprite('treasure.png', 700, 500, 0)
wall1 = Wall(102, 0, 51, 300, 50, 10, 100)
wall2 = Wall(102, 0, 51, 50, 50, 500, 10)
wall3 = Wall(102, 0, 51, 300, 250, 10, 250)
wall4 = Wall(102, 0, 51, 50, 500, 500, 10)
clock = pg.time.Clock()
fps = 500
finish = False
pg.font.init()
font = pg.font.Font(None, 70)
wintext = pg.font.render('ПАБЕДААААА!!!',True, (255, 215, 0))
losetext = pg.font.render('НЕЕЕЕЕТ!!!',True, (255, 215, 0))

# Музыка
pg.mixer.init()
pg.mixer.music.load('jungles.ogg')
pg.mixer.music.play()
lose = pg.mixer.Sound('kick.ogg')
win = pg.mixer.Sound('money.ogg')

game = True
while game:
    keys_pressed = pg.key.get_pressed()
    for e in pg.event.get():
        if e.type == pg.QUIT:
            game = False

    if finish != True:
        if pg.sprite.collide_rect(player, zoloto):
            win.play()
            window.blit(wintext, (200, 200))
            time.sleep(1)
            finish = True
            game = False
        if pg.sprite.collide_rect(player, cyborg):
            lose.play()
            window.blit(losetext, (200, 200))
            time.sleep(1)
            finish = True
            game = False
        if pg.sprite.collide_rect(player, wall1):
            lose.play()
            window.blit(losetext, (200, 200))
            time.sleep(1)
            finish = True
            game = False
        if pg.sprite.collide_rect(player, wall2):
            lose.play()
            window.blit(losetext, (200, 200))
            time.sleep(1)
            finish = True
            game = False
        if pg.sprite.collide_rect(player, wall3):
            lose.play()
            window.blit(losetext, (200, 200))
            time.sleep(1)
            finish = True
            game = False
        if pg.sprite.collide_rect(player, wall4):
            lose.play()
            time.sleep(1)
            finish = True
            game = False

        window.blit(background, (0 ,0))
        clock.tick(fps)
        player.update()
        cyborg.update()
        player.reset()
        cyborg.reset()
        zoloto.reset()
        wall1.draw_wall()
        wall2.draw_wall()
        wall3.draw_wall()
        wall4.draw_wall()
        pg.display.update()
'''