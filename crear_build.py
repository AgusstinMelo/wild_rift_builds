import json
import readline
from campeon import Campeon
from objeto import Objeto


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