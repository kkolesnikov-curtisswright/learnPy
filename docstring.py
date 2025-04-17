def celsius_to_fahrenheit(celsius: float) -> float:

    """
    Calculates temperature in Fahrenheit from Celsius

    Args:

        celsius - temperature in Celsius (float)

    Returns:

        temperature in fahrenheit (float)

    Example:
            celsius_to_fahrenheit(32)
            >>> 89.6
    """
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit: float) -> float:

    """
    Calculates temperature in Celsius from Fahrenheit

    Args:

        fahrenheit - temperature in Fahrenheit (float)

    Returns:

        temperature in Celsius (float)

    Example:
            fahrenheit_to_celsius(32)
            >>> 0.0
    """
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temperature, unit):

    """
    Converts temperature between Celsius and Fahrenheit

    Args:

        temperature - temperature value (float)
        unit - temperature unit ("C" for Celsius or "F" for Fahrenheit) (string)

    Returns:

        converted temperature (Celsius or Fahrenheit) (float)

    """

    if unit == "C":
        converted_temperature = celsius_to_fahrenheit(temperature)
    elif unit == "F":
        converted_temperature = fahrenheit_to_celsius(temperature)
    else:
        raise ValueError("Only 'F' and 'C' values acceptable")
    
    converted_temperature = round(converted_temperature, 2)
    
    return converted_temperature

import logging

logging.basicConfig(level=logging.INFO)
logging.info(f"Converted temperature: {convert_temperature(32, 'F')}")