#!/usr/bin/env python3
import petname
import json
import random  
import sys

def main():
    heads = ["snake", "bull", "raven", "bunny"]
    animal = {}
    animals = []
    for _ in range(20):

        animal["head"] = heads[random.randint(0,3)]
        animal["body"] = petname.name() + "-" + petname.name()
        animal["arms"] = random.randint(1,5)*2
        animal["legs"] = random.randint(1,4)*3
        animal["tails"] = animal['arms'] + animal['legs']
        animals.append(animal.copy())

    with open(sys.argv[1], 'w') as out:
            json.dump(animals, out, indent=4)

if __name__ == '__main__':
    main()