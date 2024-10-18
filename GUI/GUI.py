import sys
import os
from PySide6.QtCore import Qt

from PySide6.QtGui import QColor, QPalette, QPixmap, QIcon

from PySide6.QtWidgets import *
from PySide6.QtWidgets import QWidget

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
class Recipe:
    def __init__(self, path):
        self.path = path
        self.recipe = self.parse()

        self.title, self.ingredients, self.instructions = self.get_recipe_info()

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
        
        #self.search_bar configuration
        self.search_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        
        self.scroll = QScrollArea()

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
        
        
        for i in range(10):
            self.sub_layout.addWidget(recipe_widget(Recipe(PATH_TO_RECIPE)).horizontal_item_widget())
            
        

               
        r"""
        self.layout = QVBoxLayout()
        self.widget = QWidget()
        self.search_label = QLabel("Search:")
        self.search = QLineEdit()
        self.layout.addWidget(self.search_label)
        self.scroll = QScrollArea()
        self.search = QLineEdit()
        
        
        self.layout.addWidget(self.search)
        self.search  
        for path in range(0,15):

            self.add_row(row_button(Recipe(os.getcwd() + "\mashed_potatoes.txt"), self).get_row())
        self.widget.setLayout(self.layout)
        
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
    
        print(len(self.children()))
        self.setCentralWidget(self.scroll)"""
        
        
        
    def add_row(self, row: QGroupBox):
        self.layout.addWidget(row)
        
class recipe_widget(QWidget):
    def __init__(self, recipe: Recipe):
        super().__init__()
        
        self.recipe = recipe
        self.item_widget = None
        
    def get_widget(self):
        return self.widget
    
    def horizontal_item_widget(self,):

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
    
    
    def on_item_click(self, event):
        
        instructions = self.construct_instructions_view()
        self.item_widget.window().setCentralWidget(instructions) 

    def construct_instructions_view(self):
        instructions = QLabel(self.recipe.instructions)

        font = instructions.font()
        font.setPointSize(int(font.pointSize() * 1.2))
        instructions.setFont(font)
        return instructions       
class row_button:
    def __init__(self, recipe: Recipe, window):
        

        self.groupBox = QGroupBox()
        self.layout = QHBoxLayout()
        self.recipe_name = QLabel(recipe.title)
        
        self.ingredients = recipe.ingredients
        # Create a QLabel to hold the icon
        self.icon = QLabel()
        
        # Load the pixmap from the icon file
        pixmap = QPixmap(ICON_PATH).scaled(80, 80)
        
        # Set the pixmap to the QLabel
        self.icon.setPixmap(pixmap)
        
        
        self.layout.addWidget(self.icon)
        self.layout.addWidget(self.recipe_name)
        
        self.groupBox.setLayout(self.layout)
        
        self.groupBox.mousePressEvent = self.on_click
    
    def get_row(self):
        return self.groupBox
        
    def on_click(self, event):
        instructions = QLabel(self.recipe_instruction)

        font = instructions.font()
        font.setPointSize(int(font.pointSize() * 1.2))
        instructions.setFont(font)
        self.window.setCentralWidget(instructions)
        
        print(self.window.children())
        
app = QApplication(sys.argv)

window = MainWindow()

app.exec()