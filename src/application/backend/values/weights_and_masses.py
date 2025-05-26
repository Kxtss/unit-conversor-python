"""
This module contains the definition of various weight and mass units, their conversion factors, and a method to convert between them.
- The `weight_and_mass` class represents a single weight or mass unit with its name and value.
- The `weights_and_masses` class contains several predefined weight and mass units as class attributes and provides a method to convert between them.
"""
class weight_and_mass:
    def __init__(self, name, value):
        self.name = name
        self.value = value

"""
This class represents a weight or mass unit with its name and value in grams.
- The value is the conversion factor of the unit in relation to grams.
"""
class weights_and_masses:
    """
    Weight and mass units with their conversion factors in grams.
    The conversion factors are based on the metric system and common
    imperial units. The base unit is Gram (g).
    
    The conversion factors are as follows:
    - 1 Carat = 0.02 grams
    - 1 Milligram = 0.001 grams
    - 1 Centigram = 0.01 grams
    - 1 Decigram = 0.1 grams
    - 1 Gram = 1 gram (base unit)
    - 1 Decagram = 10 grams
    - 1 Hectogram = 100 grams
    - 1 Kilogram = 1000 grams
    - 1 Metric Ton = 1000000 grams
    - 1 Ounce = 28.3495 grams
    - 1 Pound = 453.592 grams
    - 1 Stone = 6350.29 grams
    - 1 Short Ton = 907185 grams
    - 1 Long Ton = 1016047 grams
    """
    Carat = weight_and_mass("Carat", 0.02)
    Milligram = weight_and_mass("Milligram", 0.001)
    Centigram = weight_and_mass("Centigram", 0.01)
    Decigram = weight_and_mass("Decigram", 0.1)
    Gram = weight_and_mass("Gram", 1.0) # unit base
    Decagram = weight_and_mass("Decagram", 10.0)
    Hectogram = weight_and_mass("Hectogram", 100.0)
    Kilogram = weight_and_mass("Kilogram", 1000.0)
    Metric_Ton = weight_and_mass("Metric Ton", 1000000.0)
    Ounce = weight_and_mass("Ounce", 28.3495)
    Pound = weight_and_mass("Pound", 453.592)
    Stone = weight_and_mass("Stone", 6350.29)
    Short_Ton = weight_and_mass("Short Ton", 907185.0)
    Long_Ton = weight_and_mass("Long Ton", 1016047.0)

    """
    This method converts a value from one weight or mass unit to another.
    Args:
        value (float): The amount to convert.
        origin (str): The weight or mass unit to convert from.
        destin (str): The weight or mass unit to convert to.
    Returns:
        float: The converted amount.
    Raises:
        AttributeError: If the origin or destination unit is not defined in the class.
    """
    def convert_weight_and_mass(self, value, origin, destin):
        value = float(value)
        origin_unit = getattr(weights_and_masses, origin.title().replace(" ", "_")) # Convert to title case and replace spaces with underscores
        destin_unit = getattr(weights_and_masses, destin.title().replace(" ", "_")) # Convert to title case and replace spaces with underscores
        return (value * origin_unit.value) / destin_unit.value 
    