import unittest
from GUI import GUI_module

class GUITest(unittest.TestCase):
    def setUp(self):
        self.gui = GUI()

    def test_something(self):
        # Write your test case here
        pass

if __name__ == '__main__':
    unittest.main()