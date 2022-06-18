# constructor __init__(self,argumen1,argumen2,argumenN)
class hero: # template
    
    def __init__(self,heroName, heroSpeed, heroHealth, heroArmor):
        self.name = heroName
        self.speed = heroSpeed
        self.health = heroHealth
        self.armor = heroArmor

hero1 = hero("Sniper",330,550,30)
hero2 = hero("Mirana",340,560,20)

print(hero1.name)
print(hero1.__dict__)


