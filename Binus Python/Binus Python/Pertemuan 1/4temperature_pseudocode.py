Title: Converting temperature units
Declaration: option, temperature
Implementation:

Display Options
Display 1 - Celsius to Fahrenheit
Display 2 - Celsius to Kelvin
Display 3 - Fahrenheit to Celsius
Display 4 - Fahrenheit to Kelvin
Display 5 - Kelvin to Celsius
Display 6 - Kelvin to Fahrenheit

if option = 1:
    input temperature
    temperature = celsius
    fahrenheit = (celsius * 1.8) + 32
    Display fahrenheit
elif option = 2:
    input temperature
    temperature = celsius
    kelvin = celsius + 273.15
    Display kelvin
elif option = 3:
    input temperature
    temperature = fahrenheit
    celsius = (fahrenheit - 32) / 1.8
    Display celsius
elif option = 4:
    input temperature
    temperature = fahrenheit
    kelvin = (fahrenheit - 32) / 1.8 + 273.15
    Display kelvin
elif option = 5:
    input temperature
    temperature = kelvin
    celsius = kelvin - 273.15
    Display celsius
elif option = 6:
    input temperature
    temperature = kelvin
    fahrenheit = (kelvin - 273.15) * 1.8 + 32
else:
    Display invalid option
    