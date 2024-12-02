class Recipe:
    """
    A class to represent a recipe.
    Attributes
    ----------
    all_data : dict
        The original dictionary containing all recipe data.
    name : str
        The name of the recipe.
    description : str
        A description of the recipe.
    recipeCuisine : str
        The cuisine type of the recipe.
    totalTime : str
        The total time required to prepare the recipe.
    cookTime : str
        The cooking time duration.
    calories : str
        The number of calories in the recipe.
    carbohydrateContent : str
        The amount of carbohydrates in the recipe.
    cholesterolContent : str
        The amount of cholesterol in the recipe.
    fiberContent : str
        The amount of dietary fiber in the recipe.
    proteinContent : str
        The amount of protein in the recipe.
    saturatedFatContent : str
        The amount of saturated fat in the recipe.
    sodiumContent : str
        The amount of sodium in the recipe.
    sugarContent : str
        The amount of sugar in the recipe.
    fatContent : str
        The total amount of fat in the recipe.
    unsaturatedFatContent : str
        The amount of unsaturated fat in the recipe.
    prepTime : str
        The preparation time duration.
    recipeCategory : str
        The category or type of the recipe.
    recipeIngredient : list
        A list of ingredients required for the recipe.
    recipeInstructions : list
        A list of instructions to prepare the recipe.
    recipeYield : str
        The quantity produced by the recipe (e.g., number of servings).
    Parameters
    ----------
    recipe_as_dict : dict
        A dictionary containing all the recipe data.
    """
    def __init__(self, recipe_as_dict) -> None:
        self.all_data = recipe_as_dict
        
        self.name = recipe_as_dict['name']
        self.description = recipe_as_dict['description']
        self.recipeCuisine = recipe_as_dict['recipeCuisine']
        self.totalTime = recipe_as_dict['totalTime']
        self.cookTime = recipe_as_dict['cookTime']
        self.calories = recipe_as_dict['calories']
        self.carbohydrateContent = recipe_as_dict['carbohydrateContent']
        self.cholesterolContent = recipe_as_dict['cholesterolContent']
        self.fiberContent = recipe_as_dict['fiberContent']
        self.proteinContent = recipe_as_dict['proteinContent']
        self.saturatedFatContent = recipe_as_dict['saturatedFatContent']
        self.sodiumContent = recipe_as_dict['sodiumContent']
        self.sugarContent = recipe_as_dict['sugarContent']
        self.fatContent = recipe_as_dict['fatContent']
        self.unsaturatedFatContent = recipe_as_dict['unsaturatedFatContent']
        self.prepTime = recipe_as_dict['prepTime']
        self.recipeCategory = recipe_as_dict['recipeCategory']
        self.recipeIngredient = recipe_as_dict['recipeIngredient']
        self.recipeInstructions = recipe_as_dict['recipeInstructions']
        self.recipeYield = recipe_as_dict['recipeYield']
