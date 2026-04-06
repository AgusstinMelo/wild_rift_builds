class Objeto:
    def __init__(self, object: dict):
        self._nombre = object['name']
        self._descripcion = object['description']
        self._vida = object['life']
        self._regeneracion_de_vida = object['life_reg']
        self._mana = object['mana']
        self._regeneracion_de_mana = object['mana_reg']
        self._daño_de_ataque = object['attack_damange']
        self._velocidad_de_ataque = object['attack_speed']
        self._armadura = object['armor']
        self._resistencia_magica = object['magic_res']
        self._movimiento_plano = object['flat_movement']
        self._movimiento_porcentual = object['percentage_movement']
        self._poder_de_habilidad = object['ability_power']
        self._impacto_critico = object['critical_impact']
        self._daño_critico = object['critical_damange']
        self._vampirismo_fisico = object['physic_vamp']
        self._vampirismo_magico = object['magic_vamp']
        self._penetracion_de_armadura_plana = object['flat_armor_penetration']
        self._penetracion_de_armadura_porcentual = object['percentage_armor_penetration']
        self._penetracion_magica = object['flat_magic_penetration']
        self._penetracion_magica_porcentual = object['percentage_magic_penetration']
        self._velocidad_de_habilidades = object['ability_haste']
        self._tenacidad = object['tenacity']
        self._curacion_y_escudo = object['healing-and-shield']
        self._daño_adaptable_ad = object.get('adaptable_ad', 0)
        self._daño_adaptable_ap = object.get('adaptable_ap', 0)

    def get_nombre(self):
        return self._nombre

    def get_descripcion(self):
        return self._descripcion

    def get_vida(self):
        return self._vida

    def get_regeneracion_de_vida(self):
        return self._regeneracion_de_vida

    def get_mana(self):
        return self._mana

    def get_regeneracion_de_mana(self):
        return self._regeneracion_de_mana

    def get_daño_de_ataque(self):
        return self._daño_de_ataque

    def get_velocidad_de_ataque(self):
        return self._velocidad_de_ataque

    def get_armadura(self):
        return self._armadura

    def get_resistencia_magica(self):
        return self._resistencia_magica

    def get_movimiento_plano(self):
        return self._movimiento_plano

    def get_movimiento_porcentual(self):
        return self._movimiento_porcentual

    def get_poder_de_habilidad(self):
        return self._poder_de_habilidad

    def get_impacto_critico(self):
        return self._impacto_critico

    def get_daño_critico(self):
        return self._daño_critico

    def get_vampirismo_fisico(self):
        return self._vampirismo_fisico

    def get_vampirismo_magico(self):
        return self._vampirismo_magico

    def get_penetracion_de_armadura_plana(self):
        return self._penetracion_de_armadura_plana

    def get_penetracion_de_armadura_porcentual(self):
        return self._penetracion_de_armadura_porcentual

    def get_penetracion_magica(self):
        return self._penetracion_magica

    def get_penetracion_magica_porcentual(self):
        return self._penetracion_magica_porcentual

    def get_velocidad_de_habilidades(self):
        return self._velocidad_de_habilidades

    def get_tenacidad(self):
        return self._tenacidad

    def get_curacion_y_escudo(self):
        return self._curacion_y_escudo

    def get_daño_adaptable_ad(self):
        return self._daño_adaptable_ad

    def get_daño_adaptable_ap(self):
        return self._daño_adaptable_ap

    def tiene_daño_adaptable(self):
        return self._daño_adaptable_ad > 0 or self._daño_adaptable_ap > 0

    def print_stats(self):
        for atributo, valor in self.__dict__.items():
            if isinstance(valor, (int, float)) and valor != 0:
                print(f"{atributo.title().replace('_', ' ')} : {valor}")