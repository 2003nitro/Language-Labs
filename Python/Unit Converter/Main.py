#################################################
# Author: Adam Wilkins
# Date Created: 7/18/2026
# Date Updated: 7/23/2026
# Description: Basic unit converter application
################################################

def LengthConverter(startUnit, endUnit, value):
    """
    # Author: Adam Wilkins
    # Date Created: 7/22/2026
    # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for length measurements.
    """

    baseUnit = 0 # Convert to base unit (meters)
    if startUnit == "6": # already in meters so skip all if statements
        pass
    elif startUnit == "1": # millimeter
        baseUnit = value * 0.001
    elif startUnit == "2": # centimeter
        baseUnit = value * 0.01
    elif startUnit == "3": # inch
        baseUnit = value * 0.0254
    elif startUnit == "4": # foot
        baseUnit = value * 0.3048
    elif startUnit == "5": # yard
        baseUnit = value * 0.9144
    elif startUnit == "7": # kilometer
        baseUnit = value * 1000
    elif startUnit == "8": # mile
        baseUnit = value * 1609.344

    if endUnit == "6": # meters
        return baseUnit
    elif endUnit == "1": # millimeter
        return baseUnit * 1000
    elif endUnit == "2": # centimeter
        return baseUnit * 100
    elif endUnit == "3": # inch
        return baseUnit / 0.0254
    elif endUnit == "4": # foot
        return baseUnit / 0.3048
    elif endUnit == "5": # yard
        return baseUnit / 0.9144
    elif endUnit == "7": # kilometer
        return baseUnit / 1000
    elif endUnit == "8": # mile
        return baseUnit / 1609.344

def WeightConverter(startUnit, endUnit, value):
    """
    # Author: Adam Wilkins
    # Date Created: 7/22/2026
    # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for weight measurements.
    """

    baseUnit = 0 # Convert to base unit (grams)
    if startUnit == "2": # already in grams so skip all if statements
        pass
    elif startUnit == "1": # milligram
        baseUnit = value * 0.001
    elif startUnit == "3": # ounce
        baseUnit = value * 28.3495
    elif startUnit == "4": # pound
        baseUnit = value * 453.592
    elif startUnit == "5": # kilogram
            baseUnit = value * 1000
    elif startUnit == "6": # stone
        baseUnit = value * 6350.293
    elif startUnit == "7": # US ton
        baseUnit = value * 907184.74
    elif startUnit == "8": # metric ton
        baseUnit = value * 1000000

    if endUnit == "2": # grams
        return baseUnit
    elif endUnit == "1": # milligram
        return baseUnit * 1000
    elif endUnit == "3": # ounce
        return baseUnit / 28.3495
    elif endUnit == "4": # pound
        return baseUnit / 453.592
    elif endUnit == "5": # kilogram
        return baseUnit / 1000
    elif endUnit == "6": # stone
        return baseUnit / 6350.293
    elif endUnit == "7": # US ton
        return baseUnit / 907184.74
    elif endUnit == "8": # metric ton
        return baseUnit / 1000000
    


    

def TemperatureConverter(startUnit, endUnit, value):
    """
    # Author: Adam Wilkins
    # Date Created: 7/22/2026
    # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for temperature measurements.
    """

    baseUnit = 0 # Convert to base unit (Celsius)
    if startUnit == "1": # Celsius
        baseUnit = value
    elif startUnit == "2": # Fahrenheit
        baseUnit = (value - 32) * 5/9
    elif startUnit == "3": # Kelvin
        baseUnit = value - 273.15

    if endUnit == "1": # Celsius
        return baseUnit
    elif endUnit == "2": # Fahrenheit
        return baseUnit * 9/5 + 32
    elif endUnit == "3": # Kelvin
        return baseUnit + 273.15

def VolumeConverter(startUnit, endUnit, value):
    """
        # Author: Adam Wilkins
        # Date Created: 7/22/2026
        # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for volume measurements.
    """

    baseUnit = 0 # Convert to base unit (liters)
    if startUnit == "8": # already in liters so skip all if statements
        pass
    elif startUnit == "1": # milliliter
        baseUnit = value * 0.001
    elif startUnit == "2": # Teaspoon
        baseUnit = value * 0.00492892
    elif startUnit == "3": # Tablespoon
        baseUnit = value * 0.0147868
    elif startUnit == "4": # Fluid Ounce
        baseUnit = value * 0.0295735
    elif startUnit == "5": # Cup
        baseUnit = value * 0.236588
    elif startUnit == "6": # Pint
        baseUnit = value * 0.473176
    elif startUnit == "7": # Quart
        baseUnit = value * 0.946353
    elif startUnit == "9": # Gallon
        baseUnit = value * 3.78541

    if endUnit == "8": # liters
        return baseUnit
    elif endUnit == "1": # milliliter
        return baseUnit * 1000
    elif endUnit == "2": # Teaspoon
        return baseUnit / 0.00492892
    elif endUnit == "3": # Tablespoon
        return baseUnit / 0.0147868
    elif endUnit == "4": # Fluid Ounce
        return baseUnit / 0.0295735
    elif endUnit == "5": # Cup
        return baseUnit / 0.236588
    elif endUnit == "6": # Pint
        return baseUnit / 0.473176
    elif endUnit == "7": # Quart
        return baseUnit / 0.946353
    elif endUnit == "9": # Gallon
        return baseUnit / 3.78541

def TimeConverter(startUnit, endUnit, value):
    """
    # Author: Adam Wilkins
    # Date Created: 7/22/2026
    # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for time measurements.
    """

    baseUnit = 0 # Convert to base unit (seconds)
    if startUnit == "2": # already in seconds so skip all if statements
        pass
    elif startUnit == "1": # Millisecond
        baseUnit = value * 0.001
    elif startUnit == "3": # Minute
        baseUnit = value * 60
    elif startUnit == "4": # Hour
        baseUnit = value * 3600
    elif startUnit == "5": # Day
        baseUnit = value * 86400
    elif startUnit == "6": # Week
        baseUnit = value * 604800

    if endUnit == "2": # seconds
        return baseUnit
    elif endUnit == "1": # Millisecond
        return baseUnit * 1000
    elif endUnit == "3": # Minute
        return baseUnit / 60
    elif endUnit == "4": # Hour
        return baseUnit / 3600
    elif endUnit == "5": # Day
        return baseUnit / 86400
    elif endUnit == "6": # Week
        return baseUnit / 604800

def SpeedConverter(startUnit, endUnit, value):
    """
    # Author: Adam Wilkins
    # Date Created: 7/22/2026
    # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for speed measurements.
    """

    baseUnit = 0 # Convert to base unit (meters per second)
    if startUnit == "2": # already in meters per second so skip all if statements
        pass
    elif startUnit == "1": # Foot per second
        baseUnit = value * 0.3048
    elif startUnit == "3": # Kilometer per hour
        baseUnit = value * 1000 / 3600
    elif startUnit == "4": # Mile per hour
        baseUnit = value * 1609.34 / 3600
    elif startUnit == "5": # Knot
        baseUnit = value * 1852 / 3600

    if endUnit == "2": # meters per second
        return baseUnit
    elif endUnit == "1": # Foot per second
        return baseUnit / 0.3048
    elif endUnit == "3": # Kilometer per hour
        return baseUnit * 3600 / 1000
    elif endUnit == "4": # Mile per hour
        return baseUnit * 3600 / 1609.34
    elif endUnit == "5": # Knot
        return baseUnit * 3600 / 1852

def DataStorageConverter(startUnit, endUnit, value):
    """
    # Author: Adam Wilkins
    # Date Created: 7/22/2026
    # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for data storage measurements.
    """

    baseUnit = 0 # Convert to base unit (bytes)
    if startUnit == "2": # already in bytes so skip all if statements
        pass
    elif startUnit == "1": # Bit
        baseUnit = value * 0.125
    elif startUnit == "3": # Kilobyte
        baseUnit = value * 1024
    elif startUnit == "4": # Megabyte
        baseUnit = value * 1048576
    elif startUnit == "5": # Gigabyte
        baseUnit = value * 1073741824
    elif startUnit == "6": # Terabyte
        baseUnit = value * 1099511627776
    elif startUnit == "7": # Petabyte
        baseUnit = value * 1125899906842624

    if endUnit == "2": # bytes
        return baseUnit
    elif endUnit == "1": # Bit
        return baseUnit / 0.125
    elif endUnit == "3": # Kilobyte
        return baseUnit / 1024
    elif endUnit == "4": # Megabyte
        return baseUnit / 1048576
    elif endUnit == "5": # Gigabyte
        return baseUnit / 1073741824
    elif endUnit == "6": # Terabyte
        return baseUnit / 1099511627776
    elif endUnit == "7": # Petabyte
        return baseUnit / 1125899906842624

def AreaConverter(startUnit, endUnit, value):
    """
    # Author: Adam Wilkins
    # Date Created: 7/22/2026
    # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for area measurements.
    """

    baseUnit = 0 # Convert to base unit (square meters)
    if startUnit == "6": # already in square meters so skip all if statements
        pass
    elif startUnit == "1": # Square Millimeter
        baseUnit = value * 0.000001
    elif startUnit == "2": # Square Centimeter
        baseUnit = value * 0.0001
    elif startUnit == "3": # Square Inch
        baseUnit = value * 0.00064516
    elif startUnit == "4": # Square Foot
        baseUnit = value * 0.092903
    elif startUnit == "5": # Square Yard
        baseUnit = value * 0.836127
    elif startUnit == "7": # Acre
        baseUnit = value * 4046.86
    elif startUnit == "8": # Hectare
        baseUnit = value * 10000
    elif startUnit == "9": # Square Kilometer
        baseUnit = value * 1000000

    if endUnit == "6": # square meters
        return baseUnit
    elif endUnit == "1": # Square Millimeter
        return baseUnit / 0.000001
    elif endUnit == "2": # Square Centimeter
        return baseUnit / 0.0001
    elif endUnit == "3": # Square Inch
        return baseUnit / 0.00064516
    elif endUnit == "4": # Square Foot
        return baseUnit / 0.092903
    elif endUnit == "5": # Square Yard
        return baseUnit / 0.836127
    elif endUnit == "7": # Acre
        return baseUnit / 4046.86
    elif endUnit == "8": # Hectare
        return baseUnit / 10000
    elif endUnit == "9": # Square Kilometer
        return baseUnit / 1000000

def EnergyConverter(startUnit, endUnit, value):
    """
    # Author: Adam Wilkins
    # Date Created: 7/22/2026
    # Purpose: This function takes a starting unit, an ending unit, and a value as input and returns the converted value for energy measurements.
    """
    baseUnit = 0 # Convert to base unit (joules)
    if startUnit == "1": # already in joules so skip all if statements
        pass
    elif startUnit == "2": # Calorie
        baseUnit = value * 4.184
    elif startUnit == "3": # Kilojoule
        baseUnit = value * 1000
    elif startUnit == "4": # Kilocalorie
        baseUnit = value * 4184
    elif startUnit == "5": # BTU
        baseUnit = value * 1055.06
    elif startUnit == "6": # Watt-Hour
        baseUnit = value * 3600
    elif startUnit == "7": # Kilowatt-Hour
        baseUnit = value * 3600000

    if endUnit == "1": # joules
        return baseUnit
    elif endUnit == "2": # Calorie
        return baseUnit / 4.184
    elif endUnit == "3": # Kilojoule
        return baseUnit / 1000
    elif endUnit == "4": # Kilocalorie
        return baseUnit / 4184
    elif endUnit == "5": # BTU
        return baseUnit / 1055.06
    elif endUnit == "6": # Watt-Hour
        return baseUnit / 3600
    elif endUnit == "7": # Kilowatt-Hour
        return baseUnit / 3600000



def unitMenu():
    """
    # Author: Adam Wilkins
    # Date Created: 7/18/2026
    # Purpose: This function displays a menu for the user to select a unit type and then prompts the user to enter a starting unit, an ending unit, and a value to convert. It then calls the appropriate conversion function and displays the result.
    """
    startUnit = ""
    endUnit = ""
    unitType = ""
    print("1. Length")
    print("2. Weight / Mass")
    print("3. Temperature")
    print("4. Volume")
    print("5. Time")
    print("6. Speed")
    print("7. Data Storage")
    print("8. Area")
    print("9. Energy")
    print("0 Exit")
    unitType = input("Please select a unit type: ")

    try:
        match unitType:
            case "1":
                print("Length Units:")
                print("1. Millimeter")
                print("2. Centimeter")
                print("3. Inch")
                print("4. Foot")
                print("5. Yard")
                print("6. Meter")
                print("7. Kilometer")
                print("8. Mile")

                user = input("Please enter a selection in the form of (1-8) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(LengthConverter(startUnit, endUnit, float(user))))

            case "2":
                print("Weight / Mass Units:")
                print("1. Milligram (mg)")
                print("2. Gram (g)")
                print("3. Ounce (oz)")
                print("4. Pound (lb)")
                print("5. Kilogram (kg)")
                print("6. Stone (st)")
                print("7. US Ton (ton)")
                print("8. Metric Ton (t)")

                user = input("Please enter a selection in the form of (1-8) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(WeightConverter(startUnit, endUnit, float(user))))

            case "3":
                print("Temperature Units:")
                print("1. Celsius")
                print("2. Fahrenheit")
                print("3. Kelvin")

                user = input("Please enter a selection in the form of (1-3) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(TemperatureConverter(startUnit, endUnit, float(user))))

            case "4":
                print("Volume Units:")
                print("1. Milliliter (ml)")
                print("2. Teaspoon (tsp)")
                print("3. Tablespoon (tbsp)")
                print("4. Fluid Ounce (fl oz)")
                print("5. Cup")
                print("6. Pint")
                print("7. Quart")
                print("9. Liter (l)")
                print("10. Gallon")

                user = input("Please enter a selection in the form of (1-10) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(VolumeConverter(startUnit, endUnit, float(user))))

            case "5":
                print("Time Units:")
                print("1. Millisecond (ms)")
                print("2. Second (s)")
                print("3. Minute (min)")
                print("4. Hour (hr)")
                print("5. Day (day)")
                print("6. Week (wk)")

                user = input("Please enter a selection in the form of (1-6) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(TimeConverter(startUnit, endUnit, float(user))))

            case "6":
                print("Speed Units:")
                print("1. Feet per Second (ft/s)")
                print("2. Meters per Second (m/s)")
                print("3. Kilometers per Hour (km/h)")
                print("4. Miles per Hour (mph)")
                print("5. Knots (kn)")

                user = input("Please enter a selection in the form of (1-5) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(SpeedConverter(startUnit, endUnit, float(user))))

            case "7":
                print("Data Storage Units:")
                print("1. Bit (b)")
                print("2. Byte (B)")
                print("3. Kilobyte (KB)")
                print("4. Megabyte (MB)")
                print("5. Gigabyte (GB)")
                print("6. Terabyte (TB)")
                print("7. Petabyte (PB)")

                user = input("Please enter a selection in the form of (1-7) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(DataStorageConverter(startUnit, endUnit, float(user))))

            case "8":
                print("Area Units:")
                print("1. Square Millimeter (mm²)")
                print("2. Square Centimeter (cm²)")
                print("3. Square Inch (in²)")
                print("4. Square Foot (ft²)")
                print("5. Square Yard (yd²)")
                print("6. Square Meter (m²)")
                print("7. Acre (ac)")
                print("8. Hectare (ha)")
                print("9. Square Kilometer (km²)")

                user = input("Please enter a selection in the form of (1-9) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(AreaConverter(startUnit, endUnit, float(user))))

            case "9":
                print("Energy Units:")
                print("1. Joule (J)")
                print("2. Calorie (cal)")
                print("3. Kilojoule (kJ)")
                print("4. Kilocalorie (kcal)")
                print("5. British Thermal Unit (BTU)")
                print("6. Watt-hour (Wh)")
                print("7. Kilowatt-hour (kWh)")

                user = input("Please enter a selection in the form of (1-7) for start and end unit: ")
                startUnit, endUnit = user.split("-")
                user = input("Please enter a value to convert: ")
                print("Answer: " + str(EnergyConverter(startUnit, endUnit, float(user))))

            case default:
                print("Please try again with a proper selection")
    except:
        print("Please try again with a proper selection")




def main():
    # Created 7/18/2026

    while True:
        print("1. Enter converter")
        print("2. Exit")
        user = input("Please enter a selection: ")

        if user == "1":
            unitMenu()
    
        elif user == "2":
            break

        else:
            print("Please enter a proper selection \n")


main()