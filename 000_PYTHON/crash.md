# PYTHON PROGRAMMING CRASH COURSE
## Smart Classroom Energy Monitor

### Problem Statement

A school wants to monitor electricity consumption in its computer laboratory. You have been asked to write a Python program that calculates the laboratory's energy consumption and determines its usage status.

### Instructions

Write a Python program that does the following:

1. Collect the total number of computers, number of computers in use, power consumption per computer (watts), and number of operating hours.
2. Calculate:
   - Number of computers not in use.
   - Total power consumption.
   - Total energy consumption in watt-hours (Wh).
   - Percentage of computers in use.
3. Classify energy consumption:
   - Above 10,000 Wh: High consumption.
   - Above 5,000 Wh up to 10,000 Wh: Moderate consumption.
   - 5,000 Wh or below: Low consumption.
4. Determine whether the laboratory has high activity. This occurs when at least 80% of computers are in use AND they have operated for at least 4 hours.
5. Use a function called `calculate_energy()` to determine the energy consumption status.
6. Declare a global variable called `energy_limit` with a value of 10,000. Inside the function, create a local variable called `energy_status`.

### Starter Code

Complete the following Python program. Fill in the missing sections.

```python
energy_limit = 10000

total_computers = input("Total computers: ")#CHANGE THE HOURS USED TO AN INT
computers_in_use = input("Computers in use: ")#CHANGE THE HOURS USED TO AN INT
power_per_computer = float(input("Power per computer (W): ")) 
hours_used = input("Operating hours: ")  #CHANGE THE HOURS USED TO A FLOAT

computers_not_in_use = 
total_power = 
energy_consumed = 
percentage_in_use = 

# Create a function
def calculate_energy():

    energy_status = ""

    if __________:
        energy_status = "High consumption"
    elif __________:
        energy_status = "Moderate consumption"
    else:
        energy_status = "Low consumption"

    print("Energy Status:", energy_status)


if __________ and __________:
    activity = "High laboratory activity"
else:
    activity = "Normal laboratory activity"


# Display results
print("\n--- ENERGY MONITORING REPORT ---")
print("Computers not in use:", __________________)
print("Total power:", ________ "W")
print("Energy consumed:", energy_consumed, "Wh")
print("Percentage in use:", percentage_in_use, "%")

calculate_energy()

print("Activity:", activity)
```

### Submission
 Test your program with at least two different sets of input values and ensure that the results change accordingly.