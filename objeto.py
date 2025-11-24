class Objeto:
    def __init__(self, object: dict):
        self._name = object['name']
        self._life = object['life']
        self._life_reg = object['life_reg']
        self._mana = object['mana']
        self._mana_reg = object['mana_reg']
        self._attack_damange = object['attack_damange']
        self._attack_speed = object['attack_speed']
        self._armor = object['armor']
        self._magic_res = object['magic_res']
        self._movement = object['movement']
        self._ability_power = object['ability_power']
        self._critical_impact = object['critical_impact']
        self._life_steal = object['life_steal']
        self._omnivamp = object['omnivamp']
        self._flat_armor_penetration = object['flat_armor_penetration']
        self._percentage_armor_penetration = object['percentage_armor_penetration']
        self._magic_penetration = object['magic_penetration']
        self._ability_haste = object['ability_haste']
        
    def get_nombre(self):
        return self._name
        
    def get_life(self):
        return self._life
        
    def get_life_reg(self):
        return self._life_reg
    
    def get_mana(self):
        return self._mana
    
    def get_mana_reg(self):
        return self._mana_reg
    
    def get_attack_damange(self):
        return self._attack_damange
    
    def get_attack_speed(self):
        return self._attack_speed
    
    def get_armor(self):
        return self._armor
    
    def get_magic_res(self):
        return self._magic_res
    
    def get_movement(self):
        return self._movement
    
    def get_ability_power(self):
        return self._ability_power
    
    def get_critical_impact(self):
        return self._critical_impact
    
    def get_life_steal(self):
        return self._life_steal
    
    def get_omnivamp(self):
        return self._omnivamp
    
    def get_flat_armor_penetration(self):
        return self._flat_armor_penetration
    
    def get_percentage_armor_penetration(self):
        return self._percentage_armor_penetration
    
    def get_magic_penetration(self):
        return self._magic_penetration
    
    def get_ability_haste(self):
        return self._ability_haste
