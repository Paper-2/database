#May help keep it for now.
def get_recipe_info(self):

    recipe_parts = []

    while len(self.recipe) > 6:
        index = self.recipe.find("---")

        if index == -1:
            recipe_parts.append(self.recipe)

            break

        recipe_parts.append(self.recipe[: index - 1])

        self.recipe = self.recipe[index + 4 :]

    return recipe_parts
