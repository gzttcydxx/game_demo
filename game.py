#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 全局游戏类
class GlobalGame:
    # 总人数
    total_num: int
    # 存活人数
    exist_num: int
    # 死亡人数
    dead_num: int
    # 灵魂人数
    ghost_num: int
    # 濒死人数
    dying_num: int
    # 回合数
    turn: int = 1
    # 人物列表
    people: list
    # 怪物列表
    monsters: list
    # 游戏时间
    spent_time: int

    # 游戏结束
    def game_over(game_state: int):
        return 


# 攻击类
class Attack:
    def __init__(self, physiical: int, magical: int, real: int, which: int = 0, aoe: bool = False, is_penetrate: bool = False, is_frozen: bool = False, is_inescapable: bool = False):
        # 攻击力（0 -> 物理, 1 -> 魔法, 2 -> 真实）
        self.atk = [physiical, magical, real]
        # 攻击第几个头
        self.which = which
        # AOE伤害
        self.aoe = aoe
        # 是否无视盾
        self.is_penetrate = is_penetrate
        # 是否必中
        self.is_inescapable = is_inescapable
        # 是否冰冻
        self.is_frozen = is_frozen
        