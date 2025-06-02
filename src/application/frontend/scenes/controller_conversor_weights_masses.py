"""
module: controller_conversor_weights_masses
---------------------------------------
This module defines the `ConversorWeightAndMasses` class, which is a PyQt5-based GUI widget for interacting with weight and mass data.
It provides a graphical interface with a button and methods to retrieve weight and mass names and instances.
with a custom stylesheet and expands to fill available space.
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
- src.application.backend.values.weights_and_masses: Provides the `weights_and_masses` and `weight_and_mass` classes for handling weight and mass data.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy # Import necessary PyQt5 classes
from src.application.backend.values.weights_and_masses import weights_and_masses, weight_and_mass # Import the weights_and_masses and weight_and_mass classes from the backend module

"""
Classes:
--------
- ConversorWeightAndMasses(QWidget): A PyQt5 widget that displays a button and provides methods to interact with weight and mass data.
"""
class ConversorWeightAndMasses(QWidget):
    def __init__(self):
        super().__init__()
        self.initIU() # Initialize the user interface
    """
    Methods:
    --------
    - __init__():
        Initializes the `ConversorWeightAndMasses` widget and sets up the user interface.
    - initIU():
        Sets up the graphical user interface for the `ConversorWeightAndMasses` widget.
        Creates a button with specific styles and adds it to the layout.
    """
    def initIU(self):
        # Create the main layout for the widget the layout will be vertical and will be used to add the button to the widget
        layout = QVBoxLayout()

        self.button_weights_masses_widget = QPushButton() 
        self.button_weights_masses_widget.setText("Weight and Mass") 
        self.button_weights_masses_widget.setStyleSheet("""
                                                  font-size: 23px;
                                                  padding: 0 10px 0 10px;
                                                  background-color: #c0c0c0;
                                                  border-radius: 10px;
                                                  """)
        # Set the button to expand and fill available space
        self.button_weights_masses_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # Set the button to expand and fill available space
        layout.addWidget(self.button_weights_masses_widget)
        # Set the layout for the widget
        self.setLayout(layout)
    """
    Methods:
    --------
    - getWeightNames() -> list:
        Retrieves a list of weight and mass names from the `weights_and_masses` class.
        Iterates through the attributes of a `weights_and_masses` instance and collects the names of attributes that are instances of the `weight_and_mass` class.
    """
    def getWeightNames(self): # Method to get weight names
        weights_instance = weights_and_masses() # Create an instance of the weights_and_masses class
        weight_list = [] # Initialize an empty list to store weight names
        for key in dir(weights_instance): # Iterate through the attributes of the weights_and_masses instance
            attribute = getattr(weights_instance, key) # Get the attribute by its name
            if isinstance(attribute, weight_and_mass): # Check if the attribute is an instance of the weight_and_mass class
                weight_list.append(attribute.name.replace("_", " ")) # Append the name of the weight to the list
        return weight_list # Return the list of weight names
    """
    Method: getClass
    ----------------
    Returns an instance of the `weights_and_masses` class.
    """
    def getClass(self): # Method to get the weights_and_masses class
        return weights_and_masses() # Return an instance of the weights_and_masses class