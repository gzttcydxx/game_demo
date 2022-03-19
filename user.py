#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from game import Attack

# 人物类
class User(pygame.sprite.Sprite):
    def __init__(self):
        # 继承父类
        super(User, self).__init__()
        # 角色名称
        self.name: str
        # 生命值
        self.hp: int
        # 护盾值
        self.shield: int
        # 防御
        self.defend: int = 0
        # 是否AOE
        self.aoe: bool = False
        # 是否嘲讽
        self.is_taunt: bool = False
        # 是否禁疗
        self.is_forbidden_heal: bool = False
        # 伤害系数
        self.attack_coe: float
        # 基础攻击
        self.attack: Attack = Attack(0, 3, 0) # 或运算
        # 手牌
        self.hand: list
        # 手牌上限
        self.hand_max: int = 5
        # 指示器
        self.indicators: int
        # 指示器上限
        self.indicators: int = None
        # 每回合可使用战斗牌数
        self.available_battle_card_num: int = 1
        # 每回合可使用战斗牌数上限
        self.available_battle_card_num: int = 1
        # 召唤物数量
        self.servant_num: int
        # 召唤物数量上限
        self.servent_num_max: int = None
        # 召唤物列表
        self.servents: list


    # 获取手牌
    def get_hand(self, num: int):
        self.hand.append()
    
    # 

    # 指示器方法
    def use_indicator(self):
        pass