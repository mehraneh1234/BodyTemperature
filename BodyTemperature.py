#Mehraneh - 30062786
#Session2 - 09/02/2023
#AT2.3 Q1.
#that takes input from the user and converts that String input to a float datatype.
#You are to prompt the user to input their body temperature

# input temperature
input_temperature = float(input("Please enter your body temperature:"))

# check normal body temperature
if 38 > input_temperature >= 37:
    print("Normal Body temperature")
# check fever
elif 39 > input_temperature >= 38:
    print("Is a Fever")
# check high fever
elif 40 > input_temperature >= 39:
    print("Is a High Fever")
# check very high fever
elif 41 > input_temperature >= 40:
    print("Is A Very High Fever")
# check for serious emergency
elif input_temperature >= 41:
    print("Is A Serious Emergency")
# check the temperature is out of range
else:
    print("The temperature is out of range")
    
