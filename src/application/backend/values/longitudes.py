"""
This module defines a class `longitudes` that provides a set of predefined length units
and a method to convert values between these units. 
"""
class longitud:
    def __init__(self, name, value):
        self.name = name
        self.value = value

"""
Classes:
    longitudes:
        A class containing predefined length units as class attributes and a method 
        for unit conversion.
Attributes:
    Nanometer (longitud): Represents the unit "Nanometer" with a value of 1e-9 meters.
    Micron (longitud): Represents the unit "Micron" with a value of 1e-6 meters.
    Millimeter (longitud): Represents the unit "Millimeter" with a value of 0.001 meters.
    Centimeter (longitud): Represents the unit "Centimeter" with a value of 0.01 meters.
    Meter (longitud): Represents the base unit "Meter" with a value of 1 meter.
    Kilometer (longitud): Represents the unit "Kilometer" with a value of 1000 meters.
    Inche (longitud): Represents the unit "Inche" with a value of 0.0254 meters.
    Feet (longitud): Represents the unit "Feet" with a value of 0.3048 meters.
    Yard (longitud): Represents the unit "Yard" with a value of 0.9144 meters.
    Mile (longitud): Represents the unit "Mile" with a value of 1609.34 meters.
    Nautical_Mile (longitud): Represents the unit "Nautical Mile" with a value of 1852 meters.
"""
class longitudes:
    Nanometer = longitud("Nanometer", 1e-9)
    Micron = longitud("Micron", 1e-6)
    Millimeter = longitud("Millimeter", 0.001)
    Centimeter = longitud("Centimeter", 0.01) 
    Meter = longitud("Meter", 1) # unit base
    Kilometer = longitud("Kilometer", 1000)
    Inche = longitud("Inche", 0.0254)
    Feet = longitud("Feet", 0.3048) 
    Yard = longitud("Yard", 0.9144)
    Mile = longitud("Mile", 1609.34)
    Nautical_Mile = longitud("Nautical Mile", 1852)
    
    """
    Methods:
        convert_longitud(value, origin, destin):
            Converts a given value from one length unit to another.
            Parameters:
                value (float): The numerical value to be converted.
                origin (str): The name of the origin unit (case-insensitive).
                destin (str): The name of the destination unit (case-insensitive).
            Returns:
                float: The converted value in the destination unit.
            Raises:
                AttributeError: If the origin or destination unit is not defined in the class.
    """
    def convert_longitud(self, value, origin, destin):
        value = float(value)
        origin_unit = getattr(longitudes, origin.title().replace(" ", "_")) # Convert to title case and replace spaces with underscores
        destin_unit = getattr(longitudes, destin.title().replace(" ", "_")) # Convert to title case and replace spaces with underscores
        return (value * origin_unit.value) / destin_unit.value 