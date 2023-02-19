pokemon_list = []

class Pokemon:
    def __init__(self, name, type, hp, attack, defense):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense

def add_pokemon():
    name = input("Enter Pokemon name: ")
    type = input("Enter Pokemon type: ")
    hp = int(input("Enter Pokemon hit points (HP): "))
    attack = int(input("Enter Pokemon attack: "))
    defense = int(input("Enter Pokemon defense: "))
    pokemon_list.append(Pokemon(name, type, hp, attack, defense))

def view_pokemon():
    for pokemon in pokemon_list:
        print("Name:", pokemon.name)
        print("Type:", pokemon.type)
        print("HP:", pokemon.hp)
        print("Attack:", pokemon.attack)
        print("Defense:", pokemon.defense)
        print("---")

while True:
    print("1. Add Pokemon")
    print("2. View Pokemon")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_pokemon()
    elif choice == 2:
        view_pokemon()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Try again.")
