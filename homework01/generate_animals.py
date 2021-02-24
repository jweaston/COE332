import petname
import json
import random  


heads = ["snake", "bull", "raven", "bunny"]
animal = {}
animals = []
for i in range(20):

    animal["head"] = heads[random.randint(0,3)]
    animal["body"] = petname.name() + "-" + petname.name()
    animal["arms"] = random.randint(1,5)*2
    animal["legs"] = random.randint(1,4)*3
    animal["tails"] = animal['arms'] + animal['legs']
    animals.append(animal.copy())

with open('./animals.json', 'w') as out:
        json.dump(animals, out, indent=4)