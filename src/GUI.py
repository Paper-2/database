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
    """
    MainWindow is a class for the Recipe Book GUI application.
    """
    def __init__(self, data: Database):
        super(MainWindow, self).__init__()
        self.data = data
        self.recipes = []  # List to store recipe widgets
        self.favorites = []  # List to store favorite recipes
        self.setWindowTitle("Recipe book")
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)

        self.setWindowIcon(QIcon(ICON_PATH))
        self.__start_ui()
        self.show()
    def __start_ui(self):
        self.main_layout = QVBoxLayout()
        self.sub_layout = QVBoxLayout()
        self.favorites_layout = QVBoxLayout()  # Layout for favorites tab

        self.main_widget = QWidget()
        self.sub_widget = QWidget()
        self.favorites_widget = QWidget()  # Widget for favorites tab

        # Add a button to open the favorites window
        self.favorites_button = QPushButton("Show Favorites")
        self.favorites_button.clicked.connect(self.open_favorites_window)
        self.main_layout.addWidget(self.favorites_button)

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

        # Create QTabWidget for ingredient groups and favorites
        self.tab_widget = QTabWidget()

        # Create ingredient lists by category
        self.protein_list = QListWidget()
        self.carb_list = QListWidget()
        self.veggie_list = QListWidget()
        self.seasoning_list = QListWidget()
        self.oil_list = QListWidget()
        self.dairy_list = QListWidget()

        # Populate each list
        self.__populate_ingredient_lists()

        # Add each food group list to the corresponding tab
        self.tab_widget.addTab(self.protein_list, "Proteins")
        self.tab_widget.addTab(self.carb_list, "Carbs/Grains")
        self.tab_widget.addTab(self.veggie_list, "Vegetables")
        self.tab_widget.addTab(self.seasoning_list, "Seasonings/Spices")
        self.tab_widget.addTab(self.oil_list, "Oils")
        self.tab_widget.addTab(self.dairy_list, "Dairy")

        # Create Favorites tab
        self.tab_widget.addTab(self.favorites_widget, "Favorites")  # Add favorites tab

        # Set layout for favorites widget
        self.favorites_widget.setLayout(self.favorites_layout)

        self.dock_widget.setAllowedAreas(Qt.RightDockWidgetArea)
        dock_layout = QVBoxLayout()
        widget = QWidget()
        widget.setLayout(dock_layout)
        self.dock_widget.setWidget(widget)
        dock_layout.addWidget(self.tab_widget)

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
    def __populate_ingredient_lists(self):
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
        dock_layout.addWidget(self.tab_widget)

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

        # Add select cuisine button
        self.combo = QComboBox()
        self.combo.addItems(
            ["All", "Italian", "Mexican", "Indian", "Japanese", "German"]
        )
        #fixed the select cuisine box, we had to add widget and connect it to on search
        self.combo.currentTextChanged.connect(self.__on_search)
        self.main_layout.addWidget(self.combo)

        # Connect itemChanged for each ingredient list
        self.protein_list.itemChanged.connect(self.__on_search)
        self.carb_list.itemChanged.connect(self.__on_search)
        self.veggie_list.itemChanged.connect(self.__on_search)
        self.seasoning_list.itemChanged.connect(self.__on_search)
        self.oil_list.itemChanged.connect(self.__on_search)
        self.dairy_list.itemChanged.connect(self.__on_search)

        # Initially load all recipes with MainWindow instance
        self.__add_item(
            [recipe_widget(Recipe(recipe), self) for recipe in self.data.get_all_recipes()]
        )

    def _populate_ingredient_lists(self):
        # Proteins
        proteins = ["Chicken", "Beef", "Pork", "Tuna", "Eggs", "Veal", "Chuck Roast"]
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
        seasonings = ["Salt", "Pepper", "Garlic", "Rosemary", "Oregano", "Cilantro", "Cumin", "Ginger", "Cayenne Pepper", "Turmeric", "Sugar"]
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
        dairy = ["Cheese", "Mozzarella Cheese", "Parmesan Cheese", "Mexican Cheese"]
        for item_name in dairy:
            item = QListWidgetItem(item_name)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.dairy_list.addItem(item)

    def __add_item(self, recipe_widgets):
        """Add recipe widgets to the main layout."""
        for widget in recipe_widgets:
            self.recipes.append(widget)  # Use append instead of add
            self.sub_layout.addWidget(widget.horizontal_item_widget())

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
        # Combine all selected ingredients from all lists
        ingredients = ""

        # Loop through each food group and collect checked ingredients
        for list_widget in [self.protein_list, self.carb_list, self.veggie_list, self.seasoning_list, self.oil_list, self.dairy_list]:
            for index in range(list_widget.count()):
                item: QListWidgetItem = list_widget.item(index)
                if item.checkState() != Qt.Unchecked:
                    ingredients += f"%{item.text()}% "

        # Handle cuisine combo selection

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
            recipe_widgets.append(recipe_widget(Recipe(recipe), self))
        self.__add_item(recipe_widgets)

        self.__remove_items_based_on_search(recipes_to_keep)

    def add_to_favorites(self, recipe_widget):
        """Add a recipe to the favorites list and update the favorites tab."""
        if recipe_widget.title not in self.favorites:
            self.favorites.append(recipe_widget.title)
            self.favorites_layout.addWidget(recipe_widget.horizontal_item_widget())  # Add to favorites layout
            if hasattr(self, 'favorites_window'):
                self.favorites_window.update_favorites_list()  # Update the favorites window if open

    def remove_from_favorites(self, recipe_widget):
        """Remove a recipe from the favorites list and update the favorites tab."""
        if recipe_widget.title in self.favorites:
            self.favorites.remove(recipe_widget.title)
            # Remove from favorites layout (you may need to implement a method to find and remove the widget)
            for i in range(self.favorites_layout.count()):
                widget = self.favorites_layout.itemAt(i).widget()
                if widget and widget.findChild(QLabel, "title").text() == recipe_widget.title:
                    widget.deleteLater()
                    break

    def open_favorites_window(self):
        """Open the favorites window."""
        self.favorites_window = FavoritesWindow(self.favorites, self)  # Pass self to FavoritesWindow
        self.favorites_window.exec_()


# You would also need to update the 'recipe_widget' class and other logic as needed.
class recipe_widget:
    def __init__(self, recipe, main_window: MainWindow = None):
        self.window = main_window  # Store reference to MainWindow
        self.recipe = recipe
        self.title = self.recipe.title
        self.item_widget = None
        self.favorite_button = None  # Add a button for favorites
        self.is_favorite = False  # Track favorite status

        # Add this recipe widget to the main window's recipe list
        if self.window:
            self.window.recipes.append(self)

    def horizontal_item_widget(self):
        if self.item_widget is not None:
            return self.item_widget

        layout = QHBoxLayout()
        title = QLabel(self.recipe.title)
        title.setObjectName("title")
        icon = QLabel()
        icon.setPixmap(QPixmap(ICON_PATH).scaled(80, 80))

        # Create the favorite button
        self.favorite_button = QPushButton("Favorite")
        self.favorite_button.clicked.connect(self.toggle_favorite)  # Connect to toggle function

        # Add widgets to layout
        layout.addWidget(icon)
        layout.addWidget(title)
        layout.addWidget(self.favorite_button)  # Add the favorite button to the layout

        # Create a group box to contain the recipe item
        self.item_widget = QGroupBox()
        self.item_widget.setLayout(layout)

        # Connect the item click to open a detailed view of the recipe
        self.item_widget.mousePressEvent = self.on_item_click

        return self.item_widget

    def toggle_favorite(self):
        # Toggle favorite status
        self.is_favorite = not self.is_favorite  # Toggle the favorite status
        if self.is_favorite:
            self.favorite_button.setText("Unfavorite")  # Change button text to "Unfavorite"
            print(f"Favorited {self.title}")  # Logic to mark as favorite in the database can be added here
            self.window.add_to_favorites(self)  # Add to favorites in MainWindow
        else:
            self.favorite_button.setText("Favorite")  # Change button text to "Favorite"
            print(f"Unfavorited {self.title}")  # Logic to unmark as favorite in the database can be added here

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
        Triggers the `on_back_click` method when clicked.
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
        """
        Handles the event when the back button is clicked.
        This method restores the original UI layout by making the dock widget visible
        and resetting the central widget to the main widget.
        """
        
        # Restore the original UI layout and make the dock widget visible again
        self.window.dock_widget.setHidden(False)  # Show the dock widget
        self.window.setCentralWidget(self.window.main_widget)  # Reset the central widget


class FavoritesWindow(QDialog):
    def __init__(self, favorites, main_window: MainWindow, parent=None):
        super(FavoritesWindow, self).__init__(parent)
        self.favorites = favorites  # List of favorite recipes
        self.main_window = main_window  # Reference to the main window
        self.setWindowTitle("Favorite Recipes")
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.favorites_list_widget = QListWidget()
        self.layout.addWidget(self.favorites_list_widget)

        self.update_favorites_list()

        # Connect item click to open the recipe
        self.favorites_list_widget.itemDoubleClicked.connect(self.open_recipe)

    def update_favorites_list(self):
        """Update the favorites list display."""
        self.favorites_list_widget.clear()  # Clear the current list
        # Add each favorite recipe to the list widget
        for recipe in self.favorites:
            self.favorites_list_widget.addItem(recipe)

    def open_recipe(self, item):
        """Open the selected recipe in the main window."""
        recipe_name = item.text()
        # Find the recipe in the main window's recipe list and open it
        for recipe_widget in self.main_window.recipes:
            if recipe_widget.title == recipe_name:
                self.main_window.setCentralWidget(recipe_widget.horizontal_item_widget())
                break


if __name__ == "__main__":
    ...