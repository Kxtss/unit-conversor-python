"""
Module: controller_conversor_currencies
---------------------------------------
This module defines the `ConversorCurriency` class, which is a PyQt5-based GUI widget for interacting with currency data. 
It provides a graphical interface with a button and methods to retrieve currency names and instances.
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
- src.application.backend.values.currencies: Provides the `currencies` and `currency` classes for handling currency data.
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSizePolicy # Import necessary PyQt5 classes
# Import the currencies and currency classes from the backend module
from src.application.backend.values.currencies import currencies, currency
"""
Classes:
--------
- ConversorCurriency(QWidget): A PyQt5 widget that displays a button and provides methods to interact with currency data.
"""
class ConversorCurriency(QWidget):
    def __init__(self):
        super().__init__()
        self.initIU()
    """
    Methods:
    --------
    - __init__():
        Initializes the `ConversorCurriency` widget and sets up the user interface.
    - initIU():
        Sets up the graphical user interface for the `ConversorCurriency` widget. 
        Creates a button with specific styles and adds it to the layout.
    - getCurrencyNames() -> list:
        Retrieves a list of currency names from the `currencies` class. 
        Iterates through the attributes of a `currencies` instance and collects the names of attributes that are instances of the `currency` class.
    - getClass() -> currencies:
        Returns an instance of the `currencies` class.
    Attributes:
    -----------
    - button_currencies_widget (QPushButton): 
    A button widget displayed in the `ConversorCurriency` interface.
    """
    def initIU(self):
        # Create the main layout for the widget the layout will be vertical and will be used to add the button to the widget
        layout = QVBoxLayout()

        self.button_currencies_widget = QPushButton()
        self.button_currencies_widget.setText("currencies")
        self.button_currencies_widget.setStyleSheet(
            """
                                                  font-size: 25px;
                                                  background-color: #c0c0c0;
                                                  border-radius: 10px;
                                                  """
        )
        # Set the size policy for the button to expand vertically
        self.button_currencies_widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        # Add the button to the layout
        layout.addWidget(self.button_currencies_widget)
        # Set the layout for the widget
        self.setLayout(layout)

    """
    Method: getCurrencyNames
    -------------------
    Retrieves a list of currency names from the `currencies` class.
    Iterates through the attributes of a `currencies` instance and collects the names of attributes that are instances of the `currency` class.
    Returns:
    -------
    - list: A list of currency names.
    """
    def getCurrencyNames(self):
        currency_instance = currencies() # Create an instance of the currencies class
        currency_list = [] # Initialize an empty list to store currency names
        for key in dir(currency_instance): # Iterate through the attributes of the currencies instance
            attribute = getattr(currency_instance, key) # Get the attribute by its name
            if isinstance(attribute, currency): # Check if the attribute is an instance of the currency class
                currency_list.append(attribute.name) # Append the name of the currency to the list
        return currency_list # Return the list of currency names
    """
    Method: getClass
    -------------------
    Returns an instance of the `currencies` class.
    Returns:
    -------
    - currencies: An instance of the `currencies` class.
    """
    def getClass(self): # Create an instance of the currencies class
        return currencies() # Return the instance of the currencies class
