"""
module: custom_dialog_copy
--------------------------------
This module defines the `CustomCopyDialog` class, which is a PyQt5-based dialog for displaying a message and providing an "Ok" button to close the dialog.
It provides a graphical interface with a message label and a button, styled with custom stylesheets.
Notes:
------
- The `CustomCopyDialog` class inherits from `QDialog`, allowing it to function as a modal dialog.
- The dialog is designed to be modal, blocking interaction with the parent window until it is closed.
Dependencies:
-------------
- PyQt5.QtWidgets: Used for creating the GUI components.
- PyQt5.QtCore: Provides core non-GUI functionality, including Qt constants.
"""
import sys
from PyQt5.QtWidgets import (
    QApplication, # Import QApplication for creating the application
    QDialog, # Import QDialog for creating dialog windows
    QVBoxLayout, # Import QVBoxLayout for vertical layout management
    QHBoxLayout, # Import QHBoxLayout for horizontal layout management
    QLabel, # Import QLabel for displaying text
    QPushButton, # Import QPushButton for creating buttons
)
from PyQt5.QtCore import Qt # Import Qt for using Qt constants

"""
Classes:
--------
- CustomCopyDialog(QDialog): A PyQt5 dialog that displays a message and provides an "Ok" button to close the dialog.
- The dialog is styled with custom stylesheets and is designed to be modal, blocking interaction with the parent window until closed.
- The dialog includes a message label and an "Ok" button, both styled with custom stylesheets.
- The dialog is initialized with a parent widget, and the "Ok" button is connected to the dialog's close method.
"""
class CustomCopyDialog(QDialog):
    def __init__(self, parent=None): # Initialize the dialog with an optional parent widget
        super().__init__(parent)
        self.setWindowTitle("Copy") 
        self.setModal(True)  # block the parent window
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)  # Remove the help button

        # Main layout
        self.layout_principal = QVBoxLayout(self)

        # Message label
        self.label_msg = QLabel("Result copy!")
        self.label_msg.setStyleSheet(
            """
            font-size: 18px;
            margin: 5px 15px;
            font-family: verdana;
            font-weight: bold;
        """
        )
        self.layout_principal.addWidget(self.label_msg)
        self.layout_principal.addSpacing(10)  # Add spacing between the label and the buttons

        # layout horizozontal for buttons
        self.layout_buttons = QHBoxLayout()
        self.layout_buttons.setAlignment(Qt.AlignCenter)  # Center the buttons

        # Botón Ok
        self.btn_ok = QPushButton("Ok")
        self.btn_ok.setStyleSheet(
            """
            border: 1px solid gray;
            border-radius: 5px;
            padding: 5px 20px;
            font-weight: bold;
        """
        )
        self.layout_buttons.addWidget(self.btn_ok)

        self.layout_principal.addLayout(self.layout_buttons)

        # connect the button to the close method
        # when the button is clicked, the dialog will be closed
        self.btn_ok.clicked.connect(self.reject)
    """
    Method: get_result
    ----------------
    Returns:
    -------
    - int: The result of the dialog execution.
    """
    def get_result(self):
        return self.exec_()

"""
Method: main
----------------
Main function to run the PyQt5 application.
It creates an instance of QApplication and starts the event loop.
"""
def main():
    app = QApplication(sys.argv)
    sys.exit(app.exec_())

"""
Method: run_custom_copy_dialog
----------------
Runs the custom copy dialog.
It creates an instance of the `CustomCopyDialog` class and executes it.
"""
if __name__ == "__main__":
    main()
