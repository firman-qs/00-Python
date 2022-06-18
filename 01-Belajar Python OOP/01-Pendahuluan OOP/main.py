'''
# Paradigma Pemrograman
1. Structural --> Procedural 
    eksekusi berdasarkan urutan

2. Object Oriented
    eksekusi berdasarkan obejek
'''

# membuat class
# deklarasikan di atas sebelum sintax

class Hero: # template
    pass


hero1 = Hero() # objek atau instance (instantiate)
hero2 = Hero()

hero1.name = "Grimstroke"
hero1.health = "560"

hero2.name = "Hoodwink"
hero2.health = "550"

print(hero1)
print(hero1.__dict__)
print(hero1.name)