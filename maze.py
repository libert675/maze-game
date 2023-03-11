#создай игру "Лабиринт"!
import pygame
 
pygame.init()
class GameSprite(pygame.sprite.Sprite):
    # Конструктор
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(player_image), (65,65))
        self.speed = player_speed
        # Создаем свойство Rect (координаты и размер нашего спрайта)
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    # Метод, для отрисовки спрайта
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
 
class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed() # Получаем все зажатые клавиши
        # Если нажата кнопка стрелка влево и x больше чем 5
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            # Перетаскиваем персонажа влево
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
 
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
            self.direction = 'left'
 
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
 
# Игровая сцена
win_width = 700
win_height = 500
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Лабиринт")
background = pygame.transform.scale(pygame.image.load('background.jpg'), (win_width, win_height))
 
# Спрайты игры
player = Player('hero.png', 5, win_height - 80, 4)
monster = Enemy('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
game = True
finish = False
clock = pygame.time.Clock()
FPS = 60
 
# музыка
pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()
 
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
 
    if finish != True:
        window.blit(background, (0, 0))
 
        player.update()
        monster.update()
 
        player.reset()
        monster.reset()
        final.reset()
 
    if pygame.sprite.collide_rect(player, monster):
        print('Столкновение')
 
    pygame.display.update()
    clock.tick(FPS)