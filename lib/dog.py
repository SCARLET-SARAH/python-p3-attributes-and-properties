#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
        self.name = name
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            raise ValueError(f"{breed} is not an approved breed.")

    def __str__(self):
        return f"{self.name} is a {self.breed}"
    
