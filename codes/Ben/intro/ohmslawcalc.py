# program that asks the user if they want to calculate the current, voltage, or resistance using Ohm's Law. If they choose current, the program will ask for voltage and resistance and calculate the current. If they choose voltage, the program will ask for current and resistance and calculate the voltage. If they choose resistance, the program will ask for voltage and current and calculate the resistance.
choice = input("Do you want to calculate current, voltage, or resistance? (c/v/r): ")
if choice == "c":
    voltage = float(input("Enter the voltage (V): "))
    resistance = float(input("Enter the resistance (Ω): "))
    current = voltage / resistance
    print("The current is:", current, "A")
elif choice == "v":
    current = float(input("Enter the current (A): "))
    resistance = float(input("Enter the resistance (Ω): "))
    voltage = current * resistance
    print("The voltage is:", voltage, "V")
elif choice == "r":
    voltage = float(input("Enter the voltage (V): "))
    current = float(input("Enter the current (A): "))
    resistance = voltage / current
    print("The resistance is:", resistance, "Ω")
else:
    print("Invalid choice. Please enter 'c', 'v', or 'r'.")
    
