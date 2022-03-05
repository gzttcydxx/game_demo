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