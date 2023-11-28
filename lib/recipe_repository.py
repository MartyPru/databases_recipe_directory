from lib.recipe import *

class RecipeRepository():
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * FROM recipes;')
        recipes = []
        for row in rows:
            recipe = Recipe(row['id'], row['name'], row['cooking_time_in_mins'], row['rating'])
            recipes.append(recipe)
        return recipes
    
    def find(self, id):
        match = self.connection.execute('SELECT * FROM recipes WHERE id = %s', [id])[0]
        matching_recipe = Recipe(match['id'], match['name'], match['cooking_time_in_mins'], match['rating'])
        return matching_recipe