"""
This is the main entry point for the application.
It initializes the PyQt5 application and displays the main window.

- This project is a user-friendly unit converter application built using PyQt5.
- Developed based on the Code in Place certification program offered by
  Stanford University.
- The application allows users to convert between various units of measurement.
- The project follows the Model-View-Controller (MVC) architecture, separating
  the user interface from the business logic using object-oriented
  programming principles.
- You need to install [pip PyQt5]

It supports the following types of conversions:

1. Length Conversion:
    - Converts between units such as meters, kilometers, miles, and feet.
    - The logic for length conversion is implemented in a dedicated module.

2. Currency Conversion:
    - Converts between different currencies (e.g., USD, EUR, GBP).
    - It may use an API or predefined exchange rates for the conversion.

3. Weight and Mass Conversion:
    - Converts between units such as kilograms, grams, pounds, and ounces.
    - The conversion logic is handled in a separate module.

4. Temperature Conversion:
    - Converts between Celsius, Fahrenheit, and Kelvin.
    - The module for temperature conversion contains the necessary formulas.

Each conversion type is implemented in its own Python file/module, which is
imported and used in the application.

The root directory for the project is dynamically set based on the script's
location, allowing for a flexible project structure.

author: Marco CU
date: 2025-05-17
version: 1.0
"""
import sys  # Used to manipulate the Python runtime environment
from pathlib import Path  # Used to handle file paths in a platform-independent way

# Dynamically set the base directory for the application
BASE_DIR = Path(__file__).resolve().parents[3]  # Assuming the structure is src/application/main.py
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))  # Add the base directory to the system path

from PyQt5.QtWidgets import QApplication
from frontend.base import MainWindow

def main():
    """
    Initializes the PyQt5 application and displays the main window.
    """
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    """
    Entry point of the application. Calls the main function to start the GUI.
    """
    main()