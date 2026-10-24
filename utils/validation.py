def get_non_empty_input(message):
    """Ask for input until the user enters a non-empty value."""
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Error: This field cannot be empty.")
def get_positive_int(message):
    """Get a positive integer from the user."""
    while True:
        try:
            value = int(input(message))
            if value > 0:
                return value
            print("Error: Enter a number greater than zero.")
        except ValueError:
            print("Error: Please enter a valid whole number.")
def get_non_negative_int(message):
    """Get an integer that can be zero or greater."""
    while True:
        try:
            value = int(input(message))
            if value >= 0:
                return value
            print("Error: Number cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid whole number.")
def get_positive_float(message):
    """Get a positive decimal number."""
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            print("Error: Price must be greater than zero.")
        except ValueError:
            print("Error: Please enter a valid number.")
