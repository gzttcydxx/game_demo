class Attack:
    def __init__(self, physiical: int, magical: int, real: int, anti_shield: int = 0, which: int = 0, aoe: bool = False, is_penetrate: bool = False, is_frozen: bool = False, is_inescapable: bool = False):
        # 攻击力（0 -> 物理, 1 -> 魔法, 2 -> 真实, 3 -> 对盾额外伤害）
        self.atk = [physiical, magical, real, anti_shield]
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
    
    def __or__(self, other):
        return Attack(self.atk[0]+other.atk[0],
                      self.atk[1]+other.atk[1],
                      self.atk[2]+other.atk[2],
                      self.atk[3]+other.atk[3],
                      self.which,
                      self.aoe or other.aoe,
                      self.is_penetrate or other.is_penetrate,
                      self.is_inescapable or other.is_inescapable,
                      self.is_frozen or other.is_frozen)
    
    def __str__(self) -> str:
        return '{} {} {} {} {} {} {} {} {}'.format(self.atk[0], self.atk[1], self.atk[2], self.atk[3], self.which, self.aoe, self.is_penetrate, self.is_inescapable, self.is_frozen)


if __name__ == "__main__":
    a = Attack(1, 2, 3, 4, 5, True, False, True, False)
    b = Attack(1, 2, 3, 4, 5, True, True, False, False)
    print(a | b)