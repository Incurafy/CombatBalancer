# party.py

import math
from character import Character

ASHER = "characters/asher.txt"
AZRAEL = "characters/azrael.txt"
UNAI = "characters/unai.txt"
TOR = "characters/tor.txt"
NUM_CHARACTERS = 4

class Party:
    def __init__(self) -> None:
        self.asher = Character(ASHER)
        self.azrael = Character(AZRAEL)
        self.unai = Character(UNAI)
        self.tor = Character(TOR)
        self.avg_ac = self.calc_avg_ac()
        self.avg_hp = self.calc_avg_hp()
    
    def calc_avg_ac(self):
        return (math.floor((self.asher.armour_class + self.azrael.armour_class
                + self.unai.armour_class + self.tor.armour_class)
                / NUM_CHARACTERS))
    
    def calc_avg_hp(self):
        return (math.floor((self.asher.hit_points + self.azrael.hit_points
                + self.unai.hit_points + self.tor.hit_points)
                / NUM_CHARACTERS)) 
        
    def desc(self):
        return ("Average AC: " + str(self.avg_ac) + "\n"
                + "Average HP: " + str(self.avg_hp))