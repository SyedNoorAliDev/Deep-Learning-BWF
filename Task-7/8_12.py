def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("Making a sandwich with the following items:")
    for item in items:
        print("- " + item)
    print("Enjoy your sandwich!")

# Example usage
make_sandwich('Chicken', 'cheese', 'Ketchup', 'mayo')
make_sandwich('original', 'egg', 'cheese')
make_sandwich('butter', 'jelly')
