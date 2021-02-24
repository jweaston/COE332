#!/usr/bin/env python3
import json
import random
import sys

def breed(animal1, animal2):
    assert isinstance(animal1, dict), "Input should be dict"
    assert isinstance(animal2, dict), "Input should be dict"

    child = {}
    child["head"] = animal1["head"] + "-" + animal2["head"]
    child["body"] = animal1["body"] + "-" + animal2["body"]
    child["arms"] = round((animal1["arms"]+animal2["arms"])/4)*2
    child["legs"] = round((animal1["legs"]+animal2["legs"])/6)*3
    child["tails"] = child["arms"] + child["legs"]
    return child

def main():
    
    with open(sys.argv[1], 'r') as f:
        animals = json.load(f)

    randNum1 = random.randint(0,19)
    randNum2 = random.randint(0,19)
    randNum3 = random.randint(0,19)
    print(animals[randNum1])

    parent1 = animals[randNum2]
    parent2 = animals[randNum3]
    child = breed(parent1, parent2)

    print("Parents: \n")
    print(parent1, '\n')
    print(parent2, '\n')
    print("Child: \n")
    print(child)

if __name__ == '__main__':
    main()
