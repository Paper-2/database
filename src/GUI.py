import sys
import os
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import *

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

        # Search buttons
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

        # Create QTabWidget for ingredient groups
        self.tab_widget = QTabWidget()

        # Create ingredient lists by category
        self.protein_list = QListWidget()
        self.carb_list = QListWidget()
        self.veggie_list = QListWidget()
        self.seasoning_list = QListWidget()
        self.oil_list = QListWidget()
        self.dairy_list = QListWidget()

        # Populate each list
        self._populate_ingredient_lists()

        # Add each food group list to the corresponding tab
        self.tab_widget.addTab(self.protein_list, "Proteins")
        self.tab_widget.addTab(self.carb_list, "Carbs/Grains")
        self.tab_widget.addTab(self.veggie_list, "Vegetables")
        self.tab_widget.addTab(self.seasoning_list, "Seasonings/Spices")
        self.tab_widget.addTab(self.oil_list, "Oils")
        self.tab_widget.addTab(self.dairy_list, "Dairy")

        self.dock_widget.setAllowedAreas(Qt.RightDockWidgetArea)
        dock_layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(dock_layout)
        self.dock_widget.setWidget(widget)
        dock_layout.addWidget(self.tab_widget)

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

        # Connect itemChanged for each ingredient list
        self.protein_list.itemChanged.connect(self.__on_search)
        self.carb_list.itemChanged.connect(self.__on_search)
        self.veggie_list.itemChanged.connect(self.__on_search)
        self.seasoning_list.itemChanged.connect(self.__on_search)
        self.oil_list.itemChanged.connect(self.__on_search)
        self.dairy_list.itemChanged.connect(self.__on_search)

        # Initially load all recipes
        self.__add_item(
            [recipe_widget(Recipe(recipe)) for recipe in self.data.get_all_recipes()]
        )
#made a ingredients function that categorizes all of the ingredients in the available recipies to choose from
    def _populate_ingredient_lists(self):
        # Proteins
        proteins = ["Chicken", "Beef", "Pork", "Fish", "Eggs", "Veal", "Chuck Roast"]
        for protein in proteins:
            item = QListWidgetItem(protein)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.protein_list.addItem(item)

        # Carbs/Grains
        carbs = ["Flour", "Rice", "Pasta", "Bread", "Tortillas"]
        for carb in carbs:
            item = QListWidgetItem(carb)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.carb_list.addItem(item)

        # Vegetables
        veggies = ["Onion", "Tomatoes", "Carrot", "Potatoes", "Serrano Peppers", "Green Chile Peppers", "Cilantro"]
        for veggie in veggies:
            item = QListWidgetItem(veggie)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.veggie_list.addItem(item)

        # Seasonings/Spices
        seasonings = ["Salt", "Pepper", "Garlic", "Rosemary", "Oregano", "Cilantro", "Cumin", "Ginger", "Cayenne Pepper", "Tumeric", "Sugar"]
        for seasoning in seasonings:
            item = QListWidgetItem(seasoning)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.seasoning_list.addItem(item)

        # Oils
        oils = ["Olive Oil", "Vegetable Oil", "Sesame Oil"]
        for oil in oils:
            item = QListWidgetItem(oil)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.oil_list.addItem(item)

        # Dairy
        dairy = ["Cheese", "Mozzarella Cheese", "Parmesan Cheese", "Mexican cheese", "co"]
        for item_name in dairy:
            item = QListWidgetItem(item_name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.dairy_list.addItem(item)

        # Connect itemChanged signal for each list to the search function
        self.protein_list.itemChanged.connect(self.__on_search)
        self.carb_list.itemChanged.connect(self.__on_search)
        self.veggie_list.itemChanged.connect(self.__on_search)
        self.seasoning_list.itemChanged.connect(self.__on_search)
        self.oil_list.itemChanged.connect(self.__on_search)
        self.dairy_list.itemChanged.connect(self.__on_search)


        # Add each food group list to the corresponding tab
        self.tab_widget.addTab(self.protein_list, "Proteins")
        self.tab_widget.addTab(self.carb_list, "Carbs/Grains")
        self.tab_widget.addTab(self.veggie_list, "Vegetables")
        self.tab_widget.addTab(self.seasoning_list, "Seasonings/Spices")
        self.tab_widget.addTab(self.oil_list, "Oils")
        self.tab_widget.addTab(self.dairy_list, "Dairy")

        # Add the tab widget to the main layout
        self.main_layout.addWidget(self.tab_widget)

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
        # Combine all selected ingredients from all lists
        ingredients = ""

        # Loop through each food group and collect checked ingredients
        for list_widget in [self.protein_list, self.carb_list, self.veggie_list, self.seasoning_list, self.oil_list, self.dairy_list]:
            for index in range(list_widget.count()):
                item: QListWidgetItem = list_widget.item(index)
                if item.checkState() != Qt.Unchecked:
                    ingredients += f"%{item.text()}% "

        # Handle cuisine combo selection
        if self.combo.currentText() == "All":
            combo = ""
        else:
            combo = self.combo.currentText()

        # Perform search in the database
        return self.data.search_recipes(self.search_bar.text(), ingredients.strip(), combo)

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
        triggers the on_back_click method when clicked.
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

#fixed back to button to go back to the main_widget
    def on_back_click(self):
        # Restore the original UI layout and make the dock widget visible again
        self.window.dock_widget.setHidden(False)  # Show the dock widget
        self.window.setCentralWidget(self.window.main_widget)  # Reset the central widget

    def on_favorite_toggle(self):
        # TODO: Implement this method to toggle the favorite state of the recipe.
        ...

if __name__ == "__main__":
    ...
