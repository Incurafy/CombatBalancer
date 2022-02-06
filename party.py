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
        self.avg_max_hp = self.calc_avg_max_hp()
        self.avg_att_bonus = self.calc_avg_att_bonus()
    
    def calc_avg_ac(self):
        return (math.floor((self.asher.armour_class + self.azrael.armour_class
                + self.unai.armour_class + self.tor.armour_class)
                / NUM_CHARACTERS))
    
    def calc_avg_max_hp(self):
        return (math.floor((self.asher.max_hp + self.azrael.max_hp
                + self.unai.max_hp + self.tor.max_hp)
                / NUM_CHARACTERS))
        
    def calc_avg_att_bonus(self):
        return (math.floor((self.asher.att_bonus + self.azrael.att_bonus
                + self.unai.att_bonus + self.tor.att_bonus)
                / NUM_CHARACTERS))        

    # Minor enemies
    def calc_avg_r1_att_dmg_minor(self):
        return (math.floor((self.asher.avg_r1_att_dmg_minor 
                            + self.azrael.avg_r1_att_dmg_minor 
                            + self.unai.avg_r1_att_dmg_minor 
                            + self.tor.avg_r1_att_dmg_minor))
                / NUM_CHARACTERS)

    def calc_avg_r2_att_dmg_minor(self):
        return (math.floor((self.asher.avg_r2_att_dmg_minor 
                            + self.azrael.avg_r2_att_dmg_minor 
                            + self.unai.avg_r2_att_dmg_minor 
                            + self.tor.avg_r2_att_dmg_minor))
                / NUM_CHARACTERS)
        
    def calc_avg_r3_att_dmg_minor(self):
        return (math.floor((self.asher.avg_r3_att_dmg_minor 
                            + self.azrael.avg_r3_att_dmg_minor 
                            + self.unai.avg_r3_att_dmg_minor 
                            + self.tor.avg_r3_att_dmg_minor))
                / NUM_CHARACTERS)
    
    # Major enemies
    def calc_avg_r1_att_dmg_major(self):
        return (math.floor((self.asher.avg_r1_att_dmg_major 
                            + self.azrael.avg_r1_att_dmg_major 
                            + self.unai.avg_r1_att_dmg_major 
                            + self.tor.avg_r1_att_dmg_major))
                / NUM_CHARACTERS)

    def calc_avg_r2_att_dmg_major(self):
        return (math.floor((self.asher.avg_r2_att_dmg_major 
                            + self.azrael.avg_r2_att_dmg_major 
                            + self.unai.avg_r2_att_dmg_major 
                            + self.tor.avg_r2_att_dmg_major))
                / NUM_CHARACTERS)
        
    def calc_avg_r3_att_dmg_major(self):
        return (math.floor((self.asher.avg_r3_att_dmg_major 
                            + self.azrael.avg_r3_att_dmg_major 
                            + self.unai.avg_r3_att_dmg_major 
                            + self.tor.avg_r3_att_dmg_major))
                / NUM_CHARACTERS)
    
    # Bosses
    def calc_avg_r1_att_dmg_bosses(self):
        return (math.floor((self.asher.avg_r1_att_dmg_bosses
                            + self.azrael.avg_r1_att_dmg_bosses
                            + self.unai.avg_r1_att_dmg_bosses 
                            + self.tor.avg_r1_att_dmg_bosses))
                / NUM_CHARACTERS)

    def calc_avg_r2_att_dmg_bosses(self):
        return (math.floor((self.asher.avg_r2_att_dmg_bosses
                            + self.azrael.avg_r2_att_dmg_bosses
                            + self.unai.avg_r2_att_dmg_bosses
                            + self.tor.avg_r2_att_dmg_bosses))
                / NUM_CHARACTERS)
        
    def calc_avg_r3_att_dmg_bosses(self):
        return (math.floor((self.asher.avg_r3_att_dmg_bosses
                            + self.azrael.avg_r3_att_dmg_bosses
                            + self.unai.avg_r3_att_dmg_bosses
                            + self.tor.avg_r3_att_dmg_bosses))
                / NUM_CHARACTERS)

    def desc(self):
        return ("Average AC: " + str(self.avg_ac) + "\n"
                + "Average Max HP: " + str(self.avg_max_hp) + "\n"
                + "Average Attack Bonus: " + str(self.avg_att_bonus))
