# balance.py

from party import Party

class Balance:
    def calc_hit_chance(self, att_bonus, target_ac, num_attacks, adv, disadv):
        if adv:
            return int((1 - ((target_ac - att_bonus - 1)**2 / 400)) * 100)
        elif disadv:
            return int((((21 + att_bonus - target_ac)**2) / 400) * 100)
        else:
            return int(((21 + att_bonus - target_ac) / 20) * 100)
    