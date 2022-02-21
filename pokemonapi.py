from pip._vendor import requests

pokedex= []
class Pokemon:
    def __init__(self, name, height, weight, ability1, ability2):
        self.name = name
        self.height = height
        self.weight = weight
        self.ability1 = ability1
        self.ability2 = ability2
    def __repr__(self):
        return f'<Pokemon: {self.name}, {self.height} ft, {self.weight} lbs, {self.ability1}, {self.ability2}>'

def pick_poke():
    poke_choice = input("Choose your Pokemon. ")
    api_link = f"https://pokeapi.co/api/v2/pokemon/{poke_choice}/"
    poke_name =  requests.get(api_link).json()['name'].title()
    poke_height = requests.get(api_link).json()['height']
    poke_weight = requests.get(api_link).json()['weight']
    poke_ability1 = requests.get(api_link).json()["abilities"][0]["ability"]["name"].title()
    poke_ability2 = requests.get(api_link).json()["abilities"][1]["ability"]["name"].title()

    poke = Pokemon(
        name = poke_name,
        height = poke_height,
        weight = poke_weight,
        ability1 = poke_ability1,
        ability2 = poke_ability2
        )
    
    pokedex.append(poke)
    print("\nYour Current Pokedex: ")
    print(pokedex)


dex = True
while dex:
    print("\nWelcome to the Pokemon Center, I'm sure you had a day filled with battling and catching Pokemon! Lets add your new Pokemon to the Pokedex!\n")
    flag = True
    while flag:
        pick_poke()
        while True:
            more = input("\nWould you like to add another Pokemon to your Pokedex? (Y/N) ").lower()
            if more == 'y':
                break
            elif more == 'n':
                print("\nThanks for stopping by! Go catch 'em all!")
                dex = False
                flag = False
                break
            else:
                print("Please enter a valid response. ")


    






 