"""
module: Controller_conversor_longitudes
---------------------------------------
This module defines the `ConversorLongitud` class, which is a PyQt5-based GUI widget for interacting with length data.
It provides a graphical interface with a button and methods to retrieve length names and instances.
Notes:
------
- The `root_dir` is dynamically determined to allow importing modules from the project root directory.
- The button in the interface is styled with a custom stylesheet and expands to fill available space.
"""
import sys  # sys is used to manipulate the Python runtime environment
import os  # os is used to interact with the operating system

# Get the root directory path of the project (adjust as needed)
# This is the suggested path if the project is located on the Desktop
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
sys.path.append(root_dir)  # Add the root directory to the system path

"""
Dependencies:
-------------
- PyQt5.QtWidgets: Used for creating the GUI components.
- src.application.backend.values.longitudes: Provides the `longitudes` and `longitud` classes for handling length data.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy # Import necessary PyQt5 classes
# Import the longitudes and longitud classes from the backend module
from src.application.backend.values.longitudes import longitud, longitudes
"""
Classes:
--------
- ConversorLongitud(QWidget): A PyQt5 widget that displays a button and provides methods to interact with length data.
"""
class ConversorLongitud(QWidget):
    def __init__(self):
        super().__init__()
        self.initIU() # Initialize the user interface
    """
    Methods:
    --------
    - __init__():
        Initializes the `ConversorLongitud` widget and sets up the user interface.
    - initIU():
        Sets up the graphical user interface for the `ConversorLongitud` widget.
        Creates a button with specific styles and adds it to the layout.
    """
    def initIU(self):
        # Create the main layout for the widget the layout will be vertical and will be used to add the button to the widget
        layout = QVBoxLayout()
        
        self.button_longitud_widget = QPushButton()
        self.button_longitud_widget.setText("longitudes")
        self.button_longitud_widget.setStyleSheet("""
                                                  font-size: 25px;
                                                  background-color: #c0c0c0;
                                                  border-radius: 10px;
                                                  """)
        # Set the button to expand vertically
        self.button_longitud_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # Set the button to expand horizontally
        layout.addWidget(self.button_longitud_widget)
        # Add the button to the layout
        self.setLayout(layout)

    """
    Methods:
    --------
    - getLongitudNames() -> list:
        Retrieves a list of length names from the `longitudes` class.
        Iterates through the attributes of a `longitudes` instance and collects the names of attributes that are instances of the `longitud` class.
    """
    def getLongitudNames(self):
        longitudes_instancia = longitudes() # Create an instance of the longitudes class
        lon_list = [] # Initialize an empty list to store length names
        for key in dir(longitudes_instancia): # Iterate through the attributes of the longitudes instance
            attribute = getattr(longitudes_instancia, key) # Get the attribute by name
            if isinstance(attribute, longitud): # Check if the attribute is an instance of the longitud class
                lon_list.append(attribute.name.replace("_", " ")) # Append the name of the length to the list
        return lon_list # Return the list of length names
    """
    Method: getClass
    -------------------
    Returns an instance of the `longitudes` class.
    """
    def getClass(self): # Returns an instance of the longitudes class
        return longitudes() # Returns an instance of the longitudes class