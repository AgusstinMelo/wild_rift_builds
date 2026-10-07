import json
import readline
from campeon import Campeon
from objeto import Objeto
from runa import Runa


def autocompletar(options):
    def completer(text, state):
        text_lower = text.lower()

        matches = [
            o for o in options
            if any(word.lower().startswith(text_lower) for word in o.split()) or o.lower().startswith(text_lower)
        ]

        if state < len(matches):
            return matches[state]
        return None

    return completer


def cargar_json(ruta):
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)


def elegir_campeon(data):
    campeones = [value['name'] for value in data.values()]

    readline.set_completer_delims('')
    readline.set_completer(autocompletar(campeones))
    readline.parse_and_bind("tab: complete")
    readline.parse_and_bind("set show-all-if-ambiguous off")

    print("=== Lista de campeones ===")
    for i, nombre in enumerate(campeones, start=1):
        print(f"{i}. {nombre}")

    print("\nElegí un campeón por nombre:")
    opcion = input("> ").strip()

    if opcion.lower() in ["quit", "exit", "salir", "q"]:
        print("Saliendo del programa...")
        exit()

    opcion = opcion.title().replace(' ', '-')
    if opcion in data.keys():
        return data[opcion]

    print("No se encontró el campeón.")
    return None

def filtrar_runas(data, tipo=None, tier=None):
    runas_filtradas = []

    for key, value in data.items():
        tags = value.get("type", [])

        # Runas clave
        if tipo is not None:
            if tipo not in tags:
                continue

        # Tier
        if tier is not None:
            if len(tags) < 2 or tags[1] != str(tier):
                continue

        runas_filtradas.append(value["name"])

    return runas_filtradas

def elegir_runa(runas, data, tipo=None, tier=None):
    if tipo is not None or tier is not None:
        runas_filtradas = filtrar_runas(
            data,
            tipo=tipo,
            tier=tier
        )
    else:
        runas_filtradas = runas

    readline.set_completer(autocompletar(runas_filtradas))
    readline.parse_and_bind("tab: complete")

    if tipo == "Clave":
        print("=== Lista de runas claves ===")
    else:
        print(f"=== Lista de runas de {tipo} ===")
        
    for i, nombre in enumerate(runas_filtradas, start=1):
        print(f"{i}. {nombre}")

    if tipo == "Clave":
        print("\nElegí la runa clave:")
    else:
        print("\nElegí una runa:")
            
    opcion = input("> ").strip()
    if opcion.lower() in ["quit", "exit", "salir", "q"]:
        print("Saliendo del programa...")
        exit()

    replacements = str.maketrans({
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        " ": "-"
    })

    opcion = opcion.title().translate(replacements)

    # Validar SOLO contra las runas filtradas
    runas_validas_keys = []

    for key, value in data.items():
        if value["name"] in runas_filtradas:
            runas_validas_keys.append(key)

    if opcion in runas_validas_keys:
        return data[opcion]
    elif opcion in data.keys():
        print(f"No podés elegir esa runa para este tipo/tier.")
    else:
        print("No se encontró la runa.")
    return None

def elegir_rama(excluir=None):
    es_secundaria = excluir is not None
    
    if excluir is None:
        excluir = []

    ramas = ["Precisión", "Dominación", "Valor", "Inspiración"]

    ramas_disponibles = [
        rama for rama in ramas
        if rama not in excluir
    ]

    readline.set_completer(autocompletar(ramas_disponibles))
    readline.parse_and_bind("tab: complete")

    print("=== Ramas disponibles ===")
    for i, rama in enumerate(ramas_disponibles, start=1):
        print(f"{i}. {rama}")

    if not es_secundaria:
        print("\nElegí una rama principal:")
        opcion = input("> ").strip()
    else:
        print("\nElegí una rama secundaria:")
        opcion = input("> ").strip()

    if opcion.lower() in ["quit", "exit", "salir", "q"]:
        print("Saliendo del programa...")
        exit()

    opcion = opcion.title()

    if opcion in ramas_disponibles:
        return opcion

    print("No se encontró la rama o no está disponible.")
    return None

def elegir_objeto(data):
    objetos = [value['name'] for value in data.values()]

    readline.set_completer(autocompletar(objetos))
    readline.parse_and_bind("tab: complete")

    print("=== Lista de objetos ===")
    for i, nombre in enumerate(objetos, start=1):
        print(f"{i}. {nombre}")

    print("\nElegí un objeto:")
    opcion = input("> ").strip()

    if opcion.lower() in ["quit", "exit", "salir", "q"]:
        print("Saliendo del programa...")
        exit()

    replacements = str.maketrans({
        "á": "a",
        "é": "e",
        "í": "i",
        "ó": "o",
        "ú": "u",
        " ": "-"
    })
    opcion = opcion.title().translate(replacements)

    if opcion in data.keys():
        return data[opcion]

    print("No se encontró el objeto.")
    return None


def main():
    data_champ = cargar_json("data_name_hero.json")
    campeon = None

    while not campeon:
        campeon = elegir_campeon(data_champ)

    campeon_elegido = Campeon(campeon)
    campeon_elegido.print_stats()


    #  Runas
    runas = []
    data_runes = cargar_json("runes.json")
    parse_runas = [value["name"] for value in data_runes.values()]

    # 1. Runa clave
    runa = None
    while not runa:
        runa = elegir_runa(
            parse_runas,
            data_runes,
            tipo="Clave"
        )

    runa_elegida = Runa(runa)

    print(f'\n{runa_elegida.get_nombre()}:')
    runa_elegida.print_stats()
    print(f' {runa_elegida.get_descripcion()}')

    runas.append(runa_elegida.get_nombre())
    print(f'\n{campeon_elegido.get_nombre()} runas: {runas}')

    campeon_elegido.add_rune(runa_elegida)
    campeon_elegido.print_stats()

    # 2. Rama principal
    rama_principal = None
    while not rama_principal:
        rama_principal = elegir_rama()

    print(f"\nRama principal elegida: {rama_principal}")

    # 3. Tres runas de la rama principal: tier 1, 2 y 3
    for tier in range(1, 4):
        runa = None

        while not runa:
            runa = elegir_runa(
                parse_runas,
                data_runes,
                tipo=rama_principal,
                tier=tier
            )

        runa_elegida = Runa(runa)

        print(f'\n{runa_elegida.get_nombre()}:')
        runa_elegida.print_stats()
        print(f' {runa_elegida.get_descripcion()}')

        runas.append(runa_elegida.get_nombre())
        print(f'\n{campeon_elegido.get_nombre()} runas: {runas}')

        campeon_elegido.add_rune(runa_elegida)
        campeon_elegido.print_stats()
        
    # 2. Rama secundaria
    rama_secundaria = None
    while not rama_secundaria:
        rama_secundaria = elegir_rama(excluir=[rama_principal])

    print(f"\nRama secundaria elegida: {rama_secundaria}")

    # 3. Tres runas de la rama principal: tier 1, 2 y 3
    runa = None

    while not runa:
        runa = elegir_runa(
            parse_runas,
            data_runes,
            tipo=rama_secundaria,
        )

    runa_elegida = Runa(runa)

    print(f'\n{runa_elegida.get_nombre()}:')
    runa_elegida.print_stats()
    print(f' {runa_elegida.get_descripcion()}')

    runas.append(runa_elegida.get_nombre())
    print(f'\n{campeon_elegido.get_nombre()} runas: {runas}')

    campeon_elegido.add_rune(runa_elegida)
    campeon_elegido.print_stats()

    # Objetos
    build = []
    data_object = cargar_json("objects.json")

    for i in range(6):
        objeto = None

        while not objeto:
            objeto = elegir_objeto(data_object)

        objeto_elegido = Objeto(objeto)

        print(f'\n{objeto_elegido.get_nombre()}:')
        objeto_elegido.print_stats()
        print(f' {objeto_elegido.get_descripcion()}')

        build.append(objeto_elegido.get_nombre())
        print(f'\n{campeon_elegido.get_nombre()} build: {build}')

        campeon_elegido.add_object(objeto_elegido)
        campeon_elegido.print_stats()


if __name__ == "__main__":
    main()