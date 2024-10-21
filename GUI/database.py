from fuzzywuzzy import fuzz
import Levenshtein
import sqlite3
import string


class Database:
    
    def __init__(self) -> None:
        self.cursor = ""
        self.main()


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

    def main(self):
        # Connect to the database (it will create the file if it doesn't exist)
        connection = sqlite3.connect('my_database.db')
        self.cursor = connection.cursor()


        # Create a table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Cuisines
        (cui_type TEXT, rec_name TEXT, ingredients_list TEXT, link TEXT)
        ''')

        # Inserting sample data (Add all your recipes here)
        try:
            # Italian Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Italian', 'Air Fryer Chicken Parmesan',
                            '2 boneless skinless chicken breasts, kosher salt, black pepper, all-purpose flour, eggs, panko breadcrumbs, Parmesan cheese, olive oil, crushed red pepper, garlic powder, marinara sauce, mozzarella cheese',
                            'https://www.allrecipes.com/air-fryer-chicken-parmesan-recipe-8698442'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Italian', 'Pizza on the Grill',
                            'warm water, active dry yeast, white sugar, all-purpose flour, olive oil, kosher salt, garlic minced, fresh basil, tomatoes, black olives, roasted red peppers, mozzarella cheese',
                            'https://www.allrecipes.com/recipe/14522/pizza-on-the-grill-i/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Italian', 'World\'s Best Lasagna',
                            'Italian sausage, ground beef, minced onion, garlic, crushed tomatoes, tomato sauce, tomato paste, water, sugar, parsley, basil, salt, Italian seasoning, fennel seeds, black pepper, lasagna noodles, ricotta cheese, egg, mozzarella cheese, Parmesan cheese',
                            'https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Italian', 'Shrimp Scampi with Pasta',
                            'linguine pasta, butter, extra-virgin olive oil, shallots, garlic, red pepper flakes, shrimp, kosher salt, white wine, lemon, parsley',
                            'https://www.allrecipes.com/recipe/229960/shrimp-scampi-with-pasta/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Italian', 'The Best Meatballs',
                            'ground beef, ground veal, ground pork, Romano cheese, eggs, garlic, parsley, stale bread, water, olive oil',
                            'https://www.allrecipes.com/recipe/40399/the-best-meatballs/'))

            # Indian Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Indian', 'Butter Chicken (Murgh Makhani)',
                            'garam masala, tandoori masala, Madras curry powder, cumin, cardamom, cayenne pepper, chicken thighs, butter, onion, garlic, lemon juice, ginger, tomato puree, yogurt, cashews, cilantro',
                            'https://www.allrecipes.com/recipe/246717/indian-butter-chicken-chicken-makhani/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Indian', 'Chicken Tikka Masala',
                            'yogurt, lemon juice, cumin, cinnamon, cayenne pepper, black pepper, ginger, chicken breasts, garlic, jalapeno, paprika, tomato sauce, heavy cream, cilantro',
                            'https://www.allrecipes.com/recipe/45736/chicken-tikka-masala/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Indian', 'Red Lentil Curry',
                            'red lentils, water, vegetable oil, onion, curry paste, curry powder, turmeric, cumin, chili powder, salt, sugar, garlic, ginger, tomato puree',
                            'https://www.allrecipes.com/recipe/16641/red-lentil-curry/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Indian', 'Green Onion Garlic Naan Bread',
                            'bread flour, kosher salt, baking powder, Greek yogurt, garlic, green onions, melted butter',
                            'https://www.allrecipes.com/recipe/8467738/green-onion-garlic-naan-bread/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Indian', 'Golden Butter Rice',
                            'butter, ginger, turmeric, cayenne pepper, brown sugar, salt, basmati rice, water, walnuts, green onions',
                            'https://www.allrecipes.com/golden-butter-rice-recipe-8599188'))

            # Mexican Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Mexican', 'The Best Chimichangas',
                            'kosher salt, black pepper, garlic powder, chicken breasts, olive oil, onion, garlic, ancho chili powder, cumin, water, chicken bouillon, green chiles, all-purpose flour, peanut oil, flour tortillas, refried beans, pepper jack cheese',
                            'https://www.allrecipes.com/the-best-chimichangas-recipe-8637540'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Mexican', 'Traditional Mexican Street Tacos',
                            'corn tortillas, cooked chicken, cilantro, white onion, guacamole, lime',
                            'https://www.allrecipes.com/recipe/257988/traditional-mexican-street-tacos/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Mexican', 'Enchiladas Verdes',
                            'tomatillos, serrano peppers, garlic, vegetable oil, corn tortillas, water, chicken bouillon, shredded chicken, lettuce, cilantro, crema, cotija cheese',
                            'https://www.allrecipes.com/recipe/213700/enchiladas-verdes/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Mexican', 'Beef Tamales',
                            'boneless chuck roast, garlic, dried corn husks, dried ancho chiles, vegetable oil, all-purpose flour, beef broth, garlic, oregano, cumin seeds, ground cumin, red pepper flakes, vinegar, lard, masa harina',
                            'https://www.allrecipes.com/recipe/34759/beef-tamales/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Mexican', 'Fabulous Wet Burritos',
                            'ground beef, onion, garlic, cumin, salt, pepper, refried beans, green chile peppers, chili, tomato soup, enchilada sauce, flour tortillas, lettuce, tomatoes, Mexican cheese blend, green onions',
                            'https://www.allrecipes.com/recipe/70404/fabulous-wet-burritos/'))

            # Japanese Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Japanese', 'Chicken Katsu',
                            'chicken breasts, salt, pepper, all-purpose flour, egg, panko bread crumbs, oil for frying',
                            'https://www.allrecipes.com/recipe/72068/chicken-katsu/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Japanese', 'Japanese-Style Rolled Omelet (Tamagoyaki)',
                            'eggs, water, soy sauce, mirin, kosher salt, sugar, cayenne pepper, sesame oil, vegetable oil, furikake',
                            'https://www.allrecipes.com/japanese-style-rolled-omelet-tamagoyaki-recipe-8644676'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Japanese', 'Onigiri (Japanese Rice Balls)',
                            'short-grain white rice, water, salt, bonito shavings, nori, sesame seeds',
                            'https://www.allrecipes.com/recipe/140422/onigiri-japanese-rice-balls/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Japanese', 'Spicy Tuna Sushi Roll',
                            'glutinous white rice, water, rice vinegar, tuna, mayonnaise, chili powder, wasabi paste, nori, cucumber, carrot, avocado',
                            'https://www.allrecipes.com/recipe/190943/spicy-tuna-sushi-roll/'))


            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('Japanese', 'Miso Soup',
                            'water, dashi granules, miso paste, silken tofu, green onions',
                            'https://www.allrecipes.com/recipe/13107/miso-soup/'))

            # German Dishes
            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('German', 'German Pork Chops and Sauerkraut',
                            'pork chops, sauerkraut, red apple, onion, brown sugar, caraway seeds',
                            'https://www.allrecipes.com/recipe/216330/german-pork-chops-and-sauerkraut/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('German', 'Creamy Dill German Potato Salad',
                            'yellow potatoes, mayonnaise, Greek yogurt, dill pickle brine, Dijon mustard, eggs, onion, dill pickles',
                            'https://www.allrecipes.com/creamy-dill-german-potato-salad-recipe-8660093'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('German', 'Wiener Schnitzel',
                            'veal cutlets, all-purpose flour, eggs, Parmesan cheese, milk, parsley, salt, pepper, nutmeg, bread crumbs, butter, lemon',
                            'https://www.allrecipes.com/recipe/78117/wienerschnitzel/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('German', 'German Zwiebelkuchen (Onion Pie)',
                            'onions, bacon, sour cream, eggs, all-purpose flour, salt, caraway seed, pastry for pie',
                            'https://www.allrecipes.com/recipe/24674/german-zwiebelkuchen-onion-pie/'))

            self.cursor.execute('INSERT INTO Cuisines (cui_type, rec_name, ingredients_list, link) VALUES (?, ?, ?, ?)',
                        ('German', 'German Currywurst',
                            'tomato sauce, kielbasa, chili sauce, onion salt, white sugar, black pepper, paprika, curry powder',
                            'https://www.allrecipes.com/recipe/24676/german-currywurst/'))

            # Commit the changes
            connection.commit()

        except sqlite3.IntegrityError as e:
            print(f"IntegrityError: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_all_recipes(self):
        self.cursor.execute("SELECT * FROM Cuisines")
        return self.cursor.fetchall()
    
    def get_recipes(self, cuisine):
        self.cursor.execute(f"SELECT * FROM Cuisines where cui_type = '{cuisine}'") 
        return self.cursor.fetchall()
    
    def get_recipe(self, cuisine):
        self.cursor.execute(f"SELECT * FROM Cuisines where cui_type = '{cuisine}'") 
        return self.cursor.fetchone()

if __name__ == "__main__":
    data = Database()
