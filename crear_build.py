import json
from campeon import Campeon
from objeto import Objeto

def cargar_json(ruta):
    """Carga el archivo JSON y devuelve un diccionario."""
    with open(ruta, "r", encoding="utf-8") as f:
        return json.load(f)

def elegir_campeon(data):
    """Permite elegir un campeón por nombre."""
    campeones = list(data.keys())

    print("=== Lista de campeones ===")
    for i, nombre in enumerate(campeones, start=1):
        print(f"{i}. {nombre}")

    print("\nElegí un campeón por nombre:")
    opcion = input("> ").strip()

    # Si elige nombre exacto
    opcion = opcion.title().replace(' ', '-')
    if opcion in data.keys():
        return data[opcion]

    print("No se encontró el campeón.")
    return None

def elegir_objeto(data):
    """Permite elegir un objeto."""
    objetos = list(data.keys())

    print("=== Lista de objetos ===")
    for i, nombre in enumerate(objetos, start=1):
        print(f"{i}. {nombre}")

    print("\nElegí un objeto:")
    opcion = input("> ").strip()

    # Si elige nombre exacto
    opcion = opcion.title().replace(' ', '-')
    if opcion in data.keys():
        return data[opcion]

    print("No se encontró el campeón.")
    return None


def main():
    data_champ = cargar_json("data_name_hero.json")

    campeon = elegir_campeon(data_champ)
    if campeon:
        campeon_elegido = Campeon(campeon)
        campeon_elegido.print_stats()
    data_object = cargar_json("objects.json")
    objeto = elegir_objeto(data_object)
    if objeto:
        objeto_elegido = Objeto(objeto)
        print(objeto_elegido.get_nombre())
        campeon_elegido.use_object(objeto_elegido)
        campeon_elegido.print_stats()

if __name__ == "__main__":
    main()
