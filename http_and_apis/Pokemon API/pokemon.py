from json import JSONDecodeError
import requests


class Pokemon:
    def __init__(self, name):
        try:
            self.name = name
            self.address = f"https://pokeapi.co/api/v2/pokemon/{name}/"
            self.req_response = requests.get(self.address)
            self.info = self.req_response.json()
            self.list_of_ability_names = []
            self.list_of_ability_urls = []
            self.list_of_effects = []
            self.list_of_games = []
            self.list_of_game_names = []
            self.list_of_base_stats = []
            self.list_of_base_stats_names = []
            self.list_of_type = []
            self.get_pokemon_type()
            self.append_type()
            self.get_abilities_and_effects()
            self.append_abilities_and_effects()
            self.get_games_appeared_in()
            self.append_games_appeared_in()
            self.get_base_stats()
            self.append_base_stats()
        except JSONDecodeError:
            print("This pokemon does not exist")

    def get_abilities_and_effects(self):
        for row in self.info['abilities']:
            self.list_of_ability_names.append(row['ability']['name'])
            self.list_of_ability_urls.append(row['ability']['url'])
        for url in self.list_of_ability_urls:
            get_effect = requests.get(url)
            effect = get_effect.json()['effect_entries']
            for row in effect:
                if row['language']['name'] == 'en':
                    short_effect = row['short_effect']
                    self.list_of_effects.append(short_effect)

    def get_games_appeared_in(self):
        for row in self.info['game_indices']:
            self.list_of_games.append(row['game_index'])
        for game_name in self.info['game_indices']:
            self.list_of_game_names.append(game_name['version']['name'])

    def get_base_stats(self):
        for row in self.info['stats']:
            self.list_of_base_stats.append(row['base_stat'])
        for row2 in self.info['stats']:
            self.list_of_base_stats_names.append(row2['stat']['name'])

    def get_pokemon_type(self):
        for row in self.info['types']:
            self.list_of_base_stats_names.append(row['type']['name'])

    def append_abilities_and_effects(self):
        with open(f"pokemonapi_{self.name}.txt", "a") as pokeapi:
            pokeapi.writelines("\n")
            pokeapi.writelines("\n")
            if len(self.list_of_ability_names) == 1:
                pokeapi.writelines(f"{self.name.capitalize()}'s only ability is {self.list_of_ability_names[0]},"
                                   f" and the effect {self.list_of_effects[0]}")
            elif len(self.list_of_ability_names) == 2:
                pokeapi.writelines(f"{self.name.capitalize()}'s first ability is {self.list_of_ability_names[0]},"
                                   f" and the effect {self.list_of_effects[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.name.capitalize()}'s second ability is {self.list_of_ability_names[1]},"
                                   f" and the effect {self.list_of_effects[1]}")
                pokeapi.writelines("\n")
            elif len(self.list_of_ability_names) == 3:
                pokeapi.writelines(f"{self.name.capitalize()}'s first ability is {self.list_of_ability_names[0]},"
                                   f" and the effect {self.list_of_effects[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.name.capitalize()}'s second ability is {self.list_of_ability_names[1]},"
                                   f" and the effect {self.list_of_effects[1]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.name.capitalize()}'s third ability is {self.list_of_ability_names[2]},"
                                   f" and the effect {self.list_of_effects[2]}")
                pokeapi.writelines("\n")
            elif len(self.list_of_ability_names) == 4:
                pokeapi.writelines(f"{self.name.capitalize()}'s first ability is {self.list_of_ability_names[0]},"
                                   f" and the effect {self.list_of_effects[0]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.name.capitalize()}'s second ability is {self.list_of_ability_names[1]},"
                                   f" and the effect {self.list_of_effects[1]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.name.capitalize()}'s third ability is {self.list_of_ability_names[2]},"
                                   f" and the effect {self.list_of_effects[2]}")
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.name.capitalize()}'s fourth ability is {self.list_of_ability_names[3]},"
                                   f" and the effect {self.list_of_effects[3]}")
                pokeapi.writelines("\n")

    def append_games_appeared_in(self):
        with open(f"pokemonapi_{self.name}.txt", "a") as pokeapi:
            pokeapi.writelines("\n")
            pokeapi.writelines("\n")
            pokeapi.writelines(f"{self.name.capitalize()} has appeared in {len(self.list_of_games)} games\n")
            pokeapi.writelines(f"These games are: {self.list_of_game_names}")

    def append_base_stats(self):
        with open(f"pokemonapi_{self.name}.txt", "a") as pokeapi:
            pokeapi.writelines("\n")
            pokeapi.writelines("\n")
            for x in range(len(self.list_of_base_stats_names)):
                pokeapi.writelines("\n")
                pokeapi.writelines(f"{self.list_of_base_stats_names[x]} : {self.list_of_base_stats[x]}")

    def append_type(self):
        with open(f"pokemonapi_{self.name}.txt", "a") as pokeapi:
            pokeapi.writelines(f"{self.name.capitalize()}")
            pokeapi.writelines("\n")
            pokeapi.writelines("\n")
            pokeapi.writelines(f"{self.name.capitalize()} is a {self.list_of_type} type Pokemon")





