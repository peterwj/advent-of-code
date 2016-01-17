#!/usr/bin/python

import random
from sys import argv as argv
import unittest

class TestDay15(unittest.TestCase):
    def test_basic_case(self):
        butterscoth = Ingredient('Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8')
        cinnamon = Ingredient('Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3')
        recipe = Recipe(
                ingredients={butterscoth: 44, cinnamon: 56},
                ignored_attributes=['calories'],
        )
        assert(recipe.score == 62842880)

class Ingredient():
    def __init__(self, line):
        line = line.split(' ')
        self._attributes = {}
        self._name = line[0]
        line = line[1:]
        assert(len(line) % 2 == 0)
        for i in range(0, len(line), 2):
            self._attributes[line[i]] = int(line[i+1].replace(',', ''))

    @property
    def attributes(self):
        return self._attributes

    @property
    def name(self):
        return self._name

class Recipe():
    def __init__(self, ingredients, ignored_attributes=[]):
        """Pass in a mapping of ingredient to quantity in ingredients."""
        self.recipe_attributes = {}
        self.ignored_attributes = ignored_attributes
        for ingredient, quantity in ingredients.items():
            for attribute, effect in ingredient.attributes.items():
                if attribute not in self.recipe_attributes:
                    self.recipe_attributes[attribute] = 0
                self.recipe_attributes[attribute] += quantity * effect

    @property
    def score(self):
        score = 1
        for attribute, effect in self.recipe_attributes.items():
            if attribute in self.ignored_attributes:
                continue
            score *= effect if effect > 0 else 0
        return score

    def get_attribute(self, attribute):
        return self.recipe_attributes[attribute]

def read_ingredient_file(ingredient_file):
    ingredients = []
    with open(ingredient_file) as f:
        ingredients = [Ingredient(line) for line in f]
    return ingredients


def optimize_recipe(ingredient_file, calorie_value=None):
    best_score = 0
    ingredients = read_ingredient_file(ingredient_file)
    while True:
        quantities = [random.randint(0,100) for i in range(len(ingredients)-1)]
        quantities.append(100 - sum(quantities))
        if any([x < 0 for x in quantities]):
            continue
        ingredients = zip(ingredients, quantities)
        ingredients = {k:v for (k,v) in ingredients}
        recipe = Recipe(ingredients, ['calories'])
        if calorie_value and recipe.get_attribute('calories') != calorie_value:
            continue
        score = recipe.score
        if score > best_score:
            best_score = score
            print(best_score)

if __name__ == '__main__':
    if len(argv) == 2:
        optimize_recipe(argv[1], calorie_value=500)
    else:
        unittest.main()
