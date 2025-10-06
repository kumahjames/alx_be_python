def safe_divide(numerator, denominator):
    """
    Performs division while safely handling ZeroDivisionError and ValueError.
    Returns the result or an appropriate error message.
    """
    try:
        # Attempt to convert arguments to float
        num = float(numerator)
        den = float(denominator)
        
        # Perform the division
        result = num / den
        
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
        
    except ValueError:
        # Handle non-numeric input for either numerator or denominator
        return "Error: Please enter numeric values only."

# Example of how to use the function
if __name__ == "__main__":
    print(safe_divide("10", "5"))   # Normal Division
    print(safe_divide("10", "0"))   # Division by Zero
    print(safe_divide("ten", "5"))  # Invalid Input (Non-numeric)