#!/usr/bin/env python3

import random

# List of animals with three-letter names
animals = ["Fox", "Ant", "Bee", "Cod", "Dog", "Cat", "Yak", "Cow", "Hen", "Koi", "Hog", "Jay", "Kit"]

# Randomly select 5 animals from the list
random_animals = random.sample(animals, 5)

# Print the list of randomly selected animals
print("Five randomly selected animals with three-letter names:")
for animal in random_animals:
    print(animal)

