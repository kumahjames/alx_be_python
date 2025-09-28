from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in YYYY-MM-DD HH:MM:SS format"""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date

def calculate_future_date():
    """Calculate and return a future date based on user input"""
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
        return future_date
    except ValueError:
        print("Please enter a valid number of days.")

def main():
    """Main function to run both parts of the program"""
    # Part 1: Display current date and time
    current_date = display_current_datetime()
    
    # Part 2: Calculate future date
    future_date = calculate_future_date()

if __name__ == "__main__":
    main()