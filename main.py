# main.py

from balance import Balance

balance = Balance()

chance = balance.calc_hit_chance(7, 18, 1, True, False)
print(f"Chance to hit AC: {chance}%")