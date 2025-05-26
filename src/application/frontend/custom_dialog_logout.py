"""
module: custom_dialog_logout
--------------------------------
This module defines the `CustomLogoutDialog` class, which is a PyQt5-based dialog for displaying a logout confirmation message and providing "Yes" and "No" buttons to confirm or cancel the action.
It provides a graphical interface with a message label and buttons, styled with custom stylesheets.
Notes:
------
- The `CustomLogoutDialog` class inherits from `QDialog`, allowing it to function as a modal dialog.
- The dialog is designed to be modal, blocking interaction with the parent window until it is closed.
Dependencies:
-------------
- PyQt5.QtWidgets: Used for creating the GUI components.
- PyQt5.QtCore: Provides core non-GUI functionality, including Qt constants.
"""
import sys # Import sys for system-specific parameters and functions
from PyQt5.QtWidgets import (
    QApplication, # Import QApplication for creating the application
    QDialog, # Import QDialog for creating dialog windows
    QVBoxLayout, # Import QVBoxLayout for vertical layout management
    QHBoxLayout, # Import QHBoxLayout for horizontal layout management
    QLabel, # Import QLabel for displaying text
    QPushButton) # Import QPushButton for creating buttons
from PyQt5.QtCore import Qt # Import Qt for using Qt constants

"""
Classes:
--------
- CustomLogoutDialog(QDialog): A PyQt5 dialog that displays a logout confirmation message and provides "Yes" and "No" buttons to confirm or cancel the action.
- The dialog is styled with custom stylesheets and is designed to be modal, blocking interaction with the parent window until closed.
- The dialog includes a message label and "Yes" and "No" buttons, both styled with custom stylesheets.
- The dialog is initialized with a parent widget, and the "Yes" and "No" buttons are connected to the dialog's acceptance and rejection methods.
"""
class CustomLogoutDialog(QDialog):
    def __init__(self, parent=None): # Initialize the dialog with an optional parent widget
        super().__init__(parent) 
        self.setWindowTitle("Logout")
        self.setModal(True) #block the parent window
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint) # Remove the help button

        # Main layout
        self.layout_principal = QVBoxLayout(self)

        # Message label
        self.label_msg = QLabel("Do you want to exit?")
        self.label_msg.setStyleSheet("""
            font-size: 18px;
            margin: 5px 15px;
            font-family: verdana;
            font-weight: bold;
        """)
        self.layout_principal.addWidget(self.label_msg)
        self.layout_principal.addSpacing(10) # Add spacing between the label and the buttons

        # Layout horizontal for buttons
        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.setAlignment(Qt.AlignCenter) # Center the buttons
        

        # Botón Yes
        self.btn_yes = QPushButton("Yes")
        self.btn_yes.setStyleSheet("""
            border: 1px solid gray;
            border-radius: 5px;
            padding: 5px 20px;
            font-weight: bold;
        """)
        # Add the button to the layout
        self.layout_buttons.addWidget(self.btn_yes)

        # Botón No
        self.btn_no = QPushButton("No")
        self.btn_no.setStyleSheet("""
            border: 1px solid gray;
            border-radius: 5px;
            padding: 5px 20px;
            font-weight: bold;
        """)
        # Add the button to the layout
        self.layout_buttons.addWidget(self.btn_no)

        # Add the buttons layout to the main layout
        self.layout_principal.addLayout(self.layout_buttons)

        # Connect the buttons to the dialog's acceptance and rejection methods
        # when the button is clicked, the dialog will be closed
        self.btn_yes.clicked.connect(self.accept)
        self.btn_no.clicked.connect(self.reject)
    
    """
    Method: get_result
    ----------------
    Returns:
    -------
    - int: The result of the dialog execution.
    """
    def get_result(self): # Method to get the result of the dialog
        return self.exec_() == QDialog.Accepted # Return True if the dialog was accepted, False otherwise

"""
Method: main
----------------
Main function to run the PyQt5 application.
It creates an instance of QApplication and starts the event loop.
"""
def main():
    app = QApplication(sys.argv) # Create the application
    sys.exit(app.exec_()) # Start the event loop

"""
Method: run_custom_logout_dialog
----------------
Runs the custom logout dialog.
It creates an instance of the `CustomLogoutDialog` class and executes it.
"""
if __name__ == '__main__':
    main()