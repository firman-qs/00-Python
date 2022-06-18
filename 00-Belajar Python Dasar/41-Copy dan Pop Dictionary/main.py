# copy dictionary

hero_dota = {
    "ck" : "Chaos Knight",
    "dk" : "Dragon Knight",
    "ww" : "Winter Wayvern",
    "tb" : "Terror Blade",
    "cm" : "Crystal Maiden"
}

hero_dota_copy = hero_dota.copy()  # dengan .copy()
# hero_dota_copy = hero_dota # tanpa .copy()

print(f"Hero Dota = {hero_dota}\n")
print(f"Hero Dota Copy = {hero_dota_copy}\n")

hero_dota["dk"] = "Drive King"
print(f"Hero Dota = {hero_dota}\n")
print(f"Hero Dota Copy = {hero_dota_copy}\n")

# pop dictionary (berdasarkan key)
hero_dota_ck = hero_dota_copy.pop("ck")
print(f"Hero Dota = {hero_dota_copy}\n")
print(f"Hero Dota CK = {hero_dota_ck}")

# pop item (yang terakhir)
hero_dota_last = hero_dota.popitem()
print(f"Hero Dota = {hero_dota_copy}\n")
print(f"Hero Dota Terakhir = {hero_dota_last}\n")