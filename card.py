#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pygame
from game import Attack
from user import User


# 卡牌类
class Card(pygame.sprite.Sprite):
    def __init__(self) -> None:
        # 继承父类
        super(Card, self).__init__()
        # 卡牌名称
        self.name: str
        # 使用主体
        self.entity: User


# 伤害卡牌类
class DamageCard(Card):
    def __init__(self) -> None:
        # 继承父类
        super(Card, self).__init__()
        # 卡牌伤害
        self.damage: Attack

    # 先手特效
    def effect_sente(self):
        return None

    # 伤害特效
    def effect_damage(self):
        return None

    # 后手特效
    def effect_gote(self):
        return None


# 技能卡牌类
class SkillCard(Card):
    def __init__(self) -> None:
        # 继承父类
        super(Card, self).__init__()
        # 技能类型（0 -> 战术技能, 1 -> 反击技能, 2 -> 终极技能）
        type: int


# ------------------------伤害牌------------------------ #
class JiDongShu(DamageCard):
    name = "急冻术"
    damage = Attack(0, 1, 0, aoe=True, is_frozen=True)

class HuoQiu(DamageCard):
    name = "火球"
    damage = Attack(0, 2, 0)