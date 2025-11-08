
# average_calculator.py

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    print("Welcome to Average Calculator!")
    try:
        user_input = input("Enter numbers separated by spaces: ")
        numbers = [float(num) for num in user_input.split()]
        avg = calculate_average(numbers)
        print(f"The average is: {avg}")
    except ValueError:
        print("Please enter only valid numbers.")

if __name__ == "__main__":
    main()
# this is for version 2