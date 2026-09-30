# Voltage = 5
# current = 2
# resistance = Voltage / current
# print("The resistance is", resistance,"ohms")

try:  
    voltage = float(input("enter your voltage: "))
    current = float(input("enter your current: "))
    resistance = voltage / current
    print("The resistance is", resistance,"ohms")
except ValueError:
    print("Please enter a valid number.")
    
if current == 0 and voltage != 0:
    print("The resistance is infinite (open circuit).")