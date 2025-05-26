# Unit Conversor with Python

This project is a Python-based converter application designed to perform various types of conversions, such as currency, temperature, and more. It is a simple and efficient tool for handling everyday conversion tasks.

![conversor](https://github.com/user-attachments/assets/5ba6a93a-89eb-4bc8-b827-3b73d19b7dbf)
<br>
<u>Developed based on the final project certification program for the Code in Place course offered by Stanford University.</u>

## Features

- **Currency Conversion**: Convert between different currencies using May 26, 2025 exchanges (maybe in the future I add an API to do dynamic exchanges).
    - **USD** *(United States Dollar)* <u>base unit</u>
    - **MXN** *(Mexican Peso)*
    - **EUR** *(Euro)*
    - **GBP** *(British Pound)*
    - **JPY** *(Japanese Yen)*
    - **KRW** *(South Korean Won)*
    - **CAD** *(Canadian Dollar)*
    - **AUD** *(Australian Dollar)*
<br>
![currencies](https://github.com/user-attachments/assets/1806df9e-1571-463b-ad12-01e13d141b61)
- **Temperature Conversion**: Convert between Celsius, Fahrenheit, and Kelvin.
  ![temperatures](https://github.com/user-attachments/assets/90d26a0b-5b7c-4e81-b331-0edc28985aa2)
- **Unit Conversion**: You can convert units of length and weight and mass units.
### **Longitud Units**
- **Nanometer** 
- **Micron** 
- **Millimeter** 
- **Centimeter** 
- **Meter**  <u>base unit</u>
- **Kilometer** 
- **Inch** 
- **Feet** 
- **Yard** 
- **Mile** 
- **Nautical Mile**
<br>
![longitudes](https://github.com/user-attachments/assets/48839d16-8040-43e5-9973-08dee4416009)
### **Weight and Mass Units**
- **Carat** 
- **Milligram** 
- **Centigram** 
- **Decigram** 
- **Gram**  <u>base unit</u>
- **Decagram** 
- **Hectogram** 
- **Kilogram** 
- **Metric Ton** 
- **Ounce** 
- **Pound** 
- **Stone** 
- **Short Ton** 
- **Long Ton**
<br>
![weight and mass](https://github.com/user-attachments/assets/14527630-bc79-43de-923c-2f4ad64f4bef)
- **User-Friendly Interface**: Easy-to-use interface for quick conversions.

## Requirements

- Python 3.8 or higher
- Required libraries (install via `pip`):
    - `PyQt5`

## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/Kxtss/unit-conversor-python.git
     ```
2. Navigate to the project directory:
    - create a new carpet in Desktop
    ```bash
    cd Conversor with Python
    ```
3. Install the required dependencies:
     ```bash
     pip install -r requirements.txt
     ```
4. **Note on Paths**: 
If you decide to move your project elsewhere, you'll need to adjust the internal paths in your code that access files
*uses logic like:*
```bash
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
``` 
This involves adding or removing ".." depending on the depth of the folder.
<u>*Recommending to use the Desktop path.*</u>

## Usage

1. Run the application:
     ```bash
     python main.py
     ```
2. Follow the on-screen instructions to perform conversions.


## Contact

For any questions or feedback, please contact:
- Discord: [tengokudaimakyo]
