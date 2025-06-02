"""
module: controller_conversor_temperatures
--------------------------------------- 
This module defines the `ConversorTemperature` class, which is a PyQt5-based GUI widget for interacting with temperature data.
It provides a graphical interface with a button and methods to retrieve temperature names and instances.
Notes:
------
- The `root_dir` is dynamically determined to allow importing modules from the project root directory.
- The button in the interface is styled with a custom stylesheet and expands to fill available space.
"""
import sys  # Used to manipulate the Python runtime environment
from pathlib import Path  # Used to handle file paths in a platform-independent way

# Dynamically set the base directory for the application
BASE_DIR = Path(__file__).resolve().parents[3]  # Assuming the structure is src/application/main.py
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))  # Add the base directory to the system path
"""
Dependencies:
-------------
- PyQt5.QtWidgets: Used for creating the GUI components.
- src.application.backend.values.temperatures: Provides the `temperatures` class for handling temperature data.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy
from src.application.backend.values.temperatures import temperatures  # Import the temperatures class from the backend

"""
Classes:
--------
- ConversorTemperature(QWidget): A PyQt5 widget that displays a button and provides methods to interact with temperature data.
"""
class ConversorTemperature(QWidget):
    def __init__(self):
        super().__init__()  # Call the parent class constructor
        self.initIU()  # Initialize the user interface
    """
    Methods:
    --------
    - __init__():
        Initializes the `ConversorTemperature` widget and sets up the user interface.
    - initIU():
        Sets up the graphical user interface for the `ConversorTemperature` widget.
        Creates a button with specific styles and adds it to the layout.
    - getTemperatureNames() -> list:
        Retrieves a list of temperature names from the `temperatures` class.
        Defines a list of temperature names and returns it.
    - getClass() -> temperatures:
        Returns an instance of the `temperatures` class.
    Attributes:
    -----------
    - button_temperatures_widget (QPushButton): 
        A button widget displayed in the `ConversorTemperature` interface.
    """

    def initIU(self):
        # Create the main layout for the widget; the layout will be vertical
        layout = QVBoxLayout()

        # Create a button widget for temperatures
        self.button_temperatures_widget = QPushButton()
        self.button_temperatures_widget.setText("temperatures")  # Set the button text
        self.button_temperatures_widget.setStyleSheet("""
                                                  font-size: 25px;
                                                  background-color: #c0c0c0;
                                                  border-radius: 10px;
                                                  """)
        # Set the size policy for the button to expand vertically
        self.button_temperatures_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # Add the button to the layout
        layout.addWidget(self.button_temperatures_widget)
        # Set the layout for the widget
        self.setLayout(layout)
    """
    Methods:
    --------
    - getTemperatureNames() -> list:
        Retrieves a list of temperature names from the `temperatures` class. 
        Defines a list of temperature names and returns it.
    - getClass() -> temperatures:
        Returns an instance of the `temperatures` class.
    """
    def getTemperatureNames(self):
        # Define a list of temperature names
        temp_list = ["Celsius", "Fahrenheit", "Kelvin"]
        return temp_list  # Return the list of temperature names
    """
    Method: getClass
    -------------------
    Returns:
    -------
    - temperatures: An instance of the `temperatures` class.
    """
    def getClass(self):
        # Return an instance of the temperatures class
        return temperatures()