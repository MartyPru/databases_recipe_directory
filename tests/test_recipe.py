from lib.recipe import *

"""
When initialised with values
Stores values correctly
"""
def test_init():
    recipe = Recipe(1, 'Pasta Carbonara', 15, 4)
    assert recipe.name == 'Pasta Carbonara'
    assert recipe.cooking_time_in_mins == 15
    assert recipe.rating == 4

"""
When two instances of Recipe have same values
They are equal
"""
def test_equality():
    recipe_1 = Recipe(1, 'Pasta Carbonara', 15, 4)
    recipe_2 = Recipe(1, 'Pasta Carbonara', 15, 4)
    assert recipe_1 == recipe_2

"""
When Recipe instance formatted as string
Prints as easy-to-read string
"""
def test_str_formatting():
    recipe = Recipe(1, 'Pasta Carbonara', 15, 4)
    assert str(recipe) == "Recipe(id=1, name='Pasta Carbonara', cooking_time_in_mins=15, rating=4)"
