from objeto import Objeto

class Campeon:
    def __init__(self, champ: dict):
        self._name = champ['name']
        self._life = champ['life']
        self._life_reg = champ['life_reg']
        self._mana = champ['mana']
        self._mana_reg = champ['mana_reg']
        self._attack_damange = champ['attack_damange']
        self._attack_speed = champ['attack_speed']
        self._armor = champ['armor']
        self._magic_res = champ['magic_res']
        self._movement = champ['movement']
        self._ability_power = 0
        self._critical_impact = 0
        self._life_steal = 0
        self._omnivamp = 0
        self._flat_armor_penetration = 0
        self._percentage_armor_penetration = 0
        self._magic_penetration = 0
        self._ability_haste = 0
        
    
    def get_nombre(self):
        return self._name
 
    def print_stats(self):
        print(
            f'name: {self._name}\n' \
            f'life: {self._life}\n' \
            f'life reg: {self._life_reg}\n' \
            f'mana: {self._mana}\n' \
            f'mana reg: {self._mana_reg}\n' \
            f'attack damange: {self._attack_damange}\n' \
            f'armor: {self._armor}\n' \
            f'magic res: {self._magic_res}\n' \
            f'movement: {self._movement}\n' \
            f'ability power: {self._ability_power}\n' \
            f'critical impact: {self._critical_impact}\n' \
            f'life steal: {self._life_steal}\n' \
            f'omnivamp: {self._omnivamp}\n' \
            f'flat armor penetration: {self._flat_armor_penetration}\n' \
            f'percentage armor penetration: {self._percentage_armor_penetration}\n' \
            f'magic penetration: {self._magic_penetration}\n' \
            f'ability haste: {self._ability_haste}\n' \
        )
        
        
    def set_life(self, life: int):
        self._life += life
        
    def set_life_reg(self, life_reg):
        self._life_reg += (self._life_reg * life_reg) / 100
        
    def set_mana(self, mana):
        self._mana += mana
        
    def set_mana_reg(self, mana_reg):
        self._mana_reg += (self._mana_reg * mana_reg) / 100
        
    def set_attack_damange(self, attack_damange):
        self._attack_damange += attack_damange
        
    def set_attack_speed(self, attack_speed):
        self._attack_speed += (self._attack_speed * attack_speed) / 100
        
    def set_armor(self, armor):
        self._armor += armor
        
    def set_magic_res(self, magic_res):
        self._magic_res += magic_res
        
    def set_movement(self, movement):
        self._movement += movement
        
    def set_ability_power(self, ability_power):
        self._ability_power += ability_power
        
    def set_critical_impact(self, critical_impact):
        self._critical_impact += critical_impact
        
    def set_life_steal(self, life_steal):
        self._life_steal += life_steal
        
    def set_omnivamp(self, omnivamp):
        self._omnivamp += omnivamp
        
    def set_flat_armor_penetration(self, flat_armor_pen):
        self._flat_armor_penetration += flat_armor_pen
        
    def set_percentage_armor_penetration(self, percentage_armor_pen):
        self._percentage_armor_penetration += percentage_armor_pen
        
    def set_magic_penetration(self, magic_pen):
        self._magic_penetration += magic_pen
        
    def set_ability_haste(self, ability_haste):
        self._ability_haste += ability_haste
    
    def use_object(self, obj: Objeto):
        self.set_life(obj.get_life())
        self.set_life_reg(obj.get_life_reg())
        self.set_mana(obj.get_mana())
        self.set_mana_reg(obj.get_mana_reg())
        self.set_attack_damange(obj.get_attack_damange())
        self.set_attack_speed(obj.get_attack_speed())
        self.set_armor(obj.get_armor())
        self.set_magic_res(obj.get_magic_res())
        self.set_movement(obj.get_movement())
        self.set_ability_power(obj.get_ability_power())
        self.set_critical_impact(obj.get_critical_impact())
        self.set_life_steal(obj.get_life_steal())
        self.set_omnivamp(obj.get_omnivamp())
        self.set_flat_armor_penetration(obj.get_flat_armor_penetration())
        self.set_percentage_armor_penetration(obj.get_percentage_armor_penetration())
        self.set_magic_penetration(obj.get_magic_penetration())
        self.set_ability_haste(obj.get_ability_haste())
    