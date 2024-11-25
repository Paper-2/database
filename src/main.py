import sys
from GUI import *
from PySide6.QtWidgets import *
from database import Database
import os

def main():
    app = QApplication(sys.argv)

    data = Database()
    window = MainWindow(data)
    app.exec()




if __name__ == '__main__':
    main()