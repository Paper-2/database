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

# Italian Dishes

try:
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

    

    # Commit the changes
    connection.commit()

except sqlite3.IntegrityError as e:
    print(f"IntegrityError: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Query the database
cursor.execute("SELECT * FROM Cuisines")

results = cursor.fetchall()
print(results)

# Close the cursor and connection
cursor.close()
connection.close()
