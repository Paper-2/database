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
        

#this class should be moved to another file that is not GUI.py
class Recipe_gui_proto:
    def __init__(self, path):
        self.path = path
        self.recipe = self.parse()

        self.title, self.ingredients, self.link = self.get_recipe_info()

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

        # Initialize the main window with title, size constraints, and icon
        self.setWindowTitle("Recipe book")
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)
        
        self.setWindowIcon(QIcon(ICON_PATH))
        self.start_ui()
        self.show()


    def start_ui(self):
       
        self.main_layout = QVBoxLayout()
        self.sub_layout = QVBoxLayout()
        

        self.main_widget = QWidget()
        self.sub_widget = QWidget()

        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search for a recipe: (e.g. title:mashed potatoes ingredients:potatoes)")
        self.search_bar.textChanged.connect(self.on_search)
        #self.search_bar configuration
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
        combo = QComboBox()
        combo.addItems([
            "All", "Italian", "Mexican", "Indian", 
            "Japanese", "Germna"
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
        #self.scroll configuration
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.sub_widget)
        
        self.setCentralWidget(self.main_widget)
        
        #makes main_widget use the main_layout and then adds it to the window screen
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
        
    # this function should be overridden.
    def search(self):
        print(self.search_bar.text())

    def on_search(self):
        # todo: implement search functionality
        self.search()
        pass

        
class recipe_widget:
    def __init__(self, recipe: Recipe_gui_proto, MainWindow: QMainWindow=None):
        
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
        # Check if the item widget already exists
        if self.item_widget is not None:
            return self.item_widget
        
        # Creates new widgets (note: layout is not a widget)
        layout = QHBoxLayout()
        title = QLabel(self.recipe.title)
        icon = QLabel(); icon.setPixmap(QPixmap(ICON_PATH).scaled(80, 80))
        
        # Add the widgets to the layout
        layout.addWidget(icon)
        layout.addWidget(title)
        
        # Set the layout to a QGroupBox
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
        
    def start(self):
        
        app = QApplication(sys.argv)

        window = MainWindow()
        
        app.exec()
                
        

        