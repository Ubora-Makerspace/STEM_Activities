# program called show_lyrics which prints "Bob Marley"
# also a second function which asks the user how many times
# to print "Bob Marley" and keeps asking until the user types "exit"


def show_lyrics():
    print("Bob Marley")


def print_bob_marley():
    while True:
        user_input = input("How many times do you want to print 'Bob Marley'? (type 'exit' to stop): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        try:
            number = int(user_input)

            for _ in range(number):
                show_lyrics()

        except ValueError:
            print("Please enter a number or type 'exit'.")


print_bob_marley()