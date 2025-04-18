import sys
import subprocess
import PyQt5.QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QComboBox, QVBoxLayout, QLabel
from PyQt5 import Qt


# Create a class for the opening sequence of the program.
class MapSearchWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lost Grenadiers" + " Hillside Hall 3rd floor")
        self.resize(800, 600)

        # Create a label to display the map background image from images folder directory.
        self.mapLabel = PyQt5.QtWidgets.QLabel(self)
        self.pixmap = QPixmap("../Images/PNG/Hillside3 map.png")
        self.mapLabel.setPixmap(self.pixmap)
        self.mapLabel.setScaledContents(True)
        self.mapLabel.setGeometry(0, 0, self.width(), self.height())

        # Create the search bar (QLineEdit) in the top left corner.
        self.searchBar = PyQt5.QtWidgets.QLineEdit(self)
        self.searchBar.setPlaceholderText("Search for a class")
        self.searchBar.setFixedWidth(300)
        self.searchBar.move(20, 20)

        # Button to change floors
        self.cvButton = PyQt5.QtWidgets.QPushButton("1st Floor", self)
        self.cvButton.move(20, 50)
        self.cvButton.clicked.connect(self.run_hh)

        # Button to change floors
        self.cvButton = PyQt5.QtWidgets.QPushButton("2nd Floor", self)
        self.cvButton.move(20, 80)
        self.cvButton.clicked.connect(self.run_hh2)

        # Button to change floors
        self.cvButton = PyQt5.QtWidgets.QPushButton("4th Floor", self)
        self.cvButton.move(20, 110)
        self.cvButton.clicked.connect(self.run_hh4)

        # Button to change floors
        self.cvButton = PyQt5.QtWidgets.QPushButton("5th Floor", self)
        self.cvButton.move(20, 140)
        self.cvButton.clicked.connect(self.run_hh5)

        # Optional: Create a search button next to the search bar.
        self.searchButton = PyQt5.QtWidgets.QPushButton("Search", self)
        self.searchButton.move(330, 20)

        # Connect signals to perform search when the user hits Enter or clicks the button.
        self.searchBar.returnPressed.connect(self.performSearch)
        self.searchButton.clicked.connect(self.performSearch)

    # Helper function for floor change
    def run_hh(self):
        subprocess.run(['python', 'HillsideUI.py'])
        sys.exit(app.exec_())

    def run_hh2(self):
        subprocess.run(['python', 'Hillside2UI.py'])
        sys.exit(app.exec_())

    def run_hh4(self):
        subprocess.run(['python', 'Hillside4UI.py'])
        sys.exit(app.exec_())

    def run_hh5(self):
        subprocess.run(['python', 'Hillside5UI.py'])
        sys.exit(app.exec_())

    def resizeEvent(self, event):

        # Ensure the map image always fills the window.
        self.mapLabel.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def performSearch(self):

        # Retrieve the user's query, search the file, and display results.
        query = self.searchBar.text().strip()
        if not query:
            PyQt5.QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a search query.")
            return
        results = self.searchClass(query)
        if results:

            # If multiple matches are found, join them into a single string.
            result_str = "\n".join(results)
            PyQt5.QtWidgets.QMessageBox.information(self, "Search Results", f"Room Number(s):\n{result_str}")
        else:
            PyQt5.QtWidgets.QMessageBox.information(self, "Search Results", "No matching class found.")

    def searchClass(self, query):
        results = []
        # Try catch exception opening the data list with read-only privilege.
        try:
            with open("../Database Sources/Course list.txt", "r") as file:
                for line in file:

                    # Split the line into parts (expecting three parts per line).
                    parts = line.strip().split(',')
                    if len(parts) < 3:
                        continue

                    # Skip any improperly formatted lines.
                    class_name = parts[0].strip()
                    class_number = parts[1].strip()
                    building_number = parts[2].strip()

                    # Perform a case-insensitive check if the query is in the class name or number.
                    if (query.lower() in class_name.lower() or
                            query.lower() in class_number.lower()):
                        results.append(building_number)
        except Exception as e:

            # If there's an error (for example, file not found), return an error message.
            results.append("Error reading file: " + str(e))
        return results


# Enable the program to close and exit.
if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = MapSearchWindow()
    window.show()
    sys.exit(app.exec_())