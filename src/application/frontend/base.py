"""
This script implements a Unit Converter application using PyQt5. It provides a graphical user interface
(GUI) for converting between various units such as currencies, lengths, temperatures, and weights/masses.

Attributes:
-----------
- left_widget_menu_buttons (QWidget): Central widget for the main window.
- vbox_principal (QVBoxLayout): Main vertical layout for the menu.
- label_title (QLabel): Title label for the application.
- hbox_principal (QHBoxLayout): Horizontal layout containing buttons and the right widget.
- vbox_buttons (QVBoxLayout): Vertical layout for the menu buttons.
- conversor_widget_currency (ConversorCurriency): Widget for currency conversion.
- conversor_widget_longitud (ConversorLongitud): Widget for length conversion.
- conversor_widget_temperatures (ConversorTemperature): Widget for temperature conversion.
- conversor_widget_weights_and_masses (ConversorWeightAndMasses): Widget for weight and mass conversion.
- right_widget (QWidget): Widget for the right-side content.
- grid (QGridLayout): Grid layout for the right widget.
- Various QLabel, QLineEdit, QComboBox, and QPushButton elements for user interaction.
- current_conversion_class: Stores the current conversion class (e.g., currencies, longitudes, etc.).

main() Function:
----------------
- Initializes the QApplication and displays the MainWindow.
- Starts the event loop for the application.
Usage:
------
Run the script to launch the Unit Converter application. Use the menu buttons to select a conversion type, enter the amount, select units, and perform the conversion. The result will be displayed in the interface.
"""

"""Import necessary modules and classes"""
import sys  # Used to manipulate the Python runtime environment
from pathlib import Path  # Used to handle file paths in a platform-independent way

# Dynamically set the base directory for the application
BASE_DIR = Path(__file__).resolve().parents[3]  # Assuming the structure is src/application/main.py
if str(BASE_DIR) not in sys.path:
    sys.path.append(str(BASE_DIR))  # Add the base directory to the system path

from PyQt5.QtWidgets import (
    QApplication,  # QApplication is the main application class
    QMainWindow,  # QMainWindow is the main window class
    QWidget,  # QWidget is the base class for all UI objects
    QVBoxLayout,  # QVBoxLayout is a vertical box layout class
    QLabel,  # QLabel is a class for displaying text or images
    QHBoxLayout,  # QHBoxLayout is a horizontal box layout class
    QGridLayout,  # QGridLayout is a grid layout class
    QPushButton,  # QPushButton is a class for creating buttons
    QLineEdit,  # QLineEdit is a class for creating single-line text input fields
    QComboBox,  # QComboBox is a class for creating combo boxes (drop-down lists)
)
from PyQt5.QtGui import QIcon  # QIcon is a class for creating icons
from PyQt5.QtCore import Qt, QSize # Qt is a class for core non-GUI functionality
from src.application.frontend.custom_dialog_copy import (
    CustomCopyDialog,
)  # CustomCopyDialog is a custom dialog for copying results
from src.application.frontend.custom_dialog_logout import (
    CustomLogoutDialog,
)  # CustomLogoutDialog is a custom dialog for logout confirmation
from src.application.frontend.scenes.controller_conversor_longitudes import (
    ConversorLongitud,  # ConversorLongitud is a custom widget for length conversion
)
from src.application.frontend.scenes.controller_conversor_temperatures import (
    ConversorTemperature,  # ConversorTemperature is a custom widget for temperature conversion
)
from src.application.frontend.scenes.controller_conversor_currencies import (
    ConversorCurriency,  # ConversorCurriency is a custom widget for currency conversion
)
from src.application.frontend.scenes.controller_conversor_weights_masses import (
    ConversorWeightAndMasses,  # ConversorWeightAndMasses is a custom widget for weight and mass conversion
)
from src.application.backend.values.longitudes import (
    longitudes,
)  # longitudes is a module for length conversion
from src.application.backend.values.temperatures import (
    temperatures,
)  # temperatures is a module for temperature conversion
from src.application.backend.values.currencies import (
    currencies,
)  # currencies is a module for currency conversion
from src.application.backend.values.weights_and_masses import (
    weights_and_masses,
)  # weights_and_masses is a module for weight and mass conversion

"""
Class:
- MainWindow: Represents the main window of the application. It initializes the GUI components, handles user interactions, and manages the conversion logic.
Functions:
----------
- main(): Initializes the QApplication, displays the MainWindow, and starts the event loop.
- current_conversion_class: Stores the current conversion class (e.g., currencies, lengths, etc.).
MainWindow Class:
-----------------
This class represents the main window of the Unit Converter application. It is built using PyQt5 and provides a graphical user interface for converting between various units such as currencies, longitudes, temperatures, and weights/masses.
"""


class MainWindow(QMainWindow):
    """
    Sets the window title, icon, and geometry.
    - __init__(): Initializes the main window and its components.
    """

    def __init__(self):
        super().__init__()
        """Set the main window geometry"""
        self.setGeometry(
            (self.width() // 2) - 50, (self.height() // 2) - 70, 800, 500
        )  # Center the window
        self.setFixedSize(self.width(), self.height())  # Set fixed size
        self.setWindowTitle("Conversor")  # Set the window title
        self.setWindowIcon(QIcon("images/icon.jpg"))  # Set the window icon
        self.initIU()  # Initialize the user interface
        """Variable to store the current conversion class
        - This variable is used to determine which conversion class to use based on the user's selection."""
        self.current_conversion_class = None

    """
    Initialize the user interface components.
    - initIU(): Sets up the user interface, including layouts, widgets, and styles.
    """

    def initIU(self):
        """Set the central widget for the main window"""
        self.left_widget_menu_buttons = (QWidget())  # Create a central widget for the main window
        self.setCentralWidget(self.left_widget_menu_buttons)  # Set the central widget

        """Set the main vertical layout for the menu"""
        self.vbox_principal = QVBoxLayout(
            self.left_widget_menu_buttons
        )  # Create a vertical layout for the menu
        self.vbox_principal.setAlignment(Qt.AlignLeft)  # Align the layout to the left
        self.vbox_principal.setSpacing(0)  # Set spacing between widgets

        """Create the title label for the application"""
        self.label_title = QLabel("Unit Conversor")  # Create a label for the title
        self.label_title.setStyleSheet(  # Set the style for the title label
            "font-size: 30px; background-color: #d3d3d3; font-family: verdana; font-style: italic;"
        )
        self.label_title.setAlignment(Qt.AlignCenter | Qt.AlignTop)  # Align the label to the center and top
        self.vbox_principal.addWidget(self.label_title)  # Add the title label to the main layout

        """Create the main horizontal layout for the menu"""
        self.hbox_principal = QHBoxLayout()
        self.hbox_principal.setAlignment(Qt.AlignTop)  # Align the layout to the top
        self.hbox_principal.setSpacing(0)  # Set spacing between widgets

        """Create a vertical layout for the buttons"""
        self.vbox_buttons = QVBoxLayout()
        self.vbox_buttons.setAlignment(Qt.AlignLeft)  # Align the layout to the left
        self.vbox_buttons.setSpacing(0)  # Set spacing between widgets

        """
        Create instances of the conversion widgets
        - These widgets are used to display the conversion options and handle the conversion logic.
        """
        self.conversor_widget_currency = ConversorCurriency()
        self.conversor_widget_longitud = ConversorLongitud()
        self.conversor_widget_temperatures = ConversorTemperature()
        self.conversor_widget_weights_and_masses = ConversorWeightAndMasses()

        """Add the Converter widgets to the button layout"""
        self.vbox_buttons.addWidget(self.conversor_widget_currency)
        self.vbox_buttons.addWidget(self.conversor_widget_longitud)
        self.vbox_buttons.addWidget(self.conversor_widget_temperatures)
        self.vbox_buttons.addWidget(self.conversor_widget_weights_and_masses)

        """Add the button layout to the main horizontal layout"""
        self.hbox_principal.addLayout(self.vbox_buttons)

        """Add the horizontal layout to the main vertical layout"""
        self.vbox_principal.addLayout(self.hbox_principal)

        """Create a new layout for the right-side content"""
        self.right_widget = QWidget()

        """Create a grid layout for the right widget"""
        self.grid = QGridLayout(self.right_widget)
        self.label_amount = QLabel("Enter Amount")  # Create a label for the amount input
        self.line_edit_amount = QLineEdit()  # Create a line edit for user input
        self.label_from = QLabel("From")  # Create a label for the "From" unit
        self.btn_copy = QPushButton("Copy Result")  # Create a button to copy the result
        self.label_to = QLabel("To")  # Create a label for the "To" unit
        self.combo_box1 = QComboBox(self.right_widget)  # Create a combo box for the "From" unit
        self.combo_box2 = QComboBox(self.right_widget)  # Create a combo box for the "To" unit
        self.btn_convert = QPushButton("Convert")  # Create a button to perform the conversion
        self.btn_reset = QPushButton("Reset")  # Create a button to reset the input fields
        self.label_result = QLabel("Result:")  # Create a label for the result
        self.label_txt_result = (QLabel())  # Create a label to display the conversion result

        """Set object names for styling"""
        self.label_amount.setObjectName("amountLabel")
        self.line_edit_amount.setObjectName("lineEdit")
        self.label_from.setObjectName("fromLabel")
        self.label_to.setObjectName("toLabel")
        self.combo_box1.setObjectName("combo1")
        self.combo_box2.setObjectName("combo2")
        self.btn_copy.setObjectName("copyBtn")
        self.btn_convert.setObjectName("convertBtn")
        self.btn_reset.setObjectName("resetBtn")
        self.label_result.setObjectName("resultLabel")
        self.label_txt_result.setObjectName("txtLabel")

        """Set default options for combo boxes"""
        self.combo_box1.addItem("Options")
        self.combo_box1.setCurrentText(
            "Options"
        )  # Set the current text to the default option
        self.combo_box2.addItem("Options")
        self.combo_box2.setCurrentText("Options")  # Set the current text to the default option

        """Set placeholder text for the amount input field"""
        self.line_edit_amount.setPlaceholderText("Example: 123")

        """Set object names for layouts"""
        self.right_widget.setObjectName("gridWidget")
        self.vbox_principal.setObjectName("vboxPrincipal")
        self.hbox_principal.setObjectName("hboxPrincipal")
        self.vbox_buttons.setObjectName("vboxBtns")

        """Enable word wrapping for the result label"""
        self.label_txt_result.setWordWrap(True)

        """Apply styles to the widgets"""
        self.setStyleSheet(
            """
                           #gridWidget{
                               background-color: #c9c9c9;
                                border-radius: 10px;
                                padding: 20px;
                           }
                           #combo1, #combo2{
                               width: 175;
                               height: 40;
                               font-size: 20px;
                               padding: 10px 0 10px 20px;
                               border-radius: 5px;
                               text-align: center;
                           }
                           QComboBox::down-arrow{
                               background-color: #c0c0c0;
                           }
                           #amountLabel, #resultLabel{
                               font-size: 30px;
                               font-weight: 500;
                                padding-bottom: 10px;
                           }
                           #fromLabel, #toLabel{
                               font-size: 25px;
                                font-weight: 500;
                                padding-bottom: 10px;
                           }
                           #txtLabel{
                               font-size: 20px;
                               font-weight: 450;
                               padding-bottom: 10px;
                           }
                           #lineEdit{
                               width: 275;
                               height: 40;
                               padding: 0 5px 0 5px;
                               font-size: 17px;
                               border-radius: 2px;
                               background-color: #ffffff;
                               border: 1px solid gray;
                           }
                           #copyBtn, #convertBtn, #resetBtn{
                               width: 150;
                               height: 30;
                               font-size: 20px;
                               font-weight: 300;
                               background-color: #ffffff;
                               border: 1px solid gray;
                               border-radius: 5px;
                               padding: 5px 0 5px 0;
                           }
                           """
        )

        """Add widgets to the grid layout"""
        self.grid.addWidget(self.label_amount, 0, 0, 1, 3, Qt.AlignHCenter)  # Amount label
        self.grid.addWidget(self.line_edit_amount, 1, 0, 1, 3, Qt.AlignHCenter)  # Amount input field
        self.grid.addWidget(self.label_from, 2, 0, Qt.AlignHCenter)  # From label
        self.grid.addWidget(self.label_to, 2, 2, Qt.AlignHCenter)  # To label
        self.grid.addWidget(self.combo_box1, 3, 0, Qt.AlignHCenter)  # From combo box
        self.grid.addWidget(self.combo_box2, 3, 2, Qt.AlignHCenter)  # To combo box
        self.grid.addWidget(self.btn_convert, 4, 0, Qt.AlignHCenter)  # Convert button
        self.grid.addWidget(self.btn_copy, 4, 1)  # Copy button
        self.grid.addWidget(self.btn_reset, 4, 2, Qt.AlignHCenter)  # Reset button
        self.grid.addWidget(self.label_result, 5, 1, Qt.AlignHCenter)  # Result label
        self.grid.addWidget(self.label_txt_result, 6, 0, 2, 3, Qt.AlignHCenter)  # Result text

        """Add the right widget to the main horizontal layout"""
        self.hbox_principal.addWidget(self.right_widget, 1)

        """Hide the result label initially"""
        self.label_txt_result.hide()

        """Connect buttons to their respective methods"""
        self.btn_convert.clicked.connect(self.startConversionProcess)
        self.btn_copy.clicked.connect(self.copyResult)
        self.btn_reset.clicked.connect(self.reset)

        """Connect menu buttons to their respective conversion methods"""
        self.conversor_widget_longitud.button_longitud_widget.clicked.connect(
            self.setLongitudConversion  # This method is called when the length conversion button is clicked
        )
        self.conversor_widget_currency.button_currencies_widget.clicked.connect(
            self.setCurrencyConversion  # This method is called when the currency conversion button is clicked
        )
        self.conversor_widget_temperatures.button_temperatures_widget.clicked.connect(
            self.setTemperatureConversion  # This method is called when the temperature conversion button is clicked
        )
        self.conversor_widget_weights_and_masses.button_weights_masses_widget.clicked.connect(
            self.setWeightConversion  # This method is called when the weight and mass conversion button is clicked
        )

    """
    Methods:
    --------
    - setLongitudConversion(): Configures the interface for length conversion.
    - setCurrencyConversion(): Configures the interface for currency conversion.
    - setTemperatureConversion(): Configures the interface for temperature conversion.
    - setWeightConversion(): Configures the interface for weight and mass conversion.
    - setComboBoxes(names): Populates the combo boxes with unit names.
    - setConversion(): Performs the conversion based on user input and displays the result.
    - reset(): Resets the input fields and result label.
    - startConversionProcess(): Placeholder for starting the conversion process.
    - closeEvent(event): Handles the close event with a logout confirmation dialog.
    - copyResult(): Copies the conversion result to the clipboard.
    """

    def setLongitudConversion(self):
        self.current_conversion_class = (longitudes) # Set the current conversion class to longitudes
        self.label_title.setText("Unit Convert - Longitudes") # Set the title for length conversion
        self.setComboBoxes(self.conversor_widget_longitud.getLongitudNames()) # Populate the combo boxes with length unit names
        self.btn_convert.clicked.disconnect() # Disconnect the previous signal
        self.btn_convert.clicked.connect(self.setConversion) # Connect the convert button to the conversion method
        self.line_edit_amount.setPlaceholderText("Example: 123") # Set placeholder text for the amount input field

    def setCurrencyConversion(self):
        self.current_conversion_class = currencies
        self.label_title.setText("Unit Convert - Currencies")
        self.line_edit_amount.setPlaceholderText("(exchage rate of 2, June, 2025)") # Set placeholder text for the amount input field
        self.setComboBoxes(self.conversor_widget_currency.getCurrencyNames())
        self.btn_convert.clicked.disconnect()
        self.btn_convert.clicked.connect(self.setConversion)

    def setTemperatureConversion(self):
        self.current_conversion_class = temperatures
        self.label_title.setText("Unit Convert - Temperatures")
        self.setComboBoxes(self.conversor_widget_temperatures.getTemperatureNames())
        self.btn_convert.clicked.disconnect()
        self.btn_convert.clicked.connect(self.setConversion)
        self.line_edit_amount.setPlaceholderText("Example: 123") # Set placeholder text for the amount input field

    def setWeightConversion(self):
        self.current_conversion_class = weights_and_masses
        self.label_title.setText("Unit Convert - Weights & Masses")
        self.setComboBoxes(self.conversor_widget_weights_and_masses.getWeightNames())
        self.btn_convert.clicked.disconnect()
        self.btn_convert.clicked.connect(self.setConversion)
        self.line_edit_amount.setPlaceholderText("Example: 123") # Set placeholder text for the amount input field

    def setComboBoxes(self, names):
        self.combo_box1.clear()  # Clear the first combo box
        self.combo_box2.clear()  # Clear the second combo box
        self.combo_box1.addItem("Options")  # Add default option to the first combo box
        self.combo_box2.addItem("Options")  # Add default option to the second combo box
        self.combo_box1.setCurrentText("Options")  # Set the current text to the default option
        self.combo_box2.setCurrentText("Options")  # Set the current text to the default option
        for name in names:  # Iterate through the provided names
            icon = QIcon()  # Set the icon for the combo boxes
            # Set the icon based on the currency name
            if name == "USD":
                icon = QIcon("images/flags/Flag_of_the_United_States.png")
            elif name == "MXN":
                icon = QIcon("images/flags/Flag_of_Mexico.png")
            elif name == "EUR":
                icon = QIcon("images/flags/Flag_of_Europe.png")
            elif name == "GBP":
                icon = QIcon("images/flags/Flag_of_the_United_Kingdom.png")
            elif name == "JPY":
                icon = QIcon("images/flags/Flag_of_Japan.png")
            elif name == "KRW":
                icon = QIcon("images/flags/Flag_of_South_Korea.png")
            elif name == "CAD":
                icon = QIcon("images/flags/Flag_of_Canada.png")
            elif name == "AUD":
                icon = QIcon("images/flags/Flag_of_Australia.png")
            
            self.combo_box1.addItem(icon, name) # Add each name to the first combo box and set the icon
            self.combo_box2.addItem(icon, name)  # Add each name to the second combo box and set the icon
            
            # Adjust the size of the combo box to accommodate larger icons
            self.combo_box1.setIconSize(QSize(50, 30))  # Set the icon size for the first combo box
            self.combo_box2.setIconSize(QSize(50, 30))  # Set the icon size for the second combo box


    def setConversion(self):
        # Check if a conversion class is selected
        if self.current_conversion_class is None:
            self.label_txt_result.setText("Please select a conversion type from the menu.")
            self.label_txt_result.show()
            return  # Exit the method if no conversion class is selected

        amount_text = (self.line_edit_amount.text())  # Get the text from the amount input field
        origin_unit = (self.combo_box1.currentText())  # Get the selected unit from the first combo box
        destination_unit = (self.combo_box2.currentText())  # Get the selected unit from the second combo box

        if (
            origin_unit == destination_unit  # Check if the selected units are the same
            or destination_unit == origin_unit  # Check if the selected units are the same
            or not amount_text  # Check if the amount input field is empty
        ):
            self.label_txt_result.setText("Please select units and enter an amount.")
            self.label_txt_result.show()
            return  # Exit the method if the conditions are met

        try:
            value = float(amount_text)  # Convert the amount text to a float
            if (self.current_conversion_class == currencies):  # Check if the conversion class is currencies
                converter = currencies()
                result = converter.convert_currency(value, origin_unit, destination_unit)
                self.label_txt_result.setText(
                    f"{float(value):,} {origin_unit} are {result:,.2f} {destination_unit}"
                )
                self.label_txt_result.show()
            elif (self.current_conversion_class == longitudes):  # Check if the conversion class is longitudes
                converter = longitudes()
                result = converter.convert_longitud(value, origin_unit, destination_unit)
                self.label_txt_result.setText(
                    f"{float(value):,} {origin_unit} are {result:,.4f} {destination_unit}"
                )
                self.label_txt_result.show()
            elif (self.current_conversion_class == temperatures):  # Check if the conversion class is temperatures
                converter = temperatures()
                result = converter.convert_temperature(value, origin_unit, destination_unit)
                symb_origin = converter.symbol_format(origin_unit)  # Get the symbol for the origin unit
                symb_destin = converter.symbol_format(destination_unit)  # Get the symbol for the destination unit
                self.label_txt_result.setText(
                    f"{float(value):,} {symb_origin} {origin_unit} are {result:,.2f} {symb_destin} {destination_unit}"
                )
                self.label_txt_result.show()
            elif (self.current_conversion_class == weights_and_masses):  # Check if the conversion class is weights and masses
                converter = weights_and_masses()
                result = converter.convert_weight_and_mass(value, origin_unit, destination_unit)
                self.label_txt_result.setText(
                    f"{float(value):,} {origin_unit} are {result:,.3f} {destination_unit}"
                )
                self.label_txt_result.show()
            else:
                self.label_txt_result.setText("Error: Invalid conversion type selected.")
                self.label_txt_result.show()
        except ValueError:  # Handle invalid input for the amount
            self.label_txt_result.setText("Invalid amount. Please enter a number.")
            self.label_txt_result.show()
        except AttributeError:  # Handle invalid unit selection
            self.label_txt_result.setText("Error: Invalid unit selected.")
            self.label_txt_result.show()
        except Exception as e:  # Handle any other exceptions
            self.label_txt_result.setText(f"An error occurred: {e}")
            self.label_txt_result.show()

    def reset(self):
        self.combo_box1.setCurrentText("Options")
        self.combo_box2.setCurrentText("Options")
        self.line_edit_amount.clear()
        self.label_txt_result.clear()
        self.label_txt_result.hide()

    def startConversionProcess(self):
        pass

    def closeEvent(self, event):
        # Show a custom dialog to confirm logout
        dialogo_logout = CustomLogoutDialog(self)
        if dialogo_logout.get_result():  # If the user confirms logout
            event.accept()  # Close the application
        else:  # If the user cancels logout
            event.ignore()  # Ignore the close event

    def copyResult(self):
        text_result = self.label_txt_result.text()  # Get the text from the result label

        clipboard = QApplication.clipboard()  # Get the clipboard object

        clipboard.setText(text_result)  # Set the text in the clipboard

        # Show a custom dialog to confirm the copy action
        CustomCopyDialog(self).get_result()


def main():
    app = QApplication(sys.argv)  # Create a QApplication instance
    window = MainWindow()  # Create an instance of the MainWindow class
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Start the event loop for the application


# Run the main function if this script is executed directly
# This allows the script to be run as a standalone application
if __name__ == "__main__":
    main()
