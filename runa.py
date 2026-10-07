class Runa:
    def __init__(self, rune: dict):
        self._nombre = rune['name']
        self._tipo = rune['type']
        self._descripcion = rune['description']
        self._vida = rune.get('life', 0)
        self._regeneracion_de_vida = rune.get('life_reg', 0)
        self._mana = rune.get('mana', 0)
        self._regeneracion_de_mana = rune.get('mana_reg', 0)
        self._daño_de_ataque = rune.get('attack_damange', 0)
        self._velocidad_de_ataque = rune.get('attack_speed', 0)
        self._armadura = rune.get('armor', 0)
        self._resistencia_magica = rune.get('magic_res', 0)
        self._movimiento_plano = rune.get('flat_movement', 0)
        self._movimiento_porcentual = rune.get('percentage_movement', 0)
        self._poder_de_habilidad = rune.get('ability_power', 0)
        self._impacto_critico = rune.get('critical_impact', 0)
        self._daño_critico = rune.get('critical_damange', 0)
        self._vampirismo_fisico = rune.get('physic_vamp', 0)
        self._vampirismo_magico = rune.get('magic_vamp', 0)
        self._penetracion_de_armadura_plana = rune.get('flat_armor_penetration', 0)
        self._penetracion_de_armadura_porcentual = rune.get('percentage_armor_penetration', 0)
        self._penetracion_magica = rune.get('flat_magic_penetration', 0)
        self._penetracion_magica_porcentual = rune.get('percentage_magic_penetration', 0)
        self._velocidad_de_habilidades = rune.get('ability_haste', 0)
        self._tenacidad = rune.get('tenacity', 0)
        self._curacion_y_escudo = rune.get('healing-and-shield', 0)

    def get_nombre(self):
        return self._nombre
    
    def get_type(self):
        return self._tipo
    
    def get_rama(self):
        return self._tipo[0]
    
    def get_slot(self):
        if len(self._tipo) > 1:
            return self._tipo[1]
        return None

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
    
    def print_stats(self):
        for atributo, valor in self.__dict__.items():
            if isinstance(valor, (int, float)) and valor != 0:
                print(f"{atributo.title().replace('_', ' ')} : {valor}")