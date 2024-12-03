from database import Database
from PySide6.QtWidgets import QApplication
from GUI import MainWindow
from utils import Recipe

database = Database()
app = QApplication([])
gui = MainWindow(database)


# Test selecting a cuisine shows appropriate recipes.
def test_select_cuisine():
    gui.combo.setCurrentText("Italian")
    results = gui._MainWindow__search()
    assert len(results) > 0


# Test entering ingredients returns matching recipes.
def test_input_ingredients():
    gui.search_bar.setText("Chicken")
    results = gui._MainWindow__search()
    assert len(results) > 0


# Test generating recipes for partial ingredient matches.
def test_generate_recipe():
    gui.search_bar.setText("Chicken")
    results = gui._MainWindow__search()
    assert len(results) > 0


# Test if recipes have details for display.
def test_view_recipe():
    recipes = database.get_all_recipes_names()
    assert len(recipes) > 0
    recipe_data = database.get_recipe(recipes[0][0])
    assert "name" in recipe_data and "description" in recipe_data


# Test if no recipes are found for invalid input.
def test_handle_no_recipe_found():
    gui.search_bar.setText("NonExistentIngredient")
    results = gui._MainWindow__search()
    assert len(results) == 0


# Test the system returns default/fallback recipes for empty input.
def test_error_handling():
    gui.search_bar.setText("")
    results = gui._MainWindow__search()
    assert len(results) > 0
    print("test_error_handling passed")


# Test the system returns recipes for valid user input.
def test_validate_user_input():
    gui.search_bar.setText("Chicken")
    results = gui._MainWindow__search()
    assert len(results) > 0
    print("test_validate_user_input passed")


# Test saving a recipe as a favorite.
def test_save_recipe():
    recipe_name = "Air Fryer Chicken Parmesan"
    database.set_favorite(recipe_name, 1)
    status = database.isfavorite(recipe_name)
    assert status is True


# Test if saved recipes are displayed.
def test_display_saved_recipes():
    database.set_favorite("Air Fryer Chicken Parmesan", 1)
    favorites = database.get_favorite_recipes()
    assert len(favorites) > 0


if __name__ == "__main__":
    try:
        test_select_cuisine()
        print("test_select_cuisine passed")

        test_input_ingredients()
        print("test_input_ingredients passed")

        test_generate_recipe()
        print("test_generate_recipe passed")

        test_view_recipe()
        print("test_view_recipe passed")

        test_handle_no_recipe_found()
        print("test_handle_no_recipe_found passed")

        test_error_handling()
        print("test_error_handling passed")

        test_validate_user_input()
        print("test_validate_user_input passed")

        test_save_recipe()
        print("test_save_recipe passed")

        test_display_saved_recipes()
        print("test_display_saved_recipes passed")

    finally:
        app.quit()
