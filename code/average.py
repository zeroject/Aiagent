# filename: average.py

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        float: The average of the numbers.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")
    
    return sum(numbers) / len(numbers)

# Example usage
numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(f"The average is: {average}")