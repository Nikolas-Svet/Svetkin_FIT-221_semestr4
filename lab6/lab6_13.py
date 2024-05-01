class Weapon:

    def __init__(self, name, damage, range):
        self.name = name
        self.damage = damage
        self.range = range

    def hit(self, actor, target):
        if target.is_alive():
            print(1)
        else:
            print("Враг уже повержен!")

    def __str__(self):
        return self.name


class BaseCharacter:

    def __init__(self, x, y):
        self.delta_x = x
        self.delta_y = y
        self.hp = 100

    def move(self, delta_x, delta_y):
        self.delta_x += delta_x
        self.delta_y += delta_y

    def get_damage(self, amount):
        self.hp -= amount

    def get_coords(self):
        return self.delta_x, self.delta_y


class BaseEnemy(BaseCharacter):

    def __init__(self, x, y, weapon):
        self.weapon = weapon
        super.__init__(x, y, 100)

    def hit(self, target):
        print(1)

    def __str__(self):
        print(f"Враг на позиции ({self.delta_x},{self.delta_y}) с оружием {self.weapon.name}")


class MainHero(BaseCharacter):
    def __init__(self, x, y, hp, name):
        self.name = name
        super().__init__(x, y, hp)
        self.current_weapon = 0
        self.list_weapon = []

    def hit(self, target):
        if self.weapon == 0:
            print("Я обезоружен")
        else:
            print(1)

    def add_wepon(self, weapon):
        if isinstance(weapon, Weapon):
            if len(self.list_weapon) == 0:
                self.list_weapon.append(weapon)
                self.current_weapon = self.list_weapon[0]
            else:
                self.list_weapon.append(weapon)
            print("Подобрал оружие", weapon.name)
        else:
            print("Это не оружие")

    def next_weapon(self):
        if len(self.list_weapon) == 0:
            print("Я обезоружен")
        elif len(self.list_weapon) == 1:
            print("У меня только одно оружие")
        else:
            print(1)

    def heal(self, amount):
        if (self.hp + amount) > 200:
            print("Вылечиться нельзя, так как hp не должно превышать 200")
        else:
            self.hp += amount
            print("Полечился, теперь здоровья", self.hp)
