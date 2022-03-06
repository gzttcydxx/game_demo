#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
from random import randint
from typing import List, Tuple


# 怪物类
class Monster:
    # 星级
    star: int
    # 名字
    name: str
    # 描述
    description: str
    # 生命值
    hp: List[int]
    # 生命值上限
    hp_max: Tuple[int]
    # 多段攻击
    # is_mul_atk: bool = False
    # 攻击力
    atk: List[int]
    # 护盾
    shield: int = 0
    # 是否AOE
    aoe: bool = False
    # 护盾伤害系数（0 -> 物理, 1 -> 魔法, 2 -> 真实）
    shield_damage_coe: List[int] = [0.5, 0.5, 1]
    # 本体伤害系数（0 -> 物理, 1 -> 魔法, 2 -> 真实）
    self_damage_coe: List[int] = [1, 1, 1]
    # 当前状态
    state: int = 1
    # 总状态数
    total_state: int
    # 状态字典（hp）
    state_detail: dict = {1: 0}


    def __str__(self):
        return f"【怪物信息】 名字：{self.name}\n" \
               f"           星级：{self.star}\n" \
               f"           生命值：{self.hp}\n" \
               f"           护盾：{self.shield}\n" \
               f"           攻击力：{self.atk}\n" \
               f"           AOE攻击：{self.aoe}"

    # 特性
    def character(self):
        pass

    # 受到攻击
    def attacked(self, attack: Attack):
        if self.shield and not attack.is_penetrate:
            self.shield = self.shield - ceil(attack.atk * self.shield_damage_coe[attack.type])
            self.shield = 0 if self.shield < 0 else self.shield
        else:
            if attack.aoe:
                for i in range(len(self.hp)):
                    self.hp[i] = self.hp[i] - ceil(attack.atk * self.self_damage_coe[attack.type])
                    self.hp[i] = 0 if self.hp[i] < 0 else self.hp[i]
            else:
                self.hp[attack.which] = self.hp[attack.which] - ceil(attack.atk * self.self_damage_coe[attack.type])
                self.hp[attack.which] = 0 if self.hp[attack.which] < 0 else self.hp[attack.which]

    # 治疗
    def heal(self, num: int, which: int = 0):
        self.hp[which] += num
        self.hp[which] = self.hp_max[which] if self.hp[which] > self.hp_max[which] else self.hp[which]
        print(f"【战斗信息】 怪物受到治疗，恢复{num}点生命值")

    # 复活
    def revival(self):
        for i in range(len(self.hp)):
            if self.hp[i] == 0:
                self.hp[i] = self.hp_max[i]

    # 是否存活
    @property
    def is_alive(self):
        return any(self.hp)


# --------------------★★★-------------------- #

class GuaiLiYuan(Monster):
    name = "怪力螈"
    star = 3
    hp = [15]
    hp_max = tuple(hp)
    atk = [3]

    def character(self):
        return "【特性】 生命值低于5点时伤害附带3点真实伤害"


class CaoYuanLangQun(Monster):
    name = "草原狼群"
    star = 3
    hp = [10, 10, 10]
    hp_max = tuple(hp)
    atk = [1, 1, 1]


class BingJingShe(Monster):
    name = "冰晶蛇"
    star = 3
    hp = [15]
    hp_max = tuple(hp)
    atk = [2]

    def character(self):
        return "【特性】 生命值低于5点时攻击会附带寒冰，使被攻击的玩家冻结，被冻结的玩家停止行动一回合"


class DaShuYao(Monster):
    name = "大树妖"
    star = 3
    hp = [20]
    hp_max = tuple(hp)
    shield = 10
    atk = [2]
    self_damage_coe = [0.5, 1, 1]

    def character(self):
        return "【特性】 本体受到的物理伤害减半"


# --------------------★★★★-------------------- #

class AnYanJuLong(Monster):
    name = "暗炎巨龙"
    star = 4
    hp = [25]
    hp_max = tuple(hp)
    atk = [5]

    def character(self):
        return "【特性】 攻击造成真实伤害"


class JiFeng(Monster):
    name = "疾风"
    star = 4
    hp = [20]
    hp_max = tuple(hp)
    atk = [3, 3]

    def character(self):
        return "【特性】 一回合进行两次攻击\n" \
               "【特性】 受到玩家攻击时投掷一枚骰子，若点数为4则攻击无效"

    def attacked(self, attack: Attack):
        if randint(1, 6) != 4:
            super(JiFeng, self).attacked(attack)
        else:
            print("【战斗信息】 掷出4，攻击无效")


class XiXueMo(Monster):
    name = "吸血魔"
    star = 4
    hp = [20]
    hp_max = tuple(hp)
    atk = [2]
    self_damage_coe = [0.5, 1, 1]

    def character(self):
        return "【特性】 每次攻击若造成伤害则恢复5点生命值\n" \
               "【特性】 本体受到的物理伤害减半"


class JiHunChongQun(Monster):
    name = "汲魂虫群"
    star = 4
    hp = [10, 10, 10, 10, 10]
    hp_max = tuple(hp)
    atk = [1, 1, 1, 1, 1]

    def character(self):
        return "【特性】 攻击造成真实伤害\n" \
               "【特性】 若有玩家阵亡，则虫群数量恢复至最大值"


# --------------------★★★★★-------------------- #

class JuYanLong(Monster):
    name = "巨岩龙"
    star = 5
    hp = [30]
    hp_max = tuple(hp)
    shield = 20
    atk = [3]
    self_damage_coe = [0.5, 1, 1]

    def character(self):
        return "【特性】 本体受到的物理伤害减半"
