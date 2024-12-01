import sqlite3
import os
import json

class Database:
    
    def __init__(self) -> None:  #TODO: UPDATE METHOD
        os.remove('recipes_data.db')
        self.connection = sqlite3.connect('recipes_data.db')
        
        self.cursor = self.connection.cursor()

        self.__create_table()

    def __create_table(self):  #TODO: UPDATE METHOD
        
        json_files = get_all_jsons()
        
        self.cursor.execute("""--sql -- the --sql is part of a vscode extension that allows me to color sql code in the python file and -- is a comment in sql
            CREATE TABLE IF NOT EXISTS Cuisines
            (
                name TEXT PRIMARY KEY, -- the name of the recipe which must be unique
                description TEXT,
                recipeCuisine TEXT,
                totalTime TEXT,
                cookTime TEXT,
                calories TEXT,
                carbohydrateContent TEXT,
                cholesterolContent TEXT,
                fiberContent TEXT,
                proteinContent TEXT,
                saturatedFatContent TEXT,
                sodiumContent TEXT,
                sugarContent TEXT,
                fatContent TEXT,
                unsaturatedFatContent TEXT,
                prepTime TEXT,
                recipeCategory TEXT,
                recipeIngredient TEXT,
                recipeInstructions TEXT,
                recipeYield INTEGER,
                is_favorite INTEGER
            )
            """)
        
        for json_file in json_files:
            with open(json_file, 'r') as f:
                data = json.load(f)
                nutrition = json.dumps(data.get('nutrition', {}))
                recipeCuisine = json.dumps(data.get('recipeCuisine', []))
                recipeIngredient = json.dumps(data.get('recipeIngredient', []))
                
                try:
                    # Extract nutrition information
                    nutrition_data = data.get('nutrition', {})
                    calories = nutrition_data.get('calories', '')
                    carbohydrateContent = nutrition_data.get('carbohydrateContent', '')
                    cholesterolContent = nutrition_data.get('cholesterolContent', '')
                    fiberContent = nutrition_data.get('fiberContent', '')
                    proteinContent = nutrition_data.get('proteinContent', '')
                    saturatedFatContent = nutrition_data.get('saturatedFatContent', '')
                    sodiumContent = nutrition_data.get('sodiumContent', '')
                    sugarContent = nutrition_data.get('sugarContent', '')
                    fatContent = nutrition_data.get('fatContent', '')
                    unsaturatedFatContent = nutrition_data.get('unsaturatedFatContent', '')
                    
                    
                    recipeCategory = json.dumps(data.get('recipeCategory', [])[0])
                    
                    
                    recipeInstructions = list_to_long_string(data.get('recipeInstructions', []))
                    
                    
                    recipeYield = data.get('recipeYield', 0)[0]
                    
                    # Set is_favorite default value to 0
                    is_favorite = 0
                    
                    self.cursor.execute("""--sql
                        INSERT OR REPLACE INTO Cuisines 
                        (name, description, recipeCuisine, totalTime, cookTime, 
                         calories, carbohydrateContent, cholesterolContent, fiberContent, proteinContent,
                         saturatedFatContent, sodiumContent, sugarContent, fatContent, unsaturatedFatContent,
                         prepTime, recipeCategory, recipeIngredient, recipeInstructions, recipeYield, is_favorite)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        data.get('name', ''),
                        data.get('description', ''),
                        recipeCuisine,
                        data.get('totalTime', ''),
                        data.get('cookTime', ''),
                        calories,
                        carbohydrateContent,
                        cholesterolContent,
                        fiberContent,
                        proteinContent,
                        saturatedFatContent,
                        sodiumContent,
                        sugarContent,
                        fatContent,
                        unsaturatedFatContent,
                        data.get('prepTime', ''),
                        recipeCategory,
                        recipeIngredient,
                        recipeInstructions,
                        recipeYield,
                        is_favorite
                    ))
                except sqlite3.Error as e:
                    print(f"Error inserting {json_file}: {e}")
                    continue
                except sqlite3.Error as e:
                    print(f"Error inserting {json_file}: {e}")
                    continue
            break # remove this line to insert all recipes into the database

    def get_all_recipes(self):  #TODO: UPDATE METHOD
        """
        Retrieves all recipes from the Cuisines table in the database.
        Returns:
            list: A list of tuples, where each tuple represents a row in the Cuisines table.
        """
        
        self.cursor.execute("SELECT * FROM Cuisines")
        return self.cursor.fetchall()
    
    def isfavorite(self, name):  #TODO: UPDATE METHOD
        """
        Retrieves the favorite status of a recipe from the database.

        Args:
            name (str): The name of the recipe to check.

        Returns:
            bool: True if the recipe is marked as favorite, False otherwise.
        """
        self.cursor.execute("SELECT is_favorite FROM Cuisines WHERE name = ?", (name,))
        
        result = self.cursor.fetchone()
        
        return bool(result[0])

    def set_favorite_status(self, recipe_name, status: int):  #TODO: UPDATE METHOD
        """
        Updates the favorite status of a recipe in the database.

        Args:
            recipe_name (str): The name of the recipe to update.
            status (int): The new favorite status (e.g., 1 for favorite, 0 for not favorite).

        Returns:
            None
        """
        self.cursor.execute("UPDATE Cuisines SET is_favorite = ? WHERE name = ?", (status, recipe_name))
        self.cursor.connection.commit()

    def __close(self):
        self.cursor.close()
        self.connection.close()



    def get_favorite_recipes(self):  #TODO: UPDATE METHOD
        """
        Fetches and returns a list of favorite recipes from the Cuisines table.
        """
        
        self.cursor.execute("SELECT name, ingredients_list, link FROM Cuisines WHERE is_favorite = 1")
        results = self.cursor.fetchall()
        return [(name, ingredients_list, link) for name, ingredients_list, link in results]

    def search_recipes(self, recipe_name, ingredients="", cuisine_selected=""):  #TODO: UPDATE METHOD
        """
        Searches for recipes in the database based on the given criteria.
        Args:
            recipe_name (str): The name of the recipe to search for.
            ingredients (str, optional): A string of ingredients to filter the recipes. Defaults to an empty string.
            cuisine_selected (str, optional): The type of cuisine to filter the recipes. Defaults to an empty string.
            If 'All' is provided, it will be treated as an empty string.
        Returns:
            list[tuple]: A list of tuples where each tuple contains the cuisine type, recipe name, ingredients list, and link.
            """
        if cuisine_selected == 'All':
            cuisine_selected == ""
        query = """
        SELECT name, ingredients_list, link 
        FROM Cuisines 
        WHERE name LIKE ? AND ingredients_list LIKE ? AND cui_type LIKE ?
        """

        self.cursor.execute(query, (f'%{recipe_name}%', f'%{ingredients}%', f'%{cuisine_selected}%'))
        results = self.cursor.fetchall()

        return [("cui_type", name, ingredients_list, link) for  name, ingredients_list, link in results]

def get_all_jsons():
    """
    Retrieves all JSON files in the data directory and its subdirectories.
    Returns:
        list: A list of JSON file paths.
    """
    path = r"recipes"
    json_files = []
    
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('.json'):
                json_files.append(os.path.join(dirpath, filename))
    
    return json_files

def list_to_long_string(data):
    """
    Converts a list too a line separated string. Meant to be used for instructions.
    Args:
        data (dict): The dictionary to convert.
    Returns:
        str: The long string representation of the nested dictionary.
    """
    result = ""
    counter = 1
    for json_object in data:

        result += f"Step {counter}: {json_object["text"]}\n"
        counter += 1
    return result
    
if __name__ == "__main__":
    data = Database()
    print(data.get_all_recipes())
    print(data.isfavorite("African Sweet Potato Stew"))