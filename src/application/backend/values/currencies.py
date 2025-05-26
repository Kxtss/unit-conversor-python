"""
This module contains the currency class and the currencies class.
- The currency class represents a single currency with its name and value.
- The currencies class contains several predefined currency instances and
  provides a method to convert between different currencies.
- The exchange rates are updated as of May 17, 2025.

The currencies class includes the following currencies:
- USD (United States Dollar)
- MXN (Mexican Peso)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- KRW (South Korean Won)
- CAD (Canadian Dollar)
- AUD (Australian Dollar)
"""

class currency:
    def __init__(self, name, value):
        self.name = name # name of the currency
        self.value = value # value of the currency in relation to USD

"""
This class represents a currency with its name and value in USD.
- The value is the exchange rate of the currency in relation to USD.
"""

class currencies:
    """Exchange rates updated as of 26, May, 2025"""

    USD = currency("USD", 1)  # unit base
    MXN = currency("MXN", 0.052)  # 1 mxn = 0.052 usd
    EUR = currency("EUR", 1.14)  # 1 eur = 1.14 usd
    GBP = currency("GBP", 1.36)  # 1 gbp = 1.36 usd
    JPY = currency("JPY", 0.007)  # 1 jpy = 0.007 usd
    KRW = currency("KRW", 0.00073)  # 1 krw = 0.00073 usd
    CAD = currency("CAD", 0.73)  # 1 cad = 0.73 usd
    AUD = currency("AUD", 0.65)  # 1 aud = 0.65 usd
    """This method converts a value from one currency to another.
    Args:
        value (float): The amount to convert.
        origin (str): The currency to convert from.
        destin (str): The currency to convert to.
        Returns:
        float: The converted amount.
    """

    def convert_currency(self, value, origin, destin):
        value = float(value)
        origin_unit = getattr(currencies, origin)
        destin_unit = getattr(currencies, destin)
        return (value * origin_unit.value) / destin_unit.value
