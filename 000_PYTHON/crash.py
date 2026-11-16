energy_limit = 10000

total_computers = input("Total computers: ")
total_computers = int(total_computers)
computers_in_use = input("Computers in use: ")
computers_in_use = int(computers_in_use)
power_per_computer = float(input("Power per computer (W): "))
hours_used = float(input("Operating hours: "))

computers_not_in_use = total_computers - computers_in_use
total_power = computers_in_use * power_per_computer 
energy_consumed = total_power * hours_used
percentage_in_use = (computers_in_use / total_computers) * 100

def calculate_energy():

    energy_status = "" #local variable

    if energy_consumed > energy_limit:
        energy_status = "High consumption"
    elif 5000 < energy_consumed and energy_consumed <= energy_limit:
        energy_status = "Moderate consumption"
    else:
        energy_status = "Low consumption"

    print("Energy Status:", energy_status)

calculate_energy()


if percentage_in_use >=80 and hours_used >=4:
    activity = "High laboratory activity"
else:
    activity = "Normal laboratory activity"

print("Activity:", activity)

print("\n--- ENERGY MONITORING REPORT ---")
print("Computers not in use:", computers_not_in_use)
print("Total power:", total_power, "W")
print("Energy consumed:", energy_consumed, "Wh")
print("Percentage in use:", percentage_in_use, "%")