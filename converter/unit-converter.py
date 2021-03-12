#!/usr/bin/python
# Script to do simple conversions

# Main menu to select options
def menu():
    print("--------------------welcome to Ubique!--------------------".title())
    exit_request = False
    while not exit_request:
        print("1. Temperature\n"
              "2. Distance\n"
              "3. Weight\n"
              "4. Exit")
        user_option = int(input("please enter your intended option (1, 2, 3, 4): ".title()))
        if user_option == 1:
            convert_temperature()
        elif user_option == 2:
            distance_menu()
        elif user_option == 3:
            weight_menu()
        elif user_option == 4:
            print("Bye!")
            exit_request = True
        else:
            print("please enter the option number correctly.".title())


# Converts the input temperature to C/F
def convert_temperature():
    exit_temp = False
    while not exit_temp:
        temperature = float(input("please enter the temperature: ".title()))
        temperature_option = input("please define the temperature type (C/F) or 'B' to return to main menu: ".title())

        if validate_temperature_range(temperature, temperature_option):
            if temperature_option.lower() == 'c':
                print(f"{convert_celsius_to_fahrenheit(temperature)} F\n")
                exit_temp = True
            elif temperature_option.lower() == 'f':
                print(f"{convert_fahrenheit_to_celsius(temperature)} C\n")
                exit_temp = True
            elif temperature_option.lower() == 'b':
                exit_temp = True
            else:
                print(
                    "please enter either 'C' or 'F' in small/capital to define temperature type and 'B' to return.".title())
                exit_temp = False
        else:
            print("input range is not correct.\n".title())
            return
    return


# Checks if the entered temperature range is correct
def validate_temperature_range(temperature, temperature_option):
    if (0 <= temperature <= 100 and (temperature_option.lower() == 'c') or (
            32 <= temperature <= 212 and (temperature_option.lower() == 'f'))):
        return True
    return False


# Converts Celsius to Fahrenheit
def convert_celsius_to_fahrenheit(t):
    result = (t * (9 / 5)) + 32
    return float("{:.2f}".format(result))


# Converts Fahrenheit to Celsius
def convert_fahrenheit_to_celsius(t):
    result = (t - 32) * (5 / 9)
    return float("{:.2f}".format(result))


# Menu to select conversions of mm, cm, inch or m to each other
def distance_menu():
    exit_dist = False
    while not exit_dist:

        distance = float(input("please enter the distance: ".title()))
        source_distance_type = input("please enter the source_distance".title() + " (mm, cm, inch, m) : ")
        destination_distance_type = input("please enter the source_distance".title() + " (mm, cm, inch, m) : ")

        if validate_distance_type(source_distance_type) and validate_distance_type(destination_distance_type):
            if source_distance_type.lower() == "cm" and destination_distance_type.lower() == "mm":
                print("{:.4f}".format(cm_to_mm(distance)) + " mm\n")
                exit_dist = True
            elif source_distance_type.lower() == "cm" and destination_distance_type.lower() == "m":
                print("{:.4f}".format(cm_to_m(distance)) + " m\n")
                exit_dist = True
            elif source_distance_type.lower() == "cm" and destination_distance_type.lower() == "inch":
                print("{:.4f}".format(cm_to_inch(distance)) + " inch\n")
                exit_dist = True
            elif source_distance_type.lower() == "mm" and destination_distance_type.lower() == "m":
                print("{:.4f}".format(mm_to_m(distance)) + " m\n")
                exit_dist = True

            elif source_distance_type.lower() == "mm" and destination_distance_type.lower() == "cm":
                print("{:.4f}".format(mm_to_cm(distance)) + " cm\n")
                exit_dist = True

            elif source_distance_type.lower() == "mm" and destination_distance_type.lower() == "inch":
                print("{:.4f}".format(mm_to_inch(distance)) + " inch\n")
                exit_dist = True

            elif source_distance_type.lower() == "m" and destination_distance_type.lower() == "mm":
                print("{:.4f}".format(m_to_mm(distance)) + " mm\n")
                exit_dist = True

            elif source_distance_type.lower() == "m" and destination_distance_type.lower() == "cm":
                print("{:.4f}".format(m_to_cm(distance)) + " cm\n")
                exit_dist = True

            elif source_distance_type.lower() == "m" and destination_distance_type.lower() == "inch":
                print("{:.4f}".format(m_to_inch(distance)) + " inch\n")
                exit_dist = True

            elif source_distance_type.lower() == "inch" and destination_distance_type.lower() == "mm":
                print("{:.4f}".format(inch_to_mm(distance)) + " mm\n")
                exit_dist = True

            elif source_distance_type.lower() == "inch" and destination_distance_type.lower() == "cm":
                print("{:.4f}".format(inch_to_cm(distance)) + " cm\n")
                exit_dist = True

            elif source_distance_type.lower() == "inch" and destination_distance_type.lower() == "m":
                print("{:.4f}".format(inch_to_m(distance)) + " m\n")
                exit_dist = True
            else:
                print("please enter the distance types correctly.".title())
                exit_dist = False
        else:
            print("there is a type mismatch.\n".title())
            return


# Checks if the type of the distance (e.g. cm) is acceptable
def validate_distance_type(d):
    if d.lower() == 'cm' or d.lower() == 'mm' or d.lower() == 'm' or d.lower() == 'inch':
        return True
    return False


# Distance conversions
def cm_to_mm(dist):
    return dist * 10


def cm_to_m(dist):
    return dist * 0.01


def cm_to_inch(dist):
    return dist * 0.3937


def m_to_mm(dist):
    return dist * 1000


def m_to_cm(dist):
    return dist * 100


def m_to_inch(dist):
    return dist * 39.37


def mm_to_m(dist):
    return dist * 0.001


def mm_to_cm(dist):
    return dist * 0.1


def mm_to_inch(dist):
    return dist * 0.03937


def inch_to_cm(dist):
    return dist * 2.54


def inch_to_mm(dist):
    return dist * 25.4


def inch_to_m(dist):
    return dist * 0.0254


# Weight menu to select the conversion type (Kg/g)
def weight_menu():
    exit_weight = False
    while not exit_weight:
        weight = float(input("please enter the weight: ".title()))
        weight_type = input("please enter the weight".title() + " (Kg/g): ")

        if validate_weight_type(weight_type):
            if weight_type.lower() == "kg":
                print("{:.2}".format(kg_to_g(weight)) + " g\n")
                exit_weight = True
            elif weight_type.lower() == "g":
                print("{:.2}".format(g_to_kg(weight)) + " Kg\n")
                exit_weight = True
        else:
            print("The entered type is not acceptable.\n".title())
            exit_weight = False


# Checks if the weight type (e.g. Kg) is acceptable
def validate_weight_type(wt):
    if wt.lower() == "kg" or wt.lower() == "g":
        return True
    return False


# Weight conversions
def kg_to_g(w):
    return w * 1000


def g_to_kg(w):
    return w * 0.001


# Main function to start
menu()
