import os.path
import os
import sys
import PyQt5.QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import subprocess


# helper functions for local map calls

def run_lf():
    subprocess.run(['python', 'LifeScienceUI.py'])

def run_ps():
    subprocess.run(['python', 'PhysicalScienceUI.py'])

def run_cv():
    subprocess.run(['python', 'CrestviewUI.py'])

def run_hh():
    subprocess.run(['python', 'HillsideUI.py'])

def run_kv():
    subprocess.run(['python', 'KnobviewUI.py'])

class MapSearchWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.marker = None
        self.setWindowTitle("Lost Grenadiers" + " Campus Map" )
        self.setFixedSize(1000, 800)

        # Create a label to display the map background image
        self.mapLabel = PyQt5.QtWidgets.QLabel(self)
        self.pixmap = QPixmap("../Images/PNG/IUS Campus Map.png")
        self.mapLabel.setPixmap(self.pixmap)
        self.mapLabel.setScaledContents(True)
        self.mapLabel.setGeometry(0, 0, self.width(), self.height())

        # pixel coordinates for the buildings
        self.buildingCoordinates = {
            "LF": (560, 225),
            "PS": (580, 290),
            "CV": (580, 170),
            "TB": (-100, -100),
            "KV": (840, 160),
            "HH": (640, 120)
        }
        #keeps track of old blip markers so they can be cleared
        self.markerLabels = []

        # Create the search bar (QLineEdit) in the top left corner
        self.searchBar = PyQt5.QtWidgets.QLineEdit(self)
        self.searchBar.setPlaceholderText("Search for a class")
        self.searchBar.setFixedWidth(300)
        self.searchBar.move(20, 20)

        # Optional: Create a search button next to the search bar
        self.searchButton = PyQt5.QtWidgets.QPushButton("Search", self)
        self.searchButton.move(330, 20)

        # Buttons for the local maps/buildings
        self.lfButton = PyQt5.QtWidgets.QPushButton("LF", self)
        self.lfButton.move(520, 225)
        self.lfButton.setStyleSheet("background-color: transparent; border-color: transparent; color: transparent;")
        self.lfButton.clicked.connect(run_lf)

        self.psButton = PyQt5.QtWidgets.QPushButton("PS", self)
        self.psButton.move(540, 290)
        self.psButton.setStyleSheet("background-color: transparent; border-color: transparent; color: transparent;")
        self.psButton.clicked.connect(run_ps)

        self.cvButton = PyQt5.QtWidgets.QPushButton("CV", self)
        self.cvButton.move(540, 170)
        self.cvButton.setStyleSheet("background-color: transparent; border-color: transparent; color: transparent;")
        self.cvButton.clicked.connect(run_cv)

        self.cvButton = PyQt5.QtWidgets.QPushButton("HH", self)
        self.cvButton.move(600, 125)
        self.cvButton.setStyleSheet("background-color: transparent; border-color: transparent; color: transparent;")
        self.cvButton.clicked.connect(run_hh)

        self.cvButton = PyQt5.QtWidgets.QPushButton("KV", self)
        self.cvButton.move(800, 160)
        self.cvButton.setStyleSheet("background-color: transparent; border-color: transparent; color: transparent;")
        self.cvButton.clicked.connect(run_kv)

        # Connect signals to perform search when the user hits Enter or clicks the button
        self.searchBar.returnPressed.connect(self.performSearch)
        self.searchButton.clicked.connect(self.performSearch)

    def resizeEvent(self, event):
        #Ensure the map image always fills the window.
        self.mapLabel.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

    def performSearch(self):
        # clear previous blip markers
        self.clearMarkers()


        #Retrieve the user's query, search the file, and display results.
        query = self.searchBar.text().strip()
        if not query:
            PyQt5.QtWidgets.QMessageBox.warning(self, "Input Error", "Please enter a search query.")
            return


        results = self.searchClass(query)
        if results:
            # If multiple matches are found, join them into a single string.
            result_str = "\n".join(results)
            PyQt5.QtWidgets.QMessageBox.information(self, "Search Results", f"Building/Room Number(s):\n{result_str}")

            #displays blip for matching buildings
            for building in results:
                building = building.strip()
                self.placeMarker(building)

        else:
            PyQt5.QtWidgets.QMessageBox.information(self, "Search Results", "No matching class found.")

    def clearMarkers(self):
        #removes existing blips from map
        for marker in self.markerLabels:
            marker.deleteLater()
        self.markerLabels = []


    def placeMarker(self, building):
        #loads the blip onto map
        markerPixmap = QPixmap("../Images/JPEG/Blip.jpg")
        if markerPixmap.isNull():
            PyQt5.QtWidgets.QMessageBox.warning(self, "Image Error", "Blip image 'GUI_Map_Blip.png' not found.")
            return
        self.marker = PyQt5.QtWidgets.QLabel(self)
        self.marker.setFixedSize(20, 20)
        self.marker.setPixmap(markerPixmap)


        # Get the building coordinates from the dictionary
        x, y = self.buildingCoordinates[building[0:2]]
        # Adjust the marker so it is centered over the coordinate (optional)
        self.marker.move(x, y)
        self.marker.show()
        self.markerLabels.append(self.marker)



    def searchClass(self, query):
            results = []
            try:
                with open("../Database Sources/Course list.txt", "r") as file:
                    for line in file:
                        # Split the line into parts (expecting three parts per line)
                        parts = line.strip().split(',')
                        if len(parts) < 3:
                            continue  # Skip any improperly formatted lines
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

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = MapSearchWindow()
    window.show()
    sys.exit(app.exec_())