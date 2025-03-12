class InvalidUserName(Exception):
    """Custom exception for invalid user name inputs."""
    pass


def validate_name(name):
    """
    Validates a user name based on the specified criteria.

    Args:
        name (str): The name to validate

    Raises:
        InvalidUserName: If the name doesn't meet validation criteria
    """
    # Check if name is at least 2 characters long
    if len(name) < 2:
        raise InvalidUserName("Name must be at least 2 characters long.")

    # Check if name contains only letters
    if not name.isalpha():
        raise InvalidUserName("Name must contain only letters.")

    # Check if the first letter is uppercase
    if not name[0].isupper():
        raise InvalidUserName("Name must start with an uppercase letter.")

    # If all checks pass, the name is valid
    return True


def get_valid_name():
    """
    Prompts the user to enter a valid name and handles validation.

    Returns:
        str: A valid name that meets all criteria
    """
    while True:
        try:
            name = input("Please enter your name: ")
            validate_name(name)
            return name
        except InvalidUserName as e:
            print(f"Error: {e} Please try again.")


# Example usage
if __name__ == "__main__":
    print("Welcome to the name validator program!")

    try:
        valid_name = get_valid_name()
        print(f"Hello, {valid_name}! Your name is valid.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")