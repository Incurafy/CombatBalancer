# character.py

import math

NAME = 0
PRIMARY_MOD = 1
SAVE_DC_MOD = 2
SAVE_PROF_1 = 3
SAVE_PROF_2 = 4
STR_MOD = 5
DEX_MOD = 6
CON_MOD = 7
INT_MOD = 8
WIS_MOD = 9
CHA_MOD = 10
MAX_HIT_POINTS = 11
ARMOUR_CLASS = 12
PROF_BONUS = 13
WPN_ATT_BONUS = 14
WPN_DMG_BONUS = 15
NUM_ATTACKS = 16
AVG_R1_ATT_DMG_MINOR = 17
AVG_R2_ATT_DMG_MINOR = 18
AVG_R3_ATT_DMG_MINOR = 19
AVG_R1_ATT_DMG_MAJOR = 20
AVG_R2_ATT_DMG_MAJOR = 21
AVG_R3_ATT_DMG_MAJOR = 22
AVG_R1_ATT_DMG_BOSSES = 23
AVG_R2_ATT_DMG_BOSSES = 24
AVG_R3_ATT_DMG_BOSSES = 25
AVG_EXTRA_DMG_PER_ROUND = 26

class Character:
    def parse_file(self, file):
        stats = open(file).read().splitlines()        
        for x in range(len(stats)):        
            temp = stats[x].split()
            stats[x] = temp[1]
        return stats
    
    def parse_save_prof(self, str):
        match str:
            case "str":
                return STR_MOD
            case "dex":
                return DEX_MOD
            case "con":
                return CON_MOD
            case "int":
                return INT_MOD
            case "wis":
                return WIS_MOD
            case "cha":
                return CHA_MOD
            case _:
                return "kittyflesh"
    
    def __init__(self, file) -> None:
        self.stats = self.parse_file(file)
        self.name = self.stats[NAME]
        self.primary_mod = int(self.stats[PRIMARY_MOD])
        self.save_dc_mod = int(self.stats[SAVE_DC_MOD])
        self.save_prof_1 = int(self.stats[self.parse_save_prof(self.stats[SAVE_PROF_1])])
        self.save_prof_2 = int(self.stats[self.parse_save_prof(self.stats[SAVE_PROF_2])])
        self.str_mod = int(self.stats[STR_MOD])
        self.dex_mod = int(self.stats[DEX_MOD])
        self.con_mod = int(self.stats[CON_MOD])
        self.int_mod = int(self.stats[INT_MOD])
        self.wis_mod = int(self.stats[WIS_MOD])
        self.cha_mod = int(self.stats[CHA_MOD])
        self.max_hp = int(self.stats[MAX_HIT_POINTS])
        self.armour_class = int(self.stats[ARMOUR_CLASS])
        self.prof_bonus = int(self.stats[PROF_BONUS])
        self.wpn_att_bonus = int(self.stats[WPN_ATT_BONUS])
        self.wpn_dmg_bonus = int(self.stats[WPN_DMG_BONUS])
        self.num_attacks = int(self.stats[NUM_ATTACKS])
        self.avg_r1_att_dmg_minor = float(self.stats[AVG_R1_ATT_DMG_MINOR])
        self.avg_r2_att_dmg_minor = float(self.stats[AVG_R2_ATT_DMG_MINOR])
        self.avg_r3_att_dmg_minor = float(self.stats[AVG_R3_ATT_DMG_MINOR])
        self.avg_r1_att_dmg_major = float(self.stats[AVG_R1_ATT_DMG_MAJOR])
        self.avg_r2_att_dmg_major = float(self.stats[AVG_R2_ATT_DMG_MAJOR])
        self.avg_r3_att_dmg_major = float(self.stats[AVG_R3_ATT_DMG_MAJOR])
        self.avg_r1_att_dmg_bosses = float(self.stats[AVG_R1_ATT_DMG_BOSSES])
        self.avg_r2_att_dmg_bosses = float(self.stats[AVG_R2_ATT_DMG_BOSSES])
        self.avg_r3_att_dmg_bosses = float(self.stats[AVG_R3_ATT_DMG_BOSSES])
        self.avg_extra_dmg_per_round = float(self.stats[AVG_EXTRA_DMG_PER_ROUND])
        self.att_bonus = self.prof_bonus + self.primary_mod + self.wpn_att_bonus
        self.save_dc = 8 + self.prof_bonus + self.save_dc_mod

    def desc(self):
        return ("Name: " + self.name + "\n"
                + "STR: " + str(self.str_mod) + "\n"
                + "DEX: " + str(self.dex_mod) + "\n"
                + "CON: " + str(self.con_mod) + "\n"
                + "INT: " + str(self.int_mod) + "\n"
                + "WIS: " + str(self.wis_mod) + "\n"
                + "CHA: " + str(self.cha_mod) + "\n"
                + "HP: " + str(self.max_hp) + "\n"
                + "AC: " + str(self.armour_class) + "\n"
                + "AB: " + str(self.att_bonus) + "\n"
                + "Sv DC: " + str(self.save_dc) + "\n"
                + "Save 1: " + str(self.save_prof_1) + "\n"
                + "Save 2: " + str(self.save_prof_2))
