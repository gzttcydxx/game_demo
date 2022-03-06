#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 人物类
class User:
    # 角色名称
    name: str
    # 生命值
    hp: int
    # 护盾值
    shield: int
    # 防御
    defend: int = 0
    # 是否AOE
    aoe: bool = False
    # 伤害系数
    attack_coe: float
    # 手牌
    hand: list
    # 手牌上限
    hand_max: int = 5
    # 指示器
    indicators: int
    # 指示器上限
    indicators: int = None
    # 每回合可使用战斗牌数
    available_battle_card_num: int = 1
    # 每回合可使用战斗牌数上限
    available_battle_card_num: int = 1
    # 召唤物数量
    servant_num: int
    # 召唤物数量上限
    servent_num_max: int = None
    # 召唤物列表
    servents: list


    # 获取手牌
    def get_hand(self, num: int):
        self.hand.append()
    
    # 

    # 指示器方法
    def use_indicator(self):
        pass