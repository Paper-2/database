import sys
import os
from PySide6.QtCore import Qt

from PySide6.QtGui import QColor, QPalette, QPixmap, QIcon

from PySide6.QtWidgets import *

ICON_PATH: str = os.path.join(os.getcwd(), "GUI", "recipe_database_icon.png")

class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        
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

        self.setWindowTitle("Recipe book")
        self.setMinimumHeight(400)
        self.setMinimumWidth(600)
        self.setMaximumSize(400, 600)
        self.setWindowIcon(QIcon(ICON_PATH))
        self.start_ui()


    def start_ui(self):
       
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
        self.setCentralWidget(self.scroll)
        
        self.show()
        
    def add_row(self, row: QGroupBox):
        self.layout.addWidget(row)
        
class row_button:
    def __init__(self, recipe: Recipe, window):
        
        self.window: MainWindow = window
        self.groupBox = QGroupBox()
        self.layout = QHBoxLayout()
        self.recipe_name = QLabel(recipe.title)
        self.recipe_instruction = recipe.instructions
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