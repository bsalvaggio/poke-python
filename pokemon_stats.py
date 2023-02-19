# Define a list to store Pokemon objects
pokemon_list = []

# Define a Pokemon class to represent a Pokemon object
class Pokemon:
    def __init__(self, name, type, hp, attack, defense):
        self.name = name
        self.type = type
        self.hp = hp
        self.attack = attack
        self.defense = defense

# Define a function to add a new Pokemon to the list
def add_pokemon():
    name = input("Enter Pokemon name: ")
    type = input("Enter Pokemon type: ")
    hp = int(input("Enter Pokemon hit points (HP): "))
    attack = int(input("Enter Pokemon attack: "))
    defense = int(input("Enter Pokemon defense: "))
    # Create a new Pokemon object with the entered data and add it to the list
    pokemon_list.append(Pokemon(name, type, hp, attack, defense))

# Define a function to display the stats of all Pokemon in the list
def view_pokemon():
    for pokemon in pokemon_list:
        # Print the name, type, and stats of the current Pokemon object
        print("Name:", pokemon.name)
        print("Type:", pokemon.type)
        print("HP:", pokemon.hp)
        print("Attack:", pokemon.attack)
        print("Defense:", pokemon.defense)
        print("---")

# Display a menu to the user and prompt for input until the user chooses to exit
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
