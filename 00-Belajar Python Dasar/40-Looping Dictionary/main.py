# looping dictionary

heroDB   = {
    "ck"    : "Chaos Knight",
    "dk"    : "Dragon Knight",
    "ww"    : "Winter Wayvern",
    "tb"    : "Terror Blade",
    "cm"    : "Crystal Maiden"
}

# looping biasa
for i in heroDB :
    print(i)
    
for i in heroDB :
    print(f"{i} = {heroDB.get(i)}")

# operator untuk mengambil item iterable
keys = heroDB.keys() # keys
print(keys)

for key in keys:
    print(key)

values = heroDB.values() # values
print(values)

for value in values:
    print(value)

for value in heroDB.values():
    print(value.upper())
    
for index,key in enumerate(heroDB):
    print(f"{index} = {key}")

items = heroDB.items() # items
print(items)

for item in items:
    print(item)

for key,value in heroDB.items():
    print(f"{key} = {value}") 
    