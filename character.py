# character.py

NAME = 0
PRIMARY_STAT = 1
SAVE_DC_STAT = 2
SAVE_PROF_1 = 3
SAVE_PROF_2 = 4
STRENGTH = 5
DEXTERITY = 6
CONSTITUTION = 7
INTELLIGENCE = 8
WISDOM = 9
CHARISMA = 10
HIT_POINTS = 11
ARMOUR_CLASS = 12
PROF_BONUS = 13
MW_BONUS = 14

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
                return STRENGTH
            case "dex":
                return DEXTERITY
            case "con":
                return CONSTITUTION
            case "int":
                return INTELLIGENCE
            case "wis":
                return WISDOM
            case "cha":
                return CHARISMA
            case _:
                return "kittyflesh"
    
    def __init__(self, file) -> None:
        self.stats = self.parse_file(file)
        self.name = self.stats[NAME]
        self.primary_stat = int(self.stats[PRIMARY_STAT])
        self.save_dc_stat = int(self.stats[SAVE_DC_STAT])
        self.save_prof_1 = int(self.stats[self.parse_save_prof(self.stats[SAVE_PROF_1])])
        self.save_prof_2 = int(self.stats[self.parse_save_prof(self.stats[SAVE_PROF_2])])
        self.strength = int(self.stats[STRENGTH])
        self.dexterity = int(self.stats[DEXTERITY])
        self.constitution = int(self.stats[CONSTITUTION])
        self.intelligence = int(self.stats[INTELLIGENCE])
        self.wisdom = int(self.stats[WISDOM])
        self.charisma = int(self.stats[CHARISMA])
        self.hit_points = int(self.stats[HIT_POINTS])
        self.armour_class = int(self.stats[ARMOUR_CLASS])
        self.prof_bonus = int(self.stats[PROF_BONUS])
        self.mw_bonus = int(self.stats[MW_BONUS])
        self.att_bonus = self.prof_bonus + self.primary_stat + self.mw_bonus
        self.save_dc = 8 + self.prof_bonus + self.save_dc_stat

    def desc(self):
        return ("Name: " + self.name + "\n"
                + "STR: " + str(self.strength) + "\n"
                + "DEX: " + str(self.dexterity) + "\n"
                + "CON: " + str(self.constitution) + "\n"
                + "INT: " + str(self.intelligence) + "\n"
                + "WIS: " + str(self.wisdom) + "\n"
                + "CHA: " + str(self.charisma) + "\n"
                + "HP: " + str(self.hit_points) + "\n"
                + "AC: " + str(self.armour_class) + "\n"
                + "AB: " + str(self.att_bonus) + "\n"
                + "Sv DC: " + str(self.save_dc) + "\n"
                + "Save 1: " + str(self.save_prof_1) + "\n"
                + "Save 2: " + str(self.save_prof_2))