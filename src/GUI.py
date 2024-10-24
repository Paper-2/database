import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette, QPixmap, QIcon
from PySide6.QtWidgets import *

ICON_PATH: str = os.path.join(os.getcwd(), "recipe_database_icon.png")
PATH_TO_RECIPE: str = os.path.join(os.getcwd(), "mashed_potatoes.txt")

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


    def update_recipe_list(self, recipes):
        for i in reversed(range(self.sub_layout.count())):
            widget = self.sub_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        if recipes:
            for rec_name, ingredients, link in recipes:
                recipe_item = QWidget()
                layout = QHBoxLayout()
                title = QLabel(f"Recipe: {rec_name}")
                ingredients_label = QLabel(f"Ingredients: {ingredients}")
                layout.addWidget(title)
                layout.addWidget(ingredients_label)
                recipe_item.setLayout(layout)
                self.sub_layout.addWidget(recipe_item)
        else:
            no_result_label = QLabel("No matching recipes found.")
            self.sub_layout.addWidget(no_result_label)

    def start_ui(self):

        self.main_layout = QVBoxLayout()
        self.sub_layout = QVBoxLayout()


        self.main_widget = QWidget()
        self.sub_widget = QWidget()

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.on_search)
        self.main_layout.addWidget(self.search_button)


        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search for a recipe: (e.g. mashed potatoes )")
        self.search_bar.textChanged.connect(self.on_search)
        self.search_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.scroll = QScrollArea()

        self.dock_widget = QDockWidget("Search Filters")
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)

        self.list_widget = QListWidget()
        self.list_widget.addItems([
            "Pepper", "Garlic", "Onion", "Tomatoes",
            "Chicken", "Beef", "Pork", "Fish", "Eggs",
            "Flour", "Rice", "Pasta", "Cheese", "Bread", "Carrots",
            "Potatoes", "Bell Peppers", "Broccoli", "Spinach", "Mushrooms",
            "Rosemary", "Oregano",
        ])
        
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
        
        combo = QComboBox()
        combo.addItems([
            "All", "Italian", "Mexican", "Indian", 
            "Japanese", "German"
        ])
        
        self.function()
        

        self.dock_widget.setAllowedAreas(Qt.RightDockWidgetArea)
        dock_layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(dock_layout)
        self.dock_widget.setWidget(widget)
        dock_layout.addWidget(combo)
        dock_layout.addWidget(self.list_widget)
        self.dock_widget.setMaximumWidth(150)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.sub_widget)

        self.setCentralWidget(self.main_widget)

        self.main_widget.setLayout(self.main_layout)
        self.sub_widget.setLayout(self.sub_layout)

        self.main_layout.addWidget(self.search_bar)
        self.main_layout.addWidget(self.scroll)
        
    def add_item(self, recipe):
        self.sub_layout.addWidget(recipe)

    def function(self):
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            
    def restart_ui(self):
        self.setCentralWidget(self.main_widget)

    def search(self):
        print(self.search_bar.text())

    def on_search(self):
        search_text = self.search_bar.text()
        recipes = self.search_recipes(search_text)

        while self.sub_layout.count():
            child = self.sub_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for recipe in recipes:
            self.sub_layout.addWidget(recipe_widget(recipe).horizontal_item_widget())

    @staticmethod
    def start():
        app = QApplication(sys.argv)
        window = MainWindow()
        app.exec()


class recipe_widget:
    def __init__(self, recipe, MainWindow: QMainWindow=None):
        self.window = MainWindow
        self.recipe = recipe
        self.item_widget = None

    def get_widget(self):
        return self.widget

    def horizontal_item_widget(self):

        """
        Creates and returns a horizontal item widget for displaying a recipe.
        This method checks if the item widget already exists. If it does, it returns the existing widget.
        Otherwise, it creates a new horizontal layout containing an icon and a title label,
        sets this layout to a QGroupBox, and returns the newly created widget.
        Returns:
            QGroupBox: The horizontal item widget containing the recipe's icon and title.
        """
        if self.item_widget is not None:
            return self.item_widget

        layout = QHBoxLayout()
        title = QLabel(self.recipe.title)
        icon = QLabel(); icon.setPixmap(QPixmap(ICON_PATH).scaled(80, 80))
        favorite_button = QPushButton("Favorite")
        favorite_button.clicked.connect(self.on_favorite_toggle)


        layout.addWidget(icon)
        layout.addWidget(title)
        layout.addWidget(favorite_button) 

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
        push_button.setBaseSize(100, 100)
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
        
    def on_favorite_toggle(self):
        #TODO: Implement this method to toggle the favorite state of the recipe.
        ...
        

if __name__ == '__main__':
    MainWindow.start()