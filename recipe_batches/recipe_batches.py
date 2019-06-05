#!/usr/bin/python

# Conditions
# The keys will be the ingredient names, with their associated values being the amounts
# Your function should output the maximum number of whole batches that can be made

def recipe_batches(recipe, inventory):
  leftovers = []
  # loop over the key/value pairs of the recipe dictionary
  for recipe_key, recipe_value in recipe.items():
    # divide each value by values in inventory
    try:
      leftovers.append(inventory[recipe_key] // recipe_value)
    # if this item isn't in the inventory at all, return 0
    except:
      return 0
  # if all ingredients exist in inventory, find the limiting ingredient
  return min(n for n in leftovers)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))