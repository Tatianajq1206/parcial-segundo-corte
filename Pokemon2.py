class Attack:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

class Pokemon:
    def __init__(self, name, health, attacks):
        self.name = name
        self.health = health
        self.attacks = attacks

#Lista de Pokemones con los ataques  que pueden ser utilizados por cada uno
pokemons = [
    Pokemon("Pikachu", 100, [
        Attack("Impactrueno", 50),
        Attack("Rayo", 70),
        Attack("Ataque Rápido", 30),
        Attack("Placaje", 40)
    ]),
    Pokemon("Caterpie", 100, [
        Attack("Placaje", 40),
        Attack("Tacleada", 50),
        Attack("Supersónico", 60),
        Attack("Drenadoras", 30)
    ]),
    Pokemon("Pidgeotto", 100, [
        Attack("Picotazo", 30),
        Attack("Remolino", 40),
        Attack("Tornado", 60),
        Attack("Ataque Rápido", 30)
    ]),
    Pokemon("Bulbasaur", 100, [
        Attack("Látigo Cepa", 40),
        Attack("Drenadoras", 30),
        Attack("Placaje", 40),
        Attack("Somnífero", 50)
    ]),
    Pokemon("Charmander", 100, [
        Attack("Lanzallamas", 60),
        Attack("Gruñido", 20),
        Attack("Arañazo", 30),
        Attack("Ascuas", 40)
    ]),
    Pokemon("Squirtle", 100, [
        Attack("Pistola Agua", 50),
        Attack("Burbuja", 30),
        Attack("Ataque Rápido", 30),
        Attack("Placaje", 40)
    ]),
    Pokemon("Krabby", 100, [
        Attack("Burbuja", 30),
        Attack("Rayo Burbuja", 40),
        Attack("Placaje", 40),
        Attack("Tajo Cruzado", 50)
    ]),
    Pokemon("Raticate", 100, [
        Attack("Hipercolmillo", 60),
        Attack("Ataque Rápido", 30),
        Attack("Placaje", 40),
        Attack("Golpe Cabeza", 50)
    ]),
    Pokemon("Muk", 100, [
        Attack("Lodo", 50),
        Attack("Bomba Lodo", 70),
        Attack("Ataque Ácido", 60),
        Attack("Infortunio", 40)
    ]),
    Pokemon("Kingler", 100, [
        Attack("Hidropulso", 70),
        Attack("Rayo Burbuja", 40),
        Attack("Rayo", 60),
        Attack("Placaje", 40)
    ])
]

# Muesta la lista de pokemones disponibles
def display_available_pokemons(selected_pokemons):
    available_pokemons = [pokemon for pokemon in pokemons if pokemon not in selected_pokemons]
    print("\nPersonajes disponibles:")
    for index, pokemon in enumerate(available_pokemons, start=1):
        print(f"{index}. {pokemon.name}")

#Muesta la lista de pokemones
def display_pokemons():
    for index, pokemon in enumerate(pokemons, start=1):
        print(f"{index}. {pokemon.name}")

def display_pokemons_detailed():
    for index, pokemon in enumerate(pokemons, start=1):
        print(f"{index}. {pokemon.name} (Health: {pokemon.health})")
        for attack_index, attack in enumerate(pokemon.attacks, start=1):
            print(f"{attack_index}. {attack.name} (Damage: {attack.damage})")

# Esta funcion  permite al usuario elegir los tres pokemones 
def select_pokemons():
    player_team = []
    print("\nSelecciona 3 pokemones de la siguiente lista:")
    display_pokemons_detailed()

    for i in range(1, 4):
        while True:
            try:
                choice = input(f"Jugador 1 elija su equipo de Pokémones ({i}/3): ")
                if choice.isdigit() and int(choice) in range(1, len(pokemons) + 1):
                    chosen_pokemon = pokemons[int(choice) - 1]
                    if chosen_pokemon not in player_team:
                        player_team.append(chosen_pokemon)
                        break
                    else:
                        print(f"{chosen_pokemon.name} is already in your team.")
                elif len(choice) == 1 and choice.lower() in [p.lower() for p in [p.name for p in pokemons]]:
                    chosen_pokemon = next(filter(lambda x: x.name.lower() == choice.lower(), pokemons))
                    if chosen_pokemon not in player_team:
                        player_team.append(chosen_pokemon)
                        break
                    else:
                        print(f"{chosen_pokemon.name} is already in your team.")
                else:
                    print("Selección inválida. Inténtalo de nuevo.")
            except ValueError:
                print("Entrada inválida. Inténtalo de nuevo.")

    return player_team

# Esta funcion  muestra el equipo contrario
def display_opponent_team(opponent_team):
    print("\nLos personajes que conforman al equipo contrario son: ")
    for index, pokemon in enumerate(opponent_team, start=1):
        print(f"{index}. {pokemon.name}")

# Le permite al grupo oponente elegir los personajes de su equipo
def opponent_select_pokemons(player_team):
    opponent_team = []

    available_pokemons = [p for p in pokemons if p not in player_team]

    display_available_pokemons(available_pokemons)

    for i in range(1, 4):
        while True:
            try:
                choice = input(f"Jugador 2 elija su equipo de Pokémones ({i}/3): ")
                if choice.isdigit() and int(choice) in range(1, len(available_pokemons) + 1):
                    pokemon = available_pokemons[int(choice) - 1]
                    opponent_team.append(pokemon)
                    break
                elif len(choice) == 1 and choice.lower() in [p.lower() for p in [p.name for p in available_pokemons]]:
                    pokemon = next(filter(lambda x: x.name.lower()== choice.lower(), available_pokemons))
                    opponent_team.append(pokemon)
                    break
                #aca
            except ValueError:
                print("Entrada inválida. Inténtalo de nuevo.")

    return opponent_team
# Muestra los ataques de un pokemon 
def display_pokemon_attacks(pokemon):
    print(f"\n{pokemon.name} Attacks:")
    for index, attack in enumerate(pokemon.attacks, start=1):
        print(f"{index}. {attack.name} (Damage: {attack.damage})")

def display_team_attacks(team):
    for index, pokemon in enumerate(team, start=1):
        print(f"\n{index}. {pokemon.name} (Health: {pokemon.health})")
        for attack_index, attack in enumerate(pokemon.attacks, start=1):
            print(f"{attack_index}. {attack.name} (Damage: {attack.damage})")

# Funcion para obtener un Pokemon por su nombre
def get_pokemon_by_name(name, pokemon_list):
    return next((pokemon for pokemon in pokemon_list if pokemon.name.lower() == name.lower()), None)

# Inicia el juego 
def main():
    # Selecciona 3 pokemones para el jugador
    player_team = select_pokemons()

    # Imprime el equipo del jugador y sus ataques
    display_team_attacks(player_team)

    # Selecciona 3 pokemones para el oponente
    opponent_team = opponent_select_pokemons(player_team)

    # Imprime el equipo del oponente y sus ataques
    display_team_attacks(opponent_team)


    players = [player_team, opponent_team]
    current_player_index = 0

    # Bucle del juego
    while all(len(pokemons) > 0 for pokemons in players):
        current_player_team, other_player_team = players[current_player_index], players[1 - current_player_index]

        print(f"\n\nInicia {['Jugador 1', 'Jugador 2'][current_player_index]} / Partida {current_player_index + 1}")
        attacker_name = input("Con qué personaje quieres atacar (nombre o número): ").capitalize()

        attacker = get_pokemon_by_name(attacker_name, current_player_team)

        if attacker is None:
            print("No se encontró ningún pokémon con ese nombre. Inténtalo de nuevo.")
            continue

        defender_names = [pokemon.name for pokemon in other_player_team]
        defender_name = input(
            f"A qué personaje quieres atacar (número o nombre): ").capitalize()

        defender = get_pokemon_by_name(defender_name, other_player_team)

        if defender is None:
            print("No se encontró ningún pokémon con ese nombre. Inténtalo de nuevo.")
            continue

        if defender.health <= 0:
            print(
                f"{defender.name} has already been defeated. Choose another defender.")
            continue

        print(
            f"{attacker.name} ataca a {defender.name}!")

        while True:
            attack_index = input("Selecciona el ataque número (ingresa un número): ")
            if attack_index.strip():
                attack_index = int(attack_index)
                if 1 <= attack_index <= len(attacker.attacks):
                    defender.health -= attacker.attacks[attack_index - 1].damage
                    print(
                        f"Salud de {defender.name}: {defender.health}")

                    if defender.health <= 0:
                        print(
                            f"{defender.name} ha sido derrotado!")
                        other_player_team.remove(defender)

                    if not other_player_team:
                        print(
                            f"{['Jugador 1', 'Jugador 2'][current_player_index]} gana!")
                    break
                else:
                    print("El ataque seleccionado no es válido. Inténtalo de nuevo.")
            else:
                print("El ataque seleccionado no es válido. Inténtalo de nuevo.")

        current_player_index = 1 - current_player_index

if __name__ == "__main__":
    main()