import random

print('몬스터월드에 오신것을 환영합니다!')

character_name = input('캐릭터의 이름을 설정해주세요 : ')


class Character:
    """
    모든 캐릭터의 모체가 되는 클래스
    """

    def __init__(self, name, hp, power, mp, magic_power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power
        self.max_mp = mp
        self.mp = mp
        self.magic_power = magic_power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

        return other.hp

    def magic_attack(self, other):
        mg_damage = random.randint(
            self.magic_power - 4, self.magic_power + 4)
        other.hp = max(other.hp - mg_damage, 0)
        self.mp = self.mp - 10
        print(f'{self.name}이 {other.name}에게 {mg_damage}의 마법 데미지를 입혔습니다.')
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

        return other.hp

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp} MP {self.mp}/{self.max_mp}")


class Monster:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

        return other.hp

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


def character_action():
    print('< 공격 선택 >')
    print('1. 물리 공격')
    print('2. 마법 공격 (*MP 10소모)')
    c_skill_input = int(input('사용할 공격의 번호를 입력하세요. : '))

    # 물리 공격
    if c_skill_input == 1:
        m.hp = c.attack(m)

    # 마법 공격
    elif c_skill_input == 2:
        m.hp = c.magic_attack(m)


def monster_action():
    c.hp = m.attack(c)


c = Character(character_name, 100, 10, 100, 10)
m = Monster('몬스터', 100, 10)

turn = 0


while True:

    # 턴 시작전 상태 출력
    print('===== 필드 상태 =====')
    c.show_status()
    m.show_status()

    # 캐릭터 턴
    if turn % 2 == 0:
        print('===== 플레이어 공격 =====')

        # 캐릭터 액션
        character_action()

        print('===== 플레이어 공격 종료 =====')

        if m.hp <= 0:
            print('필드에 남아있는 몬스터가 없습니다.')
            print('===== Win! =====')
            break

    # 몬스터 턴
    else:
        print('===== 몬스터 공격 =====')

        # 몬스터 액션
        monster_action()

        print('===== 몬스터 공격 종료 =====')

        if c.hp <= 0:
            print('플레이어 사망!')
            print('===== Game Over =====')
            break

    turn += 1
    print('-------------------')
    print('-------------------')
    print('-------------------')
