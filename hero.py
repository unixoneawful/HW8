class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points,catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    def nam(self):
        print(self.name)
    def hp(self):
        print(self.health_points * 2)
    def __str__(self):
        print(self.nickname, self.superpower, self.health_points)
    def __len__(self):
        print(len(self.catchphrase))
Hero = SuperHero('Emir', 'unix', 'healing', 100, 'хилюс')
Hero.nam()
Hero.hp()
Hero.__str__()
Hero.__len__()
class Hero(SuperHero):

    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        print(f'Здоровье нашего героя: {self.health_points ** 2}')

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')

    # def crit(self):
    #     return self.damage ** 2


class SecondHero(SuperHero):

    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp(self):
        self.fly = True
        print(f'Здоровье нашего героя: {self.health_points ** 2}')

    def fly_sky(self):
        print(f'fly in the {self.fly}_phrase')

thor = Hero('thor', 'bog', 'grom', 200, 'хз', damage=100)
cap = SecondHero('cap', 'pon', 'hello', 150, 'ladno', damage=200)

thor.hp()
thor.fly_sky()
cap.hp()
cap.fly_sky()


class Villian(SecondHero):

    def __init__(self,  name, nickname, superpower, health_points, catchphrase):
        super().__init__( name, nickname, superpower, health_points, catchphrase)
        SuperHero.people = 'monster'

    def gen_X(self):
        pass

    def crit(self, hero):
        return hero.damage ** 2

tanos = Villian('tanos', 'tanka', 'kamni', 900, 'pon')
print(Villian.crit(tanos, thor))
print(Villian.crit(tanos, cap))