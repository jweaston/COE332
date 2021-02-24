#!/usr/bin/env python3
import unittest
from read_animals import breed

class TestReadAnimals(unittest.TestCase):
    def test_breed(self):
        animal1 = {'head': 'bull', 'body': 'salmon-mantis', 'arms': 2, 'legs': 9, 'tails': 11} 
        animal2 = {'head': 'snake', 'body': 'beagle-oriole', 'arms': 10, 'legs': 9, 'tails': 19}
        child = {'head': 'bull-snake', 'body': 'salmon-mantis-beagle-oriole', 'arms': 6, 'legs': 9, 'tails': 15}
        self.assertEqual(breed(animal1, animal2),child)
        self.assertRaises(KeyError, breed,{'head':'raven','body':'lion-tiger','arms':5,'legs':6,'tail':11},
                                          {'heads':'lion'})
        self.assertRaises(KeyError, breed,{'head':'raven','body':'lion-tiger','arms':5,'legs':6,'tail':11},
                                          {'head':'lion'})
        self.assertRaises(AssertionError, breed,'lion','goat')
        self.assertRaises(AssertionError, breed,{'head':'bunny','body':'flamingo-dog','arms':3,'legs':6,'tail':9},'zebra')
        self.assertRaises(AssertionError, breed, 'str', 'str')


if __name__ == '__main__':
    unittest.main()