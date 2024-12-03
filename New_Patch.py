from fuzzywuzzy import fuzz
import Levenshtein
import sqlite3
import string

# Function to normalize ingredient strings for comparison
def normalize_ingredient(ingredient):
    # Convert to lowercase
    ingredient = ingredient.lower()
    # Remove punctuation
    ingredient = ingredient.translate(str.maketrans('', '', string.punctuation))
    # Remove extra spaces
    ingredient = ingredient.strip()
    # Remove trailing 's' for simple plural handling
    if ingredient.endswith('s') and not ingredient.endswith('ss'):
        ingredient = ingredient.rstrip('s')
    return ingredient

# Function to clean and extract main ingredients from recipe ingredients list
def extract_main_ingredients(ingredients_list):
    # Split the ingredients by comma
    raw_ingredients = ingredients_list.split(',')
    # Normalize each ingredient
    normalized_ingredients = [normalize_ingredient(ing) for ing in raw_ingredients]
    return normalized_ingredients

# Function to select a cuisine
def select_cuisine(cuisines):
    print("Select a cuisine:")
    for i, cuisine in enumerate(cuisines, start=1):
        print(f"{i}. {cuisine}")

    while True:
        try:
            choice = int(input("Enter the number of your selected cuisine: "))
            if 1 <= choice <= len(cuisines):
                return cuisines[choice - 1]
            else:
                print("Invalid choice. Please select a valid cuisine.")
        except ValueError:
            print("Please enter a number corresponding to the cuisine.")

# Function to gather ingredients based on categories
def input_ingredients():
    categories = ["Proteins", "Dairy", "Carbs/Grains", "Fruits", "Vegetables", "Spices/Seasonings", "Oils"]
    ingredients = {}

    for category in categories:
        print(f"\nEnter ingredients for {category}. Type 'done' to finish entering for this category.")
        user_input = []
        while True:
            ingredient = input(f"Add {category}: ")
            if ingredient.lower() == 'done':
                break
            user_input.append(ingredient)
        ingredients[category] = user_input
    return ingredients

# Function to match user input ingredients with available recipes
def match_recipes_with_fuzzy(selected_cuisine, user_ingredients, cursor):
    cursor.execute("SELECT rec_name, ingredients_list, link FROM Cuisines WHERE cui_type = ?", (selected_cuisine,))
    recipes = cursor.fetchall()

    matched_recipes = []

    # Normalize user ingredients
    normalized_user_ingredients = [normalize_ingredient(ingredient) for ingredients in user_ingredients.values() for ingredient in ingredients]

    for recipe in recipes:
        rec_name, ingredients_list, link = recipe
        # Extract and normalize recipe ingredients
        recipe_ingredients = extract_main_ingredients(ingredients_list)

        # Count how many user ingredients match recipe ingredients using fuzzy matching
        match_count = 0
        for user_ing in normalized_user_ingredients:
            for rec_ing in recipe_ingredients:
                # Use fuzzy matching to allow flexible matching (e.g., different spelling, slight variations)
                similarity = fuzz.token_set_ratio(user_ing, rec_ing)
                if similarity > 80:  # Set a threshold for similarity (80 is often used)
                    match_count += 1
                    break  # Avoid double counting for the same user ingredient

        if match_count > 0:
            matched_recipes.append((rec_name, ingredients_list, link, match_count))

    # Sort matched recipes by the number of matches in descending order
    matched_recipes.sort(key=lambda x: x[3], reverse=True)

    return matched_recipes

def add_custom_recipe():
    # Get input from the user for a custom recipe
    cui_type = input("Enter the cuisine type: ")
    rec_name = input("Enter the recipe name: ")
    ingredients_list = input("Enter the ingredients (separated by commas): ")
    link = input("Enter the recipe link (optional): ")

    # Insert the custom recipe into the CustomCuisines table
    cursor.execute('''INSERT INTO CustomCuisines (cui_type, rec_name, ingredients_list, link) 
                      VALUES (?, ?, ?, ?)''', (cui_type, rec_name, ingredients_list, link))

    # Commit the changes to the database
    connection.commit()
    print(f"Recipe '{rec_name}' added to custom cuisines!")


# Main function
def main():
    # Connect to the database (it will create the file if it doesn't exist)
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()

    # Removes old table
    cursor.execute("DROP TABLE IF EXISTS Cuisines")

    # Create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Cuisines
    (cui_type TEXT, rec_name TEXT, ingredients_list TEXT, link TEXT)
    ''')

    while True:
        print("\nMenu:")
        print("1. Select a cuisine and match a recipe")
        print("2. Add a custom recipe")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == '1':
            # Existing process to match a recipe
            selected_cuisine = select_cuisine()
            user_ingredients = input_ingredients()
            matched_recipe = match_recipes(selected_cuisine, user_ingredients)

            if matched_recipe:
                rec_name, ingredients_list, link = matched_recipe
                print(f"\nBest matching recipe: {rec_name}\nIngredients: {ingredients_list}\nLink: {link}")
            else:
                print("\nNo matching recipes found.")
        elif choice == '2':
            # Add a custom recipe
            add_custom_recipe()
        elif choice == '3':
            # Exit the program
            break
        else:
            print("Invalid choice, please try again.")

    # Inserting sample data (Add all your recipes here)
    try:
        # Italian Dishes
        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Italian', 'Air Fryer Chicken Parmesan',
                        '2 boneless skinless chicken breasts, kosher salt, black pepper, all-purpose flour, eggs, panko breadcrumbs, Parmesan cheese, olive oil, crushed red pepper, garlic powder, marinara sauce, mozzarella cheese',
                        'https://www.allrecipes.com/air-fryer-chicken-parmesan-recipe-8698442'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Italian', 'Pizza on the Grill',
                        'warm water, active dry yeast, white sugar, all-purpose flour, olive oil, kosher salt, garlic minced, fresh basil, tomatoes, black olives, roasted red peppers, mozzarella cheese',
                        'https://www.allrecipes.com/recipe/14522/pizza-on-the-grill-i/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Italian', 'World\'s Best Lasagna',
                        'Italian sausage, ground beef, minced onion, garlic, crushed tomatoes, tomato sauce, tomato paste, water, sugar, parsley, basil, salt, Italian seasoning, fennel seeds, black pepper, lasagna noodles, ricotta cheese, egg, mozzarella cheese, Parmesan cheese',
                        'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Italian', 'Shrimp Scampi with Pasta',
                        'linguine pasta, butter, extra-virgin olive oil, shallots, garlic, red pepper flakes, shrimp, kosher salt, white wine, lemon, parsley',
                        'https://www.allrecipes.com/recipe/229960/shrimp-scampi-with-pasta/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Italian', 'The Best Meatballs',
                        'ground beef, ground veal, ground pork, Romano cheese, eggs, garlic, parsley, stale bread, water, olive oil',
                        'https://www.allrecipes.com/recipe/40399/the-best-meatballs/'))

        # Indian Dishes
        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Indian', 'Butter Chicken (Murgh Makhani)',
                        'garam masala, tandoori masala, Madras curry powder, cumin, cardamom, cayenne pepper, chicken thighs, butter, onion, garlic, lemon juice, ginger, tomato puree, yogurt, cashews, cilantro',
                        'https://www.allrecipes.com/recipe/246717/indian-butter-chicken-chicken-makhani/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Indian', 'Chicken Tikka Masala',
                        'yogurt, lemon juice, cumin, cinnamon, cayenne pepper, black pepper, ginger, chicken breasts, garlic, jalapeno, paprika, tomato sauce, heavy cream, cilantro',
                        'https://www.allrecipes.com/recipe/45736/chicken-tikka-masala/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Indian', 'Red Lentil Curry',
                        'red lentils, water, vegetable oil, onion, curry paste, curry powder, turmeric, cumin, chili powder, salt, sugar, garlic, ginger, tomato puree',
                        'https://www.allrecipes.com/recipe/16641/red-lentil-curry/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Indian', 'Green Onion Garlic Naan Bread',
                        'bread flour, kosher salt, baking powder, Greek yogurt, garlic, green onions, melted butter',
                        'https://www.allrecipes.com/recipe/8467738/green-onion-garlic-naan-bread/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Indian', 'Golden Butter Rice',
                        'butter, ginger, turmeric, cayenne pepper, brown sugar, salt, basmati rice, water, walnuts, green onions',
                        'https://www.allrecipes.com/golden-butter-rice-recipe-8599188'))

        # Mexican Dishes
        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Mexican', 'The Best Chimichangas',
                        'kosher salt, black pepper, garlic powder, chicken breasts, olive oil, onion, garlic, ancho chili powder, cumin, water, chicken bouillon, green chiles, all-purpose flour, peanut oil, flour tortillas, refried beans, pepper jack cheese',
                        'https://www.allrecipes.com/the-best-chimichangas-recipe-8637540'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Mexican', 'Traditional Mexican Street Tacos',
                        'corn tortillas, cooked chicken, cilantro, white onion, guacamole, lime',
                        'https://www.allrecipes.com/recipe/257988/traditional-mexican-street-tacos/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Mexican', 'Enchiladas Verdes',
                        'tomatillos, serrano peppers, garlic, vegetable oil, corn tortillas, water, chicken bouillon, shredded chicken, lettuce, cilantro, crema, cotija cheese',
                        'https://www.allrecipes.com/recipe/213700/enchiladas-verdes/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Mexican', 'Beef Tamales',
                        'boneless chuck roast, garlic, dried corn husks, dried ancho chiles, vegetable oil, all-purpose flour, beef broth, garlic, oregano, cumin seeds, ground cumin, red pepper flakes, vinegar, lard, masa harina',
                        'https://www.allrecipes.com/recipe/34759/beef-tamales/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Mexican', 'Fabulous Wet Burritos',
                        'ground beef, onion, garlic, cumin, salt, pepper, refried beans, green chile peppers, chili, tomato soup, enchilada sauce, flour tortillas, lettuce, tomatoes, Mexican cheese blend, green onions',
                        'https://www.allrecipes.com/recipe/70404/fabulous-wet-burritos/'))

        # Japanese Dishes
        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Japanese', 'Chicken Katsu',
                        'chicken breasts, salt, pepper, all-purpose flour, egg, panko bread crumbs, oil for frying',
                        'https://www.allrecipes.com/recipe/72068/chicken-katsu/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Japanese', 'Japanese-Style Rolled Omelet (Tamagoyaki)',
                        'eggs, water, soy sauce, mirin, kosher salt, sugar, cayenne pepper, sesame oil, vegetable oil, furikake',
                        'https://www.allrecipes.com/japanese-style-rolled-omelet-tamagoyaki-recipe-8644676'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Japanese', 'Onigiri (Japanese Rice Balls)',
                        'short-grain white rice, water, salt, bonito shavings, nori, sesame seeds',
                        'https://www.allrecipes.com/recipe/140422/onigiri-japanese-rice-balls/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Japanese', 'Spicy Tuna Sushi Roll',
                        'glutinous white rice, water, rice vinegar, tuna, mayonnaise, chili powder, wasabi paste, nori, cucumber, carrot, avocado',
                        'https://www.allrecipes.com/recipe/190943/spicy-tuna-sushi-roll/'))


        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Japanese', 'Miso Soup',
                        'water, dashi granules, miso paste, silken tofu, green onions',
                        'https://www.allrecipes.com/recipe/13107/miso-soup/'))

        # German Dishes
        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('German', 'German Pork Chops and Sauerkraut',
                        'pork chops, sauerkraut, red apple, onion, brown sugar, caraway seeds',
                        'https://www.allrecipes.com/recipe/216330/german-pork-chops-and-sauerkraut/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('German', 'Creamy Dill German Potato Salad',
                        'yellow potatoes, mayonnaise, Greek yogurt, dill pickle brine, Dijon mustard, eggs, onion, dill pickles',
                        'https://www.allrecipes.com/creamy-dill-german-potato-salad-recipe-8660093'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('German', 'Wiener Schnitzel',
                        'veal cutlets, all-purpose flour, eggs, Parmesan cheese, milk, parsley, salt, pepper, nutmeg, bread crumbs, butter, lemon',
                        'https://www.allrecipes.com/recipe/78117/wienerschnitzel/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('German', 'German Zwiebelkuchen (Onion Pie)',
                        'onions, bacon, sour cream, eggs, all-purpose flour, salt, caraway seed, pastry for pie',
                        'https://www.allrecipes.com/recipe/24674/german-zwiebelkuchen-onion-pie/'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Chinese', 'Baked Sweet And Sour Chicken',
                        'olive oil, chicken thighs, black pepper, kosher salt, eggs, flour, bell peppers, ketchup, pineapple juice, honey, soy sauce, rice vinegar, white rice',
                        'https://www.allrecipes.com/baked-sweet-and-sour-chicken-recipe-8654805'))

        cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                       ('Chinese', "Sheet Pan General Tso's Chicken and Broccoli",
                        'Sambal oelek, tablespoon ricevinegar, hoisin sauce, soy sauce toasted sesame oil light brown sugar minced garlic, broccoli florets, olive oil, salt, black pepper, chicken nuggets, white rice, green onions, sesame seeds',
                        'https://www.allrecipes.com/sheet-pan-general-tso-s-chicken-and-broccoli-recipe-8715504'))
        # Commit the changes
        connection.commit()

    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Step 1: Select Cuisine
    cuisines = ["Italian", "Indian", "Mexican", "Japanese", "German", "Chinese"]
    selected_cuisine = select_cuisine(cuisines)
    print(f"\nYou have selected {selected_cuisine} cuisine.")

    # Step 2: Input ingredients by category
    print("\nNow let's input your ingredients based on categories.")
    user_ingredients = input_ingredients()

    # Step 3: Match the input ingredients with available recipes
    matched_recipes = match_recipes_with_fuzzy(selected_cuisine, user_ingredients, cursor)

    if matched_recipes:
        print("\nHere are the best matching recipes based on your ingredients:")
        for rec in matched_recipes:
            rec_name, ingredients_list, link, match_count = rec
            print(f"\nRecipe: {rec_name}\nMatched Ingredients: {match_count}\nIngredients: {ingredients_list}\nLink: {link}")
    else:
        print("\nNo matching recipes found for the selected ingredients.")

    # Close the cursor and connection
    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()
