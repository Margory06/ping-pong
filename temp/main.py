from pygame import *
x = 700
y = 500
cost_l = 0
cost_r = 0
w = display.set_mode((x, y))
back = (160, 100, 225)
w.fill(back)
display.set_caption('Игра1')
clock = time.Clock()
FPS = 17
mixer.init()
font.init()
font = font.Font('Kot Leopold.ttf', 70)
lose_right = font.render(
    'Right LOSE', True, (0, 100, 0)
)
lose_left = font.render(
    'Left LOSE', True, (0, 100, 0)
)

finish = False






class GameSprite(sprite.Sprite):
    def __init__(self, pic, x, y, speed, w, h):
        super().__init__()
        self.p = transform.scale(image.load(pic), (w, h))
        self.rect = self.p.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.s = speed
    def show(self):
        w.blit(self.p, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, pic, x, y, speed, w, h):
        super().__init__(pic, x, y, speed, w, h)
    def move_l(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_w] and self.rect.y > 5:
                self.rect.y -= self.s
            if keys_pressed[K_s] and self.rect.y < 400:
                self.rect.y += self.s
    def move_r(self):
            keys_pressed = key.get_pressed()
            if keys_pressed[K_UP] and self.rect.y > 5:
                self.rect.y -= self.s
            if keys_pressed[K_DOWN] and self.rect.y < 400:
                self.rect.y += self.s

ball = GameSprite('cosmo_ball.png', 100, 100, 15, 60, 60)
r_l = Player('l_rocket.png', 20, 250, 15, 30, 160)
r_r = Player('r_rocket.png', 660, 250, 15, 30, 160)

x_speed = ball.s
y_speed = ball.s


game = True
while game:
    if finish != True:
        w.fill(back)
        ball.rect.x += x_speed
        ball.rect.y -= y_speed
        
        if sprite.collide_rect(r_r, ball) or sprite.collide_rect(r_l, ball):
            x_speed *= -1
            #y_speed *= -1
        if ball.rect.y >= 450 or ball.rect.y <= 0:
            y_speed *= -1
        if ball.rect.x <= 0:
            cost_l += 1
            x_speed *= -1
        if ball.rect.x >= 680:
            cost_r += 1
            x_speed *= -1
        c = str(cost_l) + ':' + str(cost_r)
        cost = font.render(
            c, True, (0, 100, 0)
        )
        w.blit(cost, (300, 30))
        if cost_l >= 3:
            w.blit(lose_left, (50, 100))
            finish = True
        if cost_r >= 3:
            w.blit(lose_right, (350, 100))
            finish = True

        ball.show()
        r_r.show()
        r_l.show()
        r_r.move_r()
        r_l.move_l()
    
    for i in event.get():
        if i.type == QUIT:
            game = False
    
    clock.tick(FPS)
    display.update()