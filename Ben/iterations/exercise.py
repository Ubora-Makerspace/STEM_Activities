def print_instructions():
    print("=" * 45)
    print("         NUMBER CALCULATOR INSTRUCTIONS")
    print("=" * 45)
    print("- Enter any number (integer or decimal) one at a time.")
    print("- Type 'done' whenever you want to finish.")
    print("- Non-numeric inputs will show an error and be ignored.")
    print("=" * 45 + "\n")

# Display instructions first
print_instructions()

total = 0.0
count = 0

while True:
    user_input = input("Enter a number (or 'done'): ")
    
    # Check if user wants to stop
    if user_input.strip().lower() == "done":
        break
    
    # Attempt to convert the input to a float
    try:
        number = float(user_input)
        total += number
        count += 1
    except ValueError:
        print("Invalid input! Please enter a valid number or 'done'.")
        continue

# Display results after exiting the loop
print("\n--- Summary ---")
if count > 0:
    average = total / count
    print(f"Total:   {total}")
    print(f"Count:   {count}")
    print(f"Average: {average}")
else:
    print("No valid numbers were entered.")