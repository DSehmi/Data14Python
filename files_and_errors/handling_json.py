import json
from pprint import pprint

with open("films.json", "r") as jsonfile:
    film = json.load(jsonfile)

pprint(film)  # pprint orders alphabetically
print(type(film))
print(film['Starring'])
print(film['Ratings']['Rotten_Tomatoes'])

film = {
    "name": "The Godfather",
    "length": 178,
    "release_year": 1972,
    "cast": {
        "Marlon Brando": "Vito",
        "Al Pachino": "Michael"
    }
}

print(film)
print(json.dumps(film))  # converts a dictionary into a string

with open("godfather.json", "w") as jsonfile:
    json.dump(film, jsonfile)  # takes a dictionary, sticks it in an open file

# Define a class
# Store same attributes as defined in jason
# Read your json file
# Create an instance of the film class for your film
