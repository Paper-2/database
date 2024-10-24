import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette, QPixmap, QIcon
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QListWidgetItem, QWidget

from database import Database
from utils import Recipe

ICON_PATH: str = os.path.join(os.getcwd(), "recipe_database_icon.png")
PATH_TO_RECIPE: str = os.path.join(os.getcwd(), "mashed_potatoes.txt")


class MainWindow(QMainWindow):
    def __init__(self, data: Database):
        super(MainWindow, self).__init__()
        self.data = data
        self.recipes = set()
        self.setWindowTitle("Recipe book")
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)

        self.setWindowIcon(QIcon(ICON_PATH))
        self.__start_ui()
        self.show()

    def __start_ui(self):
        self.main_layout = QVBoxLayout()
        self.sub_layout = QVBoxLayout()

        self.main_widget = QWidget()
        self.sub_widget = QWidget()

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.__on_search)
        self.main_layout.addWidget(self.search_button)

        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText(
            "Search for a recipe: (e.g. mashed potatoes )"
        )
        self.search_bar.textChanged.connect(self.__on_search)
        self.search_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.scroll = QScrollArea()

        self.dock_widget = QDockWidget("Search Filters")
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_widget)

        self.list_widget = QListWidget()
        self.list_widget.addItems(
            [
                "Pepper",
                "Garlic",
                "Onion",
                "Tomatoes",
                "Chicken",
                "Beef",
                "Pork",
                "Fish",
                "Eggs",
                "Flour",
                "Rice",
                "Pasta",
                "Cheese",
                "Bread",
                "Carrots",
                "Potatoes",
                "Bell Peppers",
                "Broccoli",
                "Spinach",
                "Mushrooms",
                "Rosemary",
                "Oregano",
            ]
        )
        self.list_widget.itemChanged.connect(self.__on_search)
        for index in range(self.list_widget.count()):
            item: QListWidgetItem = self.list_widget.item(index)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)

        self.combo = QComboBox()
        self.combo.addItems(
            ["All", "Italian", "Mexican", "Indian", "Japanese", "German"]
        )

        self.combo.currentTextChanged.connect(self.__on_search)

        self.dock_widget.setAllowedAreas(Qt.RightDockWidgetArea)
        dock_layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(dock_layout)
        self.dock_widget.setWidget(widget)
        dock_layout.addWidget(self.combo)
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

        self.__add_item(
            [recipe_widget(Recipe(recipe)) for recipe in self.data.get_all_recipes()]
        )

    def __add_item(self, *recipe: "recipe_widget"):
        recipe = recipe[0]
        while recipe:
            if recipe[0].title in self.recipes:
                print("skipping duplicate")
                recipe.pop(0)
                continue

            self.recipes.add(recipe[0].title)
            self.sub_layout.addWidget(recipe[0].horizontal_item_widget())
            recipe.pop(0)

    def __remove_items_based_on_search(self, to_keep: set):
        allowed_recipes = to_keep.intersection(self.recipes)
        self.recipes = allowed_recipes
        print(self.sub_layout.count())
        for i in reversed(range(self.sub_layout.count())):
            widget = self.sub_layout.itemAt(i).widget()
            if widget:
                title_label = widget.findChild(QLabel, "title")
            if title_label and title_label.text() not in allowed_recipes:
                widget.deleteLater()

    def __restart_ui(self):
        self.setCentralWidget(self.main_widget)

    def __search(self):
        ingredients = ""
        for index in range(self.list_widget.count()):
            item: QListWidgetItem = self.list_widget.item(index)
            if item.checkState() != Qt.Unchecked:
                ingredients += f"%{item.text()}%"
        print()
        if self.combo.currentText() == "All":
            combo = ""
        else:
            combo = self.combo.currentText()
        print(self.search_bar.text() == "")
        print(ingredients == "")
        return self.data.search_recipes(self.search_bar.text(), ingredients, combo)

    def __on_search(self):
        recipes = self.__search()
        print(len(recipes))
        recipes_to_keep = set()
        for recipe in recipes:
            recipes_to_keep.add(recipe[1])

        recipe_widgets = []

        for recipe in recipes:
            if len(recipe) <= 3:
                print(recipe)
            recipe_widgets.append(recipe_widget(Recipe(recipe)))
        self.__add_item(recipe_widgets)

        self.__remove_items_based_on_search(recipes_to_keep)


class recipe_widget:
    def __init__(self, recipe, MainWindow: QMainWindow = None):
        self.window = MainWindow
        self.recipe = recipe
        self.title = self.recipe.title
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
        title.setObjectName("title")
        icon = QLabel()
        icon.setPixmap(QPixmap(ICON_PATH).scaled(80, 80))
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
        """
        Handles the event when an item is clicked in the GUI.
        This method performs the following actions:
        1. Retrieves the main window instance from the item widget.
        2. Constructs a new recipe view widget.
        3. Hides the dock widget in the main window.
        4. Removes the current central widget from the main window.
        5. Sets the newly constructed recipe view as the central widget of the main window.
        """
        
        self.window: MainWindow = self.item_widget.window()

        self.recipe_view: QWidget = self.construct_recipe_view()
        self.window.dock_widget.setHidden(True)
        self.window.centralWidget().setParent(None)
        self.window.setCentralWidget(self.recipe_view)

    def construct_recipe_view(self):
        """
        Constructs the recipe view widget.
        triggers the `on_back_click` method when clicked. 
        Returns:
            QWidget: The main widget containing the recipe view.
        """
        # Create the main widget and layout for the recipe view
        main_widget = QWidget()
        layout = QVBoxLayout()

        # Create and configure the instructions label
        instructions = QLabel(self.recipe.instructions)
        instructions.setWordWrap(True)
        instructions.setAlignment(Qt.AlignTop)

        # Create and configure the back button
        push_button = QPushButton("<-- Back")
        push_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        push_button.setBaseSize(100, 100)
        push_button.clicked.connect(self.on_back_click)

        # Set the layout for the main widget
        main_widget.setLayout(layout)

        # Add widgets to the layout
        layout.addWidget(push_button)
        layout.addWidget(QLabel(self.recipe.title))
        layout.addWidget(instructions)
        layout.addSpacerItem(
            QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)
        )

        return main_widget

    def on_back_click(self):
        self.window.dock_widget.setHidden(False)
        self.window.__restart_ui()

    def on_favorite_toggle(self):
        # TODO: Implement this method to toggle the favorite state of the recipe.
        ...


if __name__ == "__main__":
    ...
