#!/usr/bin/env python
# -*- coding: utf-8 -*-

from monster import *


def loop():
    mst = JuYanLong()
    print(mst)
    print(mst.character())
    print("--------------【开始攻击】--------------")
    while mst.is_alive:
        while (atk := input()) != "-1":
            if "hp" in atk:
                mst.heal(*map(int, atk[3:].split()))
            elif atk == "rv":
                mst.revival()
            else:
                mst.attacked(Attack(*map(int, atk.split())))
        print(f"【怪物信息】 生命：{mst.hp}, 护盾：{mst.shield}")
        print(f"【怪物攻击】 攻击力: {mst.atk}, AOE: {mst.aoe}")
    print(f"--------------【讨伐成功】--------------")


if __name__ == "__main__":
    loop()
