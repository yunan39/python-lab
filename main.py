from utils import square, is_even, celsius_to_fahrenheit

def main():
    try :
        user_input = float(input("Enter a number: "))
        
        # Calculate square
        sq_result = square(user_input)
        
        # Determine even/odd
        even_result = is_even(user_input)
        parity_str = "even" if even_result else "odd"
        
        # Calculate Fahrenheit equivalent
        f_result = celsius_to_fahrenheit(user_input)
        
        print(f"\n--- Results for {user_input} ---")
        print(f"Square: {sq_result}")
        print(f"Parity: The number is {parity_str}.")
        print(f"Temperature: {user_input}°C is {f_result}°F")
        
    except ValueError:
        print("Invalid input. Please enter a valid numerical value.")

if __name__ == "__main__":
    main()