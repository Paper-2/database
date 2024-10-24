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


class Recipe:
    """
    class to represent a recipe.
    Attributes:
    -----------
    cui_type : str
        The type of cuisine.
    title : str
        The title of the recipe.
    ingredients : str
        The ingredients required for the recipe.
    instructions : str
        The instructions to prepare the recipe.
    """
    def __init__(self, recipe_as_list) -> None:
        self.cui_type = recipe_as_list[0]
        self.title = recipe_as_list[1]
        self.ingredients = recipe_as_list[2]
        self.instructions = recipe_as_list[3]