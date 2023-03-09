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