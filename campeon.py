from objeto import Objeto
import math


class Campeon:
    def __init__(self, champ: dict):
        self._base_stats = {
            'nombre': champ['name'],
            'vida': champ['life'],
            'regeneracion_de_vida': champ['life_reg'],
            'mana': champ['mana'],
            'regeneracion_de_mana': champ['mana_reg'],
            'daño_de_ataque': champ['attack_damange'],
            'velocidad_de_ataque': champ['attack_speed'],
            'bonus_velocidad_de_ataque': champ['bonus_attack_speed'],
            'armadura': champ['armor'],
            'resistencia_magica': champ['magic_res'],
            'movimiento': champ['movement'],
            'movimiento_plano': champ['movement'],
            'movimiento_porcentual': 0,
            'poder_de_habilidad': 0,
            'impacto_critico': 0,
            'daño_critico': 175,
            'vampirismo_fisico': champ['phisic_vamp'],
            'vampirismo_magico': champ['magic_vamp'],
            'penetracion_de_armadura_plana': 0,
            'penetracion_de_armadura_porcentual': 0,
            'penetracion_magica': 0,
            'penetracion_magica_porcentual': 0,
            'tenacidad': 0,
            'velocidad_de_habilidades': 0,
            'curacion_y_escudo': 0,
        }

        self._build = []
        self._runas = []
        self._restore_base_stats()

    def _restore_base_stats(self):
        self._nombre = self._base_stats['nombre']
        self._vida = self._base_stats['vida']
        self._regeneracion_de_vida = self._base_stats['regeneracion_de_vida']
        self._mana = self._base_stats['mana']
        self._regeneracion_de_mana = self._base_stats['regeneracion_de_mana']
        self._daño_de_ataque = self._base_stats['daño_de_ataque']
        self._bonus_velocidad_de_ataque = self._base_stats['bonus_velocidad_de_ataque']
        self.set_velocidad_de_ataque()
        self._armadura = self._base_stats['armadura']
        self._resistencia_magica = self._base_stats['resistencia_magica']
        self._movimiento = self._base_stats['movimiento']
        self._movimiento_plano = self._base_stats['movimiento_plano']
        self._movimiento_porcentual = self._base_stats['movimiento_porcentual']
        self._poder_de_habilidad = self._base_stats['poder_de_habilidad']
        self._impacto_critico = self._base_stats['impacto_critico']
        self._daño_critico = self._base_stats['daño_critico']
        self._vampirismo_fisico = self._base_stats['vampirismo_fisico']
        self._vampirismo_magico = self._base_stats['vampirismo_magico']
        self._penetracion_de_armadura_plana = self._base_stats['penetracion_de_armadura_plana']
        self._penetracion_de_armadura_porcentual = self._base_stats['penetracion_de_armadura_porcentual']
        self._penetracion_magica = self._base_stats['penetracion_magica']
        self._penetracion_magica_porcentual = self._base_stats['penetracion_magica_porcentual']
        self._tenacidad = self._base_stats['tenacidad']
        self._velocidad_de_habilidades = self._base_stats['velocidad_de_habilidades']
        self._curacion_y_escudo = self._base_stats['curacion_y_escudo']

    def get_nombre(self):
        return self._nombre

    def get_movimiento_plano(self):
        return self._movimiento_plano

    def get_movimiento_porcentual(self):
        return self._movimiento_porcentual

    def print_stats(self):
        if self._nombre in ['Akali', 'Ambessa', 'Kennen', 'Lee Sin', 'Shen', 'Zed']:
            print(
            f'Nombre: {self._nombre}\n'
            f'Vida: {self._vida}\n'
            f'Regeneración de vida: {self._regeneracion_de_vida}\n'
            f'Energía: {self._mana}\n'
            f'Regeneración de Energía: {self._regeneracion_de_mana}\n'
            f'Velocidad de movimiento: {self._movimiento}\n'
            f'Armadura: {self._armadura}\n'
            f'Resistencia mágica: {self._resistencia_magica}\n'
            f'Daño de ataque: {self._daño_de_ataque}\n'
            f'Velocidad de ataque: {self._velocidad_de_ataque}\n'
            f'Poder de habilidad: {self._poder_de_habilidad}\n'
            f'Velocidad de habilidades: {self._velocidad_de_habilidades}\n'
            f'Impacto crítico: {self._impacto_critico}%\n'
            f'Daño crítico: {self._daño_critico}%\n'
            f'Vampirismo físico: {self._vampirismo_fisico}%\n'
            f'Vampirismo mágico: {self._vampirismo_magico}%\n'
            f'Penetración de armadura plana: {self._penetracion_de_armadura_plana}\n'
            f'Penetración de armadura porcentual: {self._penetracion_de_armadura_porcentual}%\n'
            f'Penetración mágica: {self._penetracion_magica}\n'
            f'Penetración mágica porcentual: {self._penetracion_magica_porcentual}%\n'
            f'Tenacidad: {self._tenacidad}%\n'
            f'Curación y escudo: {self._curacion_y_escudo}%\n'
        )
        elif self._nombre in ['Aatrox', 'Dr. Mundo', 'Garen', 'Katarina', 'Mordekaiser', 'Rengar', 'Riven', 'Rumble', 'Sett', 'Viego', 'Yasuo', 'Yone' ]:
            print(
            f'Nombre: {self._nombre}\n'
            f'Vida: {self._vida}\n'
            f'Regeneración de vida: {self._regeneracion_de_vida}\n'
            f'Velocidad de movimiento: {self._movimiento}\n'
            f'Armadura: {self._armadura}\n'
            f'Resistencia mágica: {self._resistencia_magica}\n'
            f'Daño de ataque: {self._daño_de_ataque}\n'
            f'Velocidad de ataque: {self._velocidad_de_ataque}\n'
            f'Poder de habilidad: {self._poder_de_habilidad}\n'
            f'Velocidad de habilidades: {self._velocidad_de_habilidades}\n'
            f'Impacto crítico: {self._impacto_critico}%\n'
            f'Daño crítico: {self._daño_critico}%\n'
            f'Vampirismo físico: {self._vampirismo_fisico}%\n'
            f'Vampirismo mágico: {self._vampirismo_magico}%\n'
            f'Penetración de armadura plana: {self._penetracion_de_armadura_plana}\n'
            f'Penetración de armadura porcentual: {self._penetracion_de_armadura_porcentual}%\n'
            f'Penetración mágica: {self._penetracion_magica}\n'
            f'Penetración mágica porcentual: {self._penetracion_magica_porcentual}%\n'
            f'Tenacidad: {self._tenacidad}%\n'
            f'Curación y escudo: {self._curacion_y_escudo}%\n'
        )
        elif self._nombre in ['Gnar', 'Renekton', 'Shyvana', 'Tryndamere' ]:
            print(
            f'Nombre: {self._nombre}\n'
            f'Vida: {self._vida}\n'
            f'Regeneración de vida: {self._regeneracion_de_vida}\n'
            f'Furia: {self._mana}\n'
            f'Velocidad de movimiento: {self._movimiento}\n'
            f'Armadura: {self._armadura}\n'
            f'Resistencia mágica: {self._resistencia_magica}\n'
            f'Daño de ataque: {self._daño_de_ataque}\n'
            f'Velocidad de ataque: {self._velocidad_de_ataque}\n'
            f'Poder de habilidad: {self._poder_de_habilidad}\n'
            f'Velocidad de habilidades: {self._velocidad_de_habilidades}\n'
            f'Impacto crítico: {self._impacto_critico}%\n'
            f'Daño crítico: {self._daño_critico}%\n'
            f'Vampirismo físico: {self._vampirismo_fisico}%\n'
            f'Vampirismo mágico: {self._vampirismo_magico}%\n'
            f'Penetración de armadura plana: {self._penetracion_de_armadura_plana}\n'
            f'Penetración de armadura porcentual: {self._penetracion_de_armadura_porcentual}%\n'
            f'Penetración mágica: {self._penetracion_magica}\n'
            f'Penetración mágica porcentual: {self._penetracion_magica_porcentual}%\n'
            f'Tenacidad: {self._tenacidad}%\n'
            f'Curación y escudo: {self._curacion_y_escudo}%\n'
        )
        else:
            print(
                f'Nombre: {self._nombre}\n'
                f'Vida: {self._vida}\n'
                f'Regeneración de vida: {self._regeneracion_de_vida}\n'
                f'Maná: {self._mana}\n'
                f'Regeneración de Maná: {self._regeneracion_de_mana}\n'
                f'Velocidad de movimiento: {self._movimiento}\n'
                f'Armadura: {self._armadura}\n'
                f'Resistencia mágica: {self._resistencia_magica}\n'
                f'Daño de ataque: {self._daño_de_ataque}\n'
                f'Velocidad de ataque: {self._velocidad_de_ataque}\n'
                f'Poder de habilidad: {self._poder_de_habilidad}\n'
                f'Velocidad de habilidades: {self._velocidad_de_habilidades}\n'
                f'Impacto crítico: {self._impacto_critico}%\n'
                f'Daño crítico: {self._daño_critico}%\n'
                f'Vampirismo físico: {self._vampirismo_fisico}%\n'
                f'Vampirismo mágico: {self._vampirismo_magico}%\n'
                f'Penetración de armadura plana: {self._penetracion_de_armadura_plana}\n'
                f'Penetración de armadura porcentual: {self._penetracion_de_armadura_porcentual}%\n'
                f'Penetración mágica: {self._penetracion_magica}\n'
                f'Penetración mágica porcentual: {self._penetracion_magica_porcentual}%\n'
                f'Tenacidad: {self._tenacidad}%\n'
                f'Curación y escudo: {self._curacion_y_escudo}%\n'
            )

    def set_vida(self, life: int):
        self._vida += life

    def set_regeneracion_de_vida(self, life_reg):
        self._regeneracion_de_vida += (self._regeneracion_de_vida * life_reg) / 100
        self._regeneracion_de_vida = round(self._regeneracion_de_vida, 2)

    def set_mana(self, mana):
        self._mana += mana

    def set_regeneracion_de_mana(self, mana_reg):
        self._regeneracion_de_mana += (self._regeneracion_de_mana * mana_reg) / 100
        self._regeneracion_de_mana = round(self._regeneracion_de_mana, 2)

    def set_daño_de_ataque(self, attack_damange):
        self._daño_de_ataque += attack_damange
        self._daño_de_ataque = math.ceil(self._daño_de_ataque)

    def set_porcentaje_velocidad_de_ataque(self, attack_speed):
        self._bonus_velocidad_de_ataque += attack_speed

    def set_velocidad_de_ataque(self):
        base = self._base_stats['velocidad_de_ataque']
        bonus_total = self._bonus_velocidad_de_ataque
        self._velocidad_de_ataque = round(base * (1 + bonus_total / 100), 2)

    def set_armadura(self, armor):
        self._armadura += armor

    def set_resistencia_magica(self, magic_res):
        self._resistencia_magica += magic_res

    def set_movimiento_plano(self, flat_movement):
        self._movimiento_plano += flat_movement

    def set_movimiento_porcentual(self, percentage_movement):
        self._movimiento_porcentual += percentage_movement

    def set_movimiento(self, flat_movement, percentage_movement):
        self._movimiento = flat_movement * (1 + (percentage_movement / 100))
        if self._movimiento > 415:
            exceso = self._movimiento - 415
            exceso = exceso * 0.8
            self._movimiento = 415 + exceso
        self._movimiento = math.ceil(self._movimiento)

    def set_poder_de_habilidad(self, ability_power):
        self._poder_de_habilidad += ability_power

    def set_impacto_critico(self, critical_impact):
        self._impacto_critico += critical_impact

    def set_daño_critico(self, daño_critico):
        self._daño_critico += daño_critico

    def set_vampirismo_fisico(self, life_steal):
        self._vampirismo_fisico += life_steal

    def set_vampirismo_magico(self, omnivamp):
        self._vampirismo_magico += omnivamp

    def set_penetracion_de_armadura_plana(self, flat_armor_pen):
        self._penetracion_de_armadura_plana += flat_armor_pen

    def set_penetracion_de_armadura_porcentual(self, percentage_armor_pen):
        self._penetracion_de_armadura_porcentual += percentage_armor_pen

    def set_penetracion_magica(self, magic_pen):
        self._penetracion_magica += magic_pen

    def set_penetracion_magica_porcentual(self, magic_pen_percentual):
        self._penetracion_magica_porcentual += magic_pen_percentual

    def set_velocidad_de_habilidades(self, ability_haste):
        self._velocidad_de_habilidades += ability_haste

    def set_tenacidad(self, tenacidad):
        self._tenacidad += tenacidad

    def set_curacion_y_escudo(self, healing_and_shield):
        self._curacion_y_escudo += healing_and_shield

    def _aplicar_fuente_de_stats(self, fuente):
        self.set_vida(fuente.get_vida())
        self.set_regeneracion_de_vida(fuente.get_regeneracion_de_vida())
        self.set_mana(fuente.get_mana())
        self.set_regeneracion_de_mana(fuente.get_regeneracion_de_mana())
        self.set_daño_de_ataque(fuente.get_daño_de_ataque())
        self.set_porcentaje_velocidad_de_ataque(fuente.get_velocidad_de_ataque())
        self.set_armadura(fuente.get_armadura())
        self.set_resistencia_magica(fuente.get_resistencia_magica())
        self.set_movimiento_plano(fuente.get_movimiento_plano())
        self.set_movimiento_porcentual(fuente.get_movimiento_porcentual())
        self.set_poder_de_habilidad(fuente.get_poder_de_habilidad())
        self.set_impacto_critico(fuente.get_impacto_critico())
        self.set_daño_critico(fuente.get_daño_critico())
        self.set_vampirismo_fisico(fuente.get_vampirismo_fisico())
        self.set_vampirismo_magico(fuente.get_vampirismo_magico())
        self.set_penetracion_de_armadura_plana(fuente.get_penetracion_de_armadura_plana())
        self.set_penetracion_de_armadura_porcentual(fuente.get_penetracion_de_armadura_porcentual())
        self.set_penetracion_magica(fuente.get_penetracion_magica())
        self.set_penetracion_magica_porcentual(fuente.get_penetracion_magica_porcentual())
        self.set_velocidad_de_habilidades(fuente.get_velocidad_de_habilidades())
        self.set_tenacidad(fuente.get_tenacidad())
        self.set_curacion_y_escudo(fuente.get_curacion_y_escudo())

    def _modo_adaptable(self):
        if self._poder_de_habilidad > self._daño_de_ataque - self._base_stats['daño_de_ataque']:
            return "AP"
        return "AD"

    def recalcular_stats(self):
        objetos_adaptables = []
        objetos_normales = []

        for obj in self._build:
            if obj.tiene_daño_adaptable():
                objetos_adaptables.append(obj)
            else:
                objetos_normales.append(obj)

        max_iteraciones = len(objetos_adaptables) + 5

        ad_final = None
        ap_final = None

        for _ in range(max_iteraciones):
            self._restore_base_stats()
            
            # Primero runas
            for runa in self._runas:
                self._aplicar_fuente_de_stats(runa)

            for obj in objetos_normales:
                self._aplicar_fuente_de_stats(obj)

            for obj in objetos_adaptables:
                self._aplicar_fuente_de_stats(obj)

            if self._modo_adaptable() == "AD":
                for obj in objetos_adaptables:
                    self.set_daño_de_ataque(obj.get_daño_adaptable_ad())
            else:
                for obj in objetos_adaptables:
                    self.set_poder_de_habilidad(obj.get_daño_adaptable_ap())

            self.set_velocidad_de_ataque()
            self.set_movimiento(self.get_movimiento_plano(), self.get_movimiento_porcentual())

            if ad_final == self._daño_de_ataque and ap_final == self._poder_de_habilidad:
                break

            ad_final = self._daño_de_ataque
            ap_final = self._poder_de_habilidad

        #Interacciones de Objetos Especiales

        for obj in objetos_normales:
            if obj.get_nombre() == 'Filo del Infinito' and self._impacto_critico > 100:
                bonus = (self._impacto_critico - 100) * 0.6
                self.set_daño_critico(bonus)

            if obj.get_nombre() == 'Sombrero Mortífero de Rabadon':
                ap_bonus = self._poder_de_habilidad * 0.2
                self.set_poder_de_habilidad(ap_bonus)        

            if obj.get_nombre() == 'Guantelete de Sterak':
                ad_adicional = self._base_stats['daño_de_ataque'] * 0.5
                self.set_daño_de_ataque(ad_adicional)                

            if obj.get_nombre() == 'Cota Sangrienta del Soberano':
                ad_adicional = self._vida - self._base_stats['vida']
                ad_adicional = ad_adicional * 0.025
                self.set_daño_de_ataque(ad_adicional)
                
            if obj.get_nombre() == 'Manamune':
                ad_adicional = self._mana * 0.015
                self.set_daño_de_ataque(ad_adicional)
                
            if obj.get_nombre() == 'Muramaná':
                ad_adicional = self._mana * 0.02
                self.set_daño_de_ataque(ad_adicional)
                
            if obj.get_nombre() == 'Báculo del Arcángel':
                ap_adicional = self._mana * 0.01
                self.set_poder_de_habilidad(ap_adicional)
                
            if obj.get_nombre() == 'Abrazo de Serafín':
                ap_adicional = self._mana * 0.03
                self.set_poder_de_habilidad(ap_adicional)
                
            if obj.get_nombre() == 'Proyector Psíquico':
                ap_adicional = self._vida - self._base_stats['vida']
                ap_adicional = ap_adicional * 0.035
                self.set_poder_de_habilidad(ap_adicional)
                
            if obj.get_nombre() == 'Llegada del Invierno':
                vida_adicional = self._mana * 0.08
                self.set_vida(vida_adicional)
            
            if obj.get_nombre() == 'Invierno Nórdico':
                vida_adicional = self._mana * 0.1
                self.set_vida(vida_adicional)
                

    def add_object(self, obj: Objeto):
        self._build.append(obj)
        self.recalcular_stats()
        
    def add_rune(self, rune):
        self._runas.append(rune)
        self.recalcular_stats()

    def use_object(self, obj: Objeto):
        self.add_object(obj)