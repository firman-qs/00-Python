import os 
os.system("cls")

# constructor __init__(self,argumen1,argumen2,argumenN)
class hero: # template
    # class variable
    list = []
    nomorHero = 1
    def __init__(self,heroName, heroSpeed, heroHealth, heroArmor):
        # instance variable
        self.name = heroName
        self.speed = heroSpeed
        self.health = heroHealth
        self.armor = heroArmor
    
        dict_hero = {
            hero.nomorHero : {
                'nama' : self.name,
                'speed' : self.speed,
                'health' : self.health,
                'armor' : self.armor
            }
        }
        
        print(f"""
{'No':7} => {hero.nomorHero}
{'Nama':<7} => {dict_hero[hero.nomorHero]['nama']}
{'Speed':<7} => {dict_hero[hero.nomorHero]['speed']}
{'Health':<7} => {dict_hero[hero.nomorHero]['health']}
{'Armor':<7} => {dict_hero[hero.nomorHero]['armor']}
        """)
        
        hero.nomorHero += 1
        
hero1 = hero("Sniper",330,550,30)
hero2 = hero("Mirana",340,560,20)




