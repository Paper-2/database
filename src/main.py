import sys
from GUI_module import *
from PySide6.QtWidgets import *
from database import Database
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'GUI')))
def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    data = Database()
    
    recipe_data = data.get_recipe("Italian")
    recipe = Recipe(recipe_data)
    recipe_widget_instance = recipe_widget(recipe).horizontal_item_widget()
    window.add_item(recipe_widget_instance)
    
    
    
    app.exec()


class Recipe(Recipe_gui_proto):
    def __init__(self, recipe_as_list) -> None:
        self.cui_type = recipe_as_list[0]
        self.title = recipe_as_list[1]
        self.ingredients = recipe_as_list[2]
        self.instructions = recipe_as_list[3]

if __name__ == '__main__':
    main()
    pass