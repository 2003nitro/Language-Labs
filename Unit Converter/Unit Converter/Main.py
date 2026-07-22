#################################################
# Author: Adam Wilkins
# Date Created: 7/18/2026
# Date Updated: 7/18/2026
# Description: Basic unit converter application
#################################################


def unitMenu():
    to = ""
    current = ""
    unitType = ""
    print("1. Volume")
    print("2. Temperature")
    print("3. Speed")
    print("4. Mass")
    print("5. Digital Storage")
    print("6. Length")
    print("7. Area")
    user = "Please select a unit type: "

    match user:
        case "1":
            print("US Gallon")
            print("US Quart")
            print("US Pint")
            print("US Cup")
            print("US Ounce")
            print("US Tablespoon")
            print("US Teaspoon")
            
        case "2":
            pass
        case "3":
            pass
        case "4":
            pass
        case "5":
            pass
        case "6":
            pass
        case "7":
            pass
        case default:
            print("Please try again with a proper selection")




def main():
    while True:
        print("1. Enter converter")
        print("2. Exit")
        user = input("Please enter a selection: ")

        if user == "1":
            
    
        elif user == "2":
            break

        else:
            print("Please enter a proper selection \n")