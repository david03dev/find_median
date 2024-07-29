def find_median(a, b, c):
    # Create a list of the three numbers
    numbers = [a, b, c]
    
    # Sort the list
    numbers.sort()
    
    # The median is the middle element in the sorted list
    median = numbers[1]
    
    return median

# Example usage
if __name__ == "__main__":
    # Input three numbers from the user
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        # Find and print the median
        median = find_median(num1, num2, num3)
        print(f"The median is: {median}")
        
    except ValueError:
        print("Please enter valid numbers.")
