import json

# Method 1


class Film:

    def __init__(self, name, year, starring, length):
        self.Name = name
        self.Year = year
        self.Starring = starring
        self.Length = length


with open("films.json", "r") as jsonfile:
    film_dict = json.load(jsonfile)


last_samurai = Film(film_dict['Name'],
                    film_dict['Year'],
                    film_dict['Starring'],
                    film_dict['Length'])

print(last_samurai.Name, last_samurai.Year, last_samurai.Starring, last_samurai.Length)

# Method 2


