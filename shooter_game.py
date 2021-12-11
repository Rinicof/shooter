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
