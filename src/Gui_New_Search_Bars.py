import sqlite3
import sys
import os

from PySide6.QtCore import Qt

from PySide6.QtGui import QColor, QPalette, QPixmap, QIcon

from PySide6.QtWidgets import *

ICON_PATH: str = os.path.join(os.getcwd(), "GUI", "recipe_database_icon.png")
PATH_TO_RECIPE: str = os.path.join(os.getcwd(), "mashed_potatoes.txt")
class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class Recipe:
    def __init__(self, path=None, title=None, ingredients=None, link=None):
        if path:
            self.path = path
            self.recipe = self.parse()
            self.title, self.ingredients, self.instructions = self.get_recipe_info()
            self.link = None
        else:

            self.title = title
            self.ingredients = ingredients
            self.link = link
            self.instructions = None

    def parse(self):
        with open(self.path, "r") as file:
            recipe = file.read()

        return recipe

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



class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        import sqlite3

        self.connection = sqlite3.connect('my_database.db')
        self.cursor = self.connection.cursor()


        self.setWindowTitle("Recipe book")
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)

        self.setWindowIcon(QIcon(ICON_PATH))
        self.start_ui()
        self.show()

    def search_recipes(self, search_text):
        query = """
        SELECT rec_name, ingredients_list, link 
        FROM Cuisines 
        WHERE rec_name LIKE ? OR ingredients_list LIKE ?
        """

        self.cursor.execute(query, (f'%{search_text}%', f'%{search_text}%'))
        results = self.cursor.fetchall()

        return [Recipe(title=rec_name, ingredients=ingredients_list, link=link) for rec_name, ingredients_list, link in results]


    def closeEvent(self, event):
        self.cursor.close()
        self.connection.close()
        event.accept()



    def update_recipe_list(self, recipes):
        while self.sub_layout.count():
            child = self.sub_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if recipes:
            for recipe in recipes:
                recipe_item = QGroupBox()
                layout = QVBoxLayout()

                title_label = QLabel(f"<b>Recipe: {recipe.title}</b>")
                ingredients_label = QLabel(f"Ingredients: {recipe.ingredients}")

                layout.addWidget(title_label)
                layout.addWidget(ingredients_label)

                recipe_item.setLayout(layout)

                self.sub_layout.addWidget(recipe_item)
                ingredients_label = QLabel(f"Ingredients: {recipe.ingredients}")
                ingredients_label.setStyleSheet("color: white")  

        else:
            no_result_label = QLabel("No matching recipes found.")
            self.sub_layout.addWidget(no_result_label)

    def start_ui(self):
        self.main_layout = QVBoxLayout()
        self.sub_layout = QVBoxLayout()

        self.main_widget = QWidget()
        self.sub_widget = QWidget()

        self.search_name_button = QPushButton("Search by Recipe Name")
        self.search_name_button.clicked.connect(self.on_search_name)
        self.main_layout.addWidget(self.search_name_button)

        self.search_ingredient_button = QPushButton("Search by Ingredients")
        self.search_ingredient_button.clicked.connect(self.on_search_ingredient)
        self.main_layout.addWidget(self.search_ingredient_button)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search for a recipe or ingredient...")
        self.search_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.main_layout.addWidget(self.search_bar)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.sub_widget)
        self.main_layout.addWidget(self.scroll)

        self.list_widget = QListWidget()
        self.list_widget.addItems([
            "Pepper", "Garlic", "Onion", "Tomatoes",
            "Chicken", "Beef", "Pork", "Fish", "Eggs",
            "Flour", "Rice", "Pasta", "Cheese", "Bread", "Carrots",
            "Potatoes", "Bell Peppers", "Broccoli", "Spinach", "Mushrooms",
            "Rosemary", "Oregano",
        ])

        self.combo = QComboBox()
        self.combo.addItems([
            "All", "Italian", "Chinese", "Mexican", "Indian",
            "French", "Japanese", "Mediterranean", "Thai",
            "Spanish", "Greek", "Korean", "Vietnamese",
            "American", "Middle Eastern"
        ])

        self.dock_widget = QDockWidget("Search Filters")
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)
        dock_layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(dock_layout)
        self.dock_widget.setWidget(widget)
        dock_layout.addWidget(self.combo)
        dock_layout.addWidget(self.list_widget)
        self.dock_widget.setMaximumWidth(150)

        self.setCentralWidget(self.main_widget)
        self.main_widget.setLayout(self.main_layout)
        self.sub_widget.setLayout(self.sub_layout)

        for i in range(6):
            self.sub_layout.addWidget(recipe_widget(Recipe(PATH_TO_RECIPE)).horizontal_item_widget())

    def on_search_name(self):
        search_text = self.search_bar.text()
        recipes = self.search_recipes_by_name(search_text)
        self.update_recipe_list(recipes)

    def on_search_ingredient(self):
        search_text = self.search_bar.text()
        recipes = self.search_recipes_by_ingredient(search_text)
        self.update_recipe_list(recipes)

    def search_recipes_by_ingredient(self, search_text):
        query = "SELECT rec_name, ingredients_list, link FROM Cuisines WHERE ingredients_list LIKE ?"
        self.cursor.execute(query, (f'%{search_text}%',))
        results = self.cursor.fetchall()
        return [Recipe(title=rec_name, ingredients=ingredients_list, link=link) for rec_name, ingredients_list, link in results]

    def search_recipes_by_name(self, search_text):
        query = "SELECT rec_name, ingredients_list, link FROM Cuisines WHERE rec_name LIKE ?"
        self.cursor.execute(query, (f'%{search_text}%',))
        results = self.cursor.fetchall()

        return [Recipe(title=rec_name, ingredients=ingredients_list, link=link) for rec_name, ingredients_list, link in results]

class recipe_widget:
    def __init__(self, recipe: Recipe, MainWindow: QMainWindow=None):
        self.window = MainWindow
        self.recipe = recipe
        self.item_widget = None

    def get_widget(self):
        return self.widget

    def horizontal_item_widget(self):
        if self.item_widget is not None:
            return self.item_widget

        layout = QHBoxLayout()
        title = QLabel(self.recipe.title)
        icon = QLabel(); icon.setPixmap(QPixmap(ICON_PATH).scaled(80, 80))

        layout.addWidget(icon)
        layout.addWidget(title)

        self.item_widget = QGroupBox()
        self.item_widget.setLayout(layout)
        self.item_widget.mousePressEvent = self.on_item_click

        return self.item_widget

    def on_item_click(self, _event):
        self.window: MainWindow = self.item_widget.window()
        self.recipe_view: QWidget = self.construct_recipe_view()
        self.window.dock_widget.setHidden(True)
        self.window.centralWidget().setParent(None)
        self.window.setCentralWidget(self.recipe_view)

    def construct_recipe_view(self):
        main_widget = QWidget()
        layout = QVBoxLayout()

        instructions = QLabel(self.recipe.instructions)
        instructions.setWordWrap(True)
        instructions.setAlignment(Qt.AlignTop)

        push_button = QPushButton("<-- Back")
        push_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        push_button.clicked.connect(self.on_back_click)

        main_widget.setLayout(layout)
        layout.addWidget(push_button)
        layout.addWidget(QLabel(self.recipe.title))
        layout.addWidget(instructions)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))

        return main_widget

    def on_back_click(self):
        self.window.dock_widget.setHidden(False)
        self.window.restart_ui()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()

    app.exec()
