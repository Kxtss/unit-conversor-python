class temperatures:
    """
    This module provides a class `temperatures` for temperature conversions and formatting.
    Classes:
        temperatures: A class containing methods for converting temperatures between Celsius, Fahrenheit, and Kelvin,
                      as well as formatting temperature symbols.
    Methods:
        symbol_format(temperature):
            Returns the symbol representation of a given temperature scale.
            Args:
                temperature (str): The name of the temperature scale ("Celsius", "Fahrenheit", "Kelvin").
            Returns:
                str: The symbol of the temperature scale ("°C", "°F", "K").
        celsius_to_fahrenheit(celsius):
            Converts a temperature from Celsius to Fahrenheit.
            Args:
                celsius (float): Temperature in Celsius.
            Returns:
                float: Temperature in Fahrenheit.
        celsius_to_kelvin(celsius):
            Converts a temperature from Celsius to Kelvin.
            Args:
                celsius (float): Temperature in Celsius.
            Returns:
                float: Temperature in Kelvin.
        fahrenheit_to_celsius(fahrenheit):
            Converts a temperature from Fahrenheit to Celsius.
            Args:
                fahrenheit (float): Temperature in Fahrenheit.
            Returns:
                float: Temperature in Celsius.
        fahrenheit_to_kelvin(fahrenheit):
            Converts a temperature from Fahrenheit to Kelvin.
            Args:
                fahrenheit (float): Temperature in Fahrenheit.
            Returns:
                float: Temperature in Kelvin.
        kelvin_to_celsius(kelvin):
            Converts a temperature from Kelvin to Celsius.
            Args:
                kelvin (float): Temperature in Kelvin.
            Returns:
                float: Temperature in Celsius.
        kelvin_to_fahrenheit(kelvin):
            Converts a temperature from Kelvin to Fahrenheit.
            Args:
                kelvin (float): Temperature in Kelvin.
            Returns:
                float: Temperature in Fahrenheit.
        convert_temperature(value, origin, destin):
            Converts a temperature value from one scale to another.
            Args:
                value (float): The temperature value to convert.
                origin (str): The original temperature scale ("Celsius", "Fahrenheit", "Kelvin").
                destin (str): The destination temperature scale ("Celsius", "Fahrenheit", "Kelvin").
            Returns:
                float: The converted temperature value.
    """

    def symbol_format(self, temperature): # formatting the temperature symbol
        if temperature == "Celsius":
            return "°C" 
        elif temperature == "Fahrenheit":
            return "°F"
        elif temperature == "Kelvin":
            return "K"

    def celsius_to_fahrenheit(celsius):
        celsius = float(celsius)
        return (celsius * 9 / 5) + 32

    def celsius_to_kelvin(celsius):
        celsius = float(celsius)
        return celsius + 273.15

    def fahrenheit_to_celsius(fahrenheit):
        fahrenheit = float(fahrenheit)
        return (fahrenheit - 32) * 5 / 9

    def fahrenheit_to_kelvin(fahrenheit):
        fahrenheit = float(fahrenheit)
        return (fahrenheit - 32) * 5 / 9 + 273.15

    def kelvin_to_celsius(kelvin):
        kelvin = float(kelvin)
        return kelvin - 273.15

    def kelvin_to_fahrenheit(kelvin):
        kelvin = float(kelvin)
        return (kelvin - 273.15) * 9 / 5 + 32

    def convert_temperature(self, value, origin, destin):
        value = float(value) # converting the value to float
        if origin == "Celsius" and destin == "Fahrenheit": # converting Celsius to Fahrenheit
            return temperatures.celsius_to_fahrenheit(value) # calling the function
        elif origin == "Celsius" and destin == "Kelvin": # converting Celsius to Kelvin
            return temperatures.celsius_to_kelvin(value)
        elif origin == "Fahrenheit" and destin == "Celsius": # converting Fahrenheit to Celsius
            return temperatures.fahrenheit_to_celsius(value)
        elif origin == "Fahrenheit" and destin == "Kelvin": # converting Fahrenheit to Kelvin
            return temperatures.fahrenheit_to_kelvin(value)
        elif origin == "Kelvin" and destin == "Celsius": # converting Kelvin to Celsius
            return temperatures.kelvin_to_celsius(value)
        elif origin == "Kelvin" and destin == "Fahrenheit": # converting Kelvin to Fahrenheit
            return temperatures.kelvin_to_fahrenheit(value)
