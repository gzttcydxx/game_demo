import pygame
from pygame.locals import *
from user import User

class Card(pygame.sprite.Sprite):
    def __init__(self):
        # 继承父类
        super(Card, self).__init__()
        # 卡牌名称
        self.name: str
        # 使用主体
        self.entity: User
        self.image = pygame.image.load("破灭斩.png")
        # self.image = pygame.transform.scale(self.image, (500 * 1240 / 1748, 500))
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
screen.fill([255, 255, 255])
pygame.display.set_caption("精灵类测试")
font = pygame.font.Font(None, 18)

card = Card()
screen.blit(card.image,card.rect)
pygame.display.update()
group = pygame.sprite.Group()
group.add(card)

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
