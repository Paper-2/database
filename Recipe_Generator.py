import sqlite3

# Connect to the database (it will create the file if it doesn't exist)
connection = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = connection.cursor()

# Removes old table
cursor.execute("DROP TABLE IF EXISTS Cuisines")

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS Cuisines
(cui_type TEXT, rec_name TEXT, ingredients_list TEXT, link TEXT)
''')

try:
    # Italian Dishes

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES 
    ('Italian', 'Air Fryer Chicken Parmesan', '2 (8-ounce) boneless skinless chicken breasts, patted dry, 
    3/4 teaspoon kosher salt, 
    1/2 teaspoon freshly ground black pepper, 
    1/3 cup all-purpose flour, 
    2 large eggs, lightly beaten, 
    1 1/2 cups seasoned panko (Japanese-style breadcrumbs), 
    1/4 cup freshly grated Parmesan cheese, plus more for garnish, 
    2 tablespoons olive oil, 
    1/4 teaspoon crushed red pepper, 
    1/4 teaspoon garlic powder, 
    1 cup jarred marinara sauce plus more for serving, 
    1 cup shredded low-moisture, part-skim mozzarella cheese', 
    'https://www.allrecipes.com/air-fryer-chicken-parmesan-recipe-8698442')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES 
    ('Italian', 'Pizza on the Grill', '1 cup warm water (110 degrees F/45 degrees C), 
    1 (.25 ounce) package active dry yeast, 
    1 pinch white sugar, 
    3 ⅓ cups all-purpose flour, 
    1 tablespoon olive oil, 
    2 teaspoons kosher salt, 
    2 cloves garlic minced, 
    1 tablespoon chopped fresh basil, 
    ½ cup olive oil, 
    1 teaspoon minced garlic, 
    ¼ cup tomato sauce, 
    1 cup chopped tomatoes, 
    ¼ cup sliced black olives, 
    ¼ cup roasted red peppers drained and chopped, 
    2 cups shredded mozzarella cheese, 
    4 tablespoons chopped fresh basil', 
    'https://www.allrecipes.com/recipe/14522/pizza-on-the-grill-i/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Italian', 'World's Best Lasagna',
    '1 pound sweet Italian sausage,
    ¾ pound lean ground beef,
    ½ cup minced onion,
    2 cloves garlic, crushed,
    1 (28 ounce) can crushed tomatoes,
    2 (6.5 ounce) cans canned tomato sauce,
    2 (6 ounce) cans tomato paste,
    ½ cup water,
    2 tablespoons white sugar,
    4 tablespoons chopped fresh parsley,
    1 ½ teaspoons dried basil leaves,
    1 ½ teaspoons salt,
    1 teaspoon Italian seasoning,
    ½ teaspoon fennel seeds,
    ¼ teaspoon ground black pepper,
    12 lasagna noodles,
    16 ounces ricotta cheese,
    1 egg,
    ¾ pound mozzarella cheese sliced,
    ¾ cup grated Parmesan cheese',
    'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Italian', 'Shrimp Scampi with Pasta',
    1 (16 ounce) package linguine pasta,
    2 tablespoons butter,
    2 tablespoons extra-virgin olive oil,
    2 shallots finely diced,
    2 cloves garlic minced,
    1 pinch red pepper flakes,
    1 pound shrimp peeled and deveined,
    1 pinch kosher salt and freshly ground pepper,
    ½ cup dry white wine,
    1 lemon juiced,
    2 tablespoons butter,
    2 tablespoons extra-virgin olive oil,
    ¼ cup finely chopped fresh parsley leaves,
    1 teaspoon extra-virgin olive oil,
    'https://www.allrecipes.com/recipe/229960/shrimp-scampi-with-pasta/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Italian', 'The Best Meatballs',
    1 pound ground beef,
    ½ pound ground veal,
    ½ pound ground pork,
    1 cup freshly grated Romano cheese,
    2 eggs,
    2 cloves garlic minced,
    1 ½ tablespoons chopped Italian flat leaf parsley,
    salt and ground black pepper to taste,
    2 cups stale Italian bread crumbled,
    1 ½ cups lukewarm water,
    1 cup olive oil,
    'https://www.allrecipes.com/recipe/40399/the-best-meatballs/')''')

    # Indian Dishes

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Indian', 'Butter Chicken (Murgh Makhani)',
    2 teaspoons garam masala,
    2 teaspoons tandoori masala powder,
    2 teaspoons Madras curry powder,
    1 teaspoon ground cumin,
    ½ teaspoon ground cardamom,
    ½ teaspoon ground cayenne pepper,
    salt and ground black pepper to taste,
    1 ½ pounds boneless skinless chicken thighs cut into bite-size pieces,
    3 tablespoons butter,
    1 yellow onion chopped,
    4 cloves garlic minced,
    1 tablespoon lemon juice,
    2 teaspoons chopped fresh ginger,
    1 cup tomato puree,
    1 cup half-and-half,
    ¼ cup plain yogurt,
    ⅓ cup cashews,
    1 bunch fresh cilantro stems removed,
    'https://www.allrecipes.com/recipe/246717/indian-butter-chicken-chicken-makhani/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Indian', 'Chicken Tikka Masala',
    1 cup yogurt,
    1 tablespoon lemon juice,
    4 teaspoons ground cumin divided,
    1 teaspoon ground cinnamon,
    2 teaspoons cayenne pepper,
    2 teaspoons freshly ground black pepper,
    1 tablespoon minced fresh ginger,
    2 teaspoons salt divided or more to taste,
    3 boneless skinless chicken breasts cut into bite-size pieces,
    4 long skewers,
    1 tablespoon butter,
    1 clove garlic minced,
    1 jalapeno pepper finely chopped,
    2 teaspoons paprika,
    1 (8 ounce) can tomato sauce,
    1 cup heavy cream,
    ¼ cup chopped fresh cilantro,
    'https://www.allrecipes.com/recipe/45736/chicken-tikka-masala/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Indian', 'Red Lentil Curry',
    2 cups red lentils,
    3 cups water or more as needed,
    1 tablespoon vegetable oil,
    1 large onion diced,
    2 tablespoons curry paste,
    1 tablespoon curry powder,
    1 teaspoon ground turmeric,
    1 teaspoon ground cumin,
    1 teaspoon chili powder,
    1 teaspoon salt,
    1 teaspoon white sugar,
    1 teaspoon minced garlic,
    1 teaspoon minced fresh ginger,
    1 (14.25 ounce) can tomato puree,
    'https://www.allrecipes.com/recipe/16641/red-lentil-curry/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Indian', 'Green Onion Garlic Naan Bread',
    1 ½ cups bread flour plus more as needed,
    ½ teaspoon kosher salt,
    2 teaspoons baking powder,
    1 cup plain Greek yogurt,
    4 cloves garlic, crushed,
    ½ cup thinly sliced green onions,
    2 tablespoons melted butter,
    'https://www.allrecipes.com/recipe/8467738/green-onion-garlic-naan-bread/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Indian', 'Golden Butter Rice',
    1/2 cup unsalted butter,
    1 tablespoon finely grated fresh ginger,
    1 1/4 teaspoons ground turmeric,
    1/4 teaspoon cayenne pepper,
    1 tablespoon brown sugar,
    1 teaspoon fine salt,
    2 cups basmati rice or other long grain white rice,
    3 cups water,
    1/3 cup chopped walnuts,
    1/3 cup sliced green onions,
    'https://www.allrecipes.com/golden-butter-rice-recipe-8599188')''')

    # Mexican Dishes

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Mexican', 'The Best Chimichangas',
    1 teaspoon kosher salt,
    1/2 teaspoon freshly ground black pepper,
    1 teaspoon garlic powder,
    3 skinless, boneless chicken breasts,
    1 tablespoon olive oil,
    1/2 cup finely chopped onion,
    3 cloves garlic, finely minced,
    1 tablespoon ancho chili powder,
    2 teaspoons ground cumin,
    2 cups plus 3 tablespoons water,
    1 chicken bouillon cube or 1 teaspoon bouillon paste such as Better Than Bouillon,
    1 (7 ounce) can green chiles,
    3 tablespoons all-purpose flour,
    2 cups peanut oil or vegetable oil for frying or as needed,
    8 (10 to 12-inch) flour tortillas,
    1 1/2 cups refried beans heated,
    1 (8 ounce) block pepper Jack cheese shredded,
    Toppings such as warm queso, pico de gallo, cilantro, and shredded lettuce,
    'https://www.allrecipes.com/the-best-chimichangas-recipe-8637540')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Mexican', 'Traditional Mexican Street Tacos',
    6 (5-inch) corn tortillas,
    3 cups chopped cooked chicken,
    4 sprigs fresh cilantro chopped,
    ½ cup chopped white onion,
    1 cup guacamole,
    1 lime cut into wedges,
    'https://www.allrecipes.com/recipe/257988/traditional-mexican-street-tacos/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Mexican', 'Enchiladas Verdes',
    2 ¼ pounds small green tomatillos, husks removed,
    3 serrano peppers,
    2 cloves garlic,
    1 cup vegetable oil for frying,
    9 corn tortillas,
    3 cups water,
    4 teaspoons chicken bouillon granules,
    ½ store-bought rotisserie chicken meat removed and shredded,
    ¼ head iceberg lettuce, shredded,
    1 cup cilantro leaves,
    1 (8 ounce) container Mexican crema crema fresca,
    1 cup grated cotija cheese,
    'https://www.allrecipes.com/recipe/213700/enchiladas-verdes/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Mexican', 'Beef Tamales',
    4 pounds boneless chuck roast,
    4 cloves garlic,
    3 (8 ounce) packages dried corn husks,
    4 dried ancho chiles,
    2 tablespoons vegetable oil,
    2 tablespoons all-purpose flour,
    1 cup beef broth,
    2 cloves garlic, minced,
    2 teaspoons chopped fresh oregano,
    1 teaspoon cumin seeds,
    1 teaspoon ground cumin,
    1 teaspoon red pepper flakes,
    1 teaspoon white vinegar,
    salt to taste,
    3 cups lard,
    1 tablespoon salt,
    9 cups masa harina,
    'https://www.allrecipes.com/recipe/34759/beef-tamales/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Mexican', 'Fabulous Wet Burritos',
    1 pound ground beef,
    ½ cup chopped onion,
    1 clove garlic minced,
    ½ teaspoon cumin,
    ¼ teaspoon salt,
    ⅛ teaspoon pepper,
    1 (16 ounce) can refried beans,
    1 (4.5 ounce) can diced green chile peppers,
    1 (15 ounce) can chili without beans,
    1 (10.5 ounce) can condensed tomato soup,
    1 (10 ounce) can enchilada sauce,
    6 (12 inch) flour tortillas warmed,
    2 cups shredded lettuce divided,
    1 cup chopped tomatoes divided,
    2 cups shredded Mexican cheese blend divided,
    ½ cup chopped green onions divided,
    'https://www.allrecipes.com/recipe/70404/fabulous-wet-burritos/')''')

    # Japanese Dishes

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Japanese', 'Chicken Katsu',
    4 skinless boneless chicken breast halves - pounded to 1/2 inch thickness,
    salt and pepper to taste,
    2 tablespoons all-purpose flour,
    1 egg beaten,
    1 cup panko bread crumbs,
    1 cup oil for frying, or as needed,
    'https://www.allrecipes.com/recipe/72068/chicken-katsu/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Japanese', 'Japanese-Style Rolled Omelet (Tamagoyaki)',
    4 large eggs,
    4 teaspoons water,
    1 teaspoon soy sauce,
    1 teaspoon mirin,
    1/4 teaspoon kosher salt,
    1/4 teaspoon white sugar,
    1 pinch cayenne pepper,
    1/2 teaspoon sesame oil,
    1 1/2 teaspoons vegetable oil,
    1 teaspoon furikake,
    'https://www.allrecipes.com/japanese-style-rolled-omelet-tamagoyaki-recipe-8644676')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Japanese', 'Onigiri (Japanese Rice Balls)',
    4 cups uncooked short-grain white rice,
    5 ½ cups water, divided,
    ¼ teaspoon salt,
    ¼ cup bonito shavings (dry fish flakes),
    2 sheets nori (dry seaweed), cut into 1/2-inch strips,
    2 tablespoons sesame seeds,
    'https://www.allrecipes.com/recipe/140422/onigiri-japanese-rice-balls/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Japanese', 'Spicy Tuna Sushi Roll',
    2 cups uncooked glutinous white rice,
    2 ½ cups water,
    1 tablespoon rice vinegar,
    1 (5 ounce) can solid white tuna in water drained,
    1 tablespoon mayonnaise,
    1 teaspoon chili powder,
    1 teaspoon wasabi paste,
    4 sheets nori (dry seaweed),
    ½ cucumber finely diced,
    1 carrot finely diced,
    1 avocado - peeled, pitted and diced,
    'https://www.allrecipes.com/recipe/190943/spicy-tuna-sushi-roll/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('Japanese', 'Miso Soup',
    4 cups water,
    2 teaspoons dashi granules,
    3 tablespoons miso paste,
    1 (8 ounce) package silken tofu diced,
    2 green onions, sliced diagonally into 1/2 inch pieces,
    'https://www.allrecipes.com/recipe/13107/miso-soup/')''')

    # German Dishes

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('German', 'German Pork Chops and Sauerkraut',
    8 center cut pork chops,
    2 pounds sauerkraut drained,
    1 large red apple diced,
    1 onion chopped,
    1 cup brown sugar,
    1 tablespoon caraway seeds,
    'https://www.allrecipes.com/recipe/216330/german-pork-chops-and-sauerkraut/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('German', 'Creamy Dill German Potato Salad',
    1 1/2 pounds yellow or gold potatoes,
    1/4 cup mayonnaise,
    1/4 cup plain Greek yogurt (such as Fage® 2%),
    1 tablespoon dill pickle brine,
    1 tablespoon Dijon mustard,
    3 large hard boiled eggs divdied,
    1/3 cup chopped onion,
    1/3 cup chopped dill pickles,
    salt and freshly ground black pepper to taste,
    'https://www.allrecipes.com/creamy-dill-german-potato-salad-recipe-8660093')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('German', 'Wiener Schnitzel',
    1 ½ pounds veal cutlets,
    ½ cup all-purpose flour,
    2 large eggs,
    3 tablespoons grated Parmesan cheese,
    2 tablespoons milk,
    1 teaspoon minced parsley,
    ½ teaspoon salt,
    ¼ teaspoon pepper,
    1 pinch ground nutmeg,
    1 cup dry bread crumbs,
    6 tablespoons butter,
    4 slices lemon,
    'https://www.allrecipes.com/recipe/78117/wienerschnitzel/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('German', 'German Zwiebelkuchen (Onion Pie)',
    6 pounds onions sliced,
    4 slices bacon,
    1 (16 ounce) container sour cream,
    4 large eggs,
    2 tablespoons all-purpose flour,
    ½ teaspoon salt,
    ½ teaspoon caraway seed,
    1 (14.1 ounce) package pastry for a double crust pie,
    'https://www.allrecipes.com/recipe/24674/german-zwiebelkuchen-onion-pie/')''')

    cursor.execute('''INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES ('German', 'German Currywurst',
    3 (15 ounce) cans tomato sauce,
    1 pound kielbasa,
    2 tablespoons chili sauce,
    ½ teaspoon onion salt,
    1 tablespoon white sugar,
    1 teaspoon ground black pepper,
    1 pinch paprika,
    Curry powder to taste,
    'https://www.allrecipes.com/recipe/24676/german-currywurst/')''')

    # Commit the changes
    connection.commit()

except sqlite3.IntegrityError as e:
    print(f"IntegrityError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Function to normalize ingredient strings for comparison
def normalize_ingredient(ingredient):
    return ingredient.lower().strip().rstrip('s')  # Make lowercase, remove spaces, ignore plurals

# Function to select a cuisine
def select_cuisine():
    cuisines = ["Italian", "Indian", "Mexican", "Japanese", "German"]
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
def match_recipes(selected_cuisine, user_ingredients):
    cursor.execute("SELECT rec_name, ingredients_list, link FROM Cuisines WHERE cui_type = ?", (selected_cuisine,))
    recipes = cursor.fetchall()

    best_match = None
    best_match_count = 0

    normalized_user_ingredients = [normalize_ingredient(ingredient) for ingredients in user_ingredients.values() for ingredient in ingredients]

    # Compare user ingredients with recipe ingredients
    for recipe in recipes:
        rec_name, ingredients_list, link = recipe
        recipe_ingredients = [normalize_ingredient(ing) for ing in ingredients_list.split(',')]

        # Count how many ingredients match
        match_count = sum(1 for ing in recipe_ingredients if ing in normalized_user_ingredients)

        # Keep track of the recipe with the most matches
        if match_count > best_match_count:
            best_match = (rec_name, ingredients_list, link)
            best_match_count = match_count

    return best_match

# Main function
def main():
    # Step 1: Select Cuisine
    selected_cuisine = select_cuisine()
    print(f"\nYou have selected {selected_cuisine} cuisine.")

    # Step 2: Input ingredients by category
    print("\nNow let's input your ingredients based on categories.")
    user_ingredients = input_ingredients()

    # Step 3: Match the input ingredients with available recipes
    matched_recipe = match_recipes(selected_cuisine, user_ingredients)

    if matched_recipe:
        rec_name, ingredients_list, link = matched_recipe
        print(f"\nBest matching recipe: {rec_name}\nIngredients: {ingredients_list}\nLink: {link}")
    else:
        print("\nNo matching recipes found for the selected ingredients.")

# Run the main function
if __name__ == "__main__":
    main()

# Close the cursor and connection
cursor.close()
connection.close()
