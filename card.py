#!/usr/bin/env python
# -*- coding: utf-8 -*-


from game import Attack
from user import User


# 卡牌类
class Card:
    # 卡牌名称
    name: str
    # 使用主体
    entity: User


# 伤害卡牌类
class DamageCard(Card):
    # 卡牌伤害
    damage: Attack

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
    # 技能类型（0 -> 战术技能, 1 -> 反击技能, 2 -> 终极技能）
    type: int


# ------------------------伤害牌------------------------ #
class JiDongShu(DamageCard):
    name = "急冻术"
    damage = Attack(0, 1, 0, aoe=True, is_frozen=True)

class HuoQiu(DamageCard):
    name = "火球"
    damage = Attack(0, 2, 0)