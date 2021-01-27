import json
import random

with open('animals.json', 'r') as f:
    animals = json.load(f)

randNum = random.randint(0,19)

print(animals[randNum])
