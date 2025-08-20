# Dictionary Methods

foodRecipe = {
    "name": "Musakka",
    "recipe": "recipe description",
    "image": "1.jpg"
}

# access items

result = foodRecipe["name"]
result = foodRecipe.get("name")
result = foodRecipe.keys()
result = foodRecipe.values()
result = foodRecipe.items() # giving list of tuples



# update items

# foodRecipe["name"] = "Mantı"
# foodRecipe.update({"name": "Mantı"})
# foodRecipe.update({"name2": "Mantı"})



# delete items

# foodRecipe.pop("name")
# foodRecipe.popitem() last item was removed
foodRecipe.clear()


result = foodRecipe

print(result)