from lib.recipe import *
from lib.recipe_repository import *
"""
When #all called on repository instance
returns all objects listed in an array
"""
def test_all_method_returns_all_objects(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repo = RecipeRepository(db_connection)
    recipes = repo.all()
    assert recipes == [
        Recipe(id=1, name='Taiwanese Beef Noodle Soup', cooking_time_in_mins=120, rating=5),
        Recipe(id=2, name='Char Siu Bao', cooking_time_in_mins=25, rating=5),
        Recipe(id=3, name='Black Pepper Chicken', cooking_time_in_mins=10, rating=4),
        Recipe(id=4, name='Raw Garlic Salad', cooking_time_in_mins=5, rating=2),
        Recipe(id=5, name='Lemon Chicken', cooking_time_in_mins=20, rating=4)
    ]

"""
When #find with id arg called on repository instane
returns object with matching id
"""
def test_find_method_returns_matching_object(db_connection):
    db_connection.seed('seeds/recipes.sql')
    repo = RecipeRepository(db_connection)
    matching_recipe = repo.find(1)
    assert matching_recipe == Recipe(id=1, name='Taiwanese Beef Noodle Soup', cooking_time_in_mins=120, rating=5)
