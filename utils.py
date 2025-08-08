def get_int_input(prompt, min_val=None, max_val=None):
    """Get a valid integer from the user with optional min/max range."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError(f"Number must be at least {min_val}.")
            if max_val is not None and value > max_val:
                raise ValueError(f"Number must not exceed {max_val}.")
            return value
        except ValueError as e:
            print(f"{e} Please try again.")
