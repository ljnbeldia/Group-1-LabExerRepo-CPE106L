# line_navigator.py

def main():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found. Please check the filename and try again.")
        return

    total_lines = len(lines)
    print(f"\nFile loaded successfully with {total_lines} lines.")

    while True:
        try:
            user_input = int(input(f"\nEnter a line number (1 to {total_lines}, or 0 to quit): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input == 0:
            print("Exiting program.")
            break
        elif 1 <= user_input <= total_lines:
            print(f"Line {user_input}: {lines[user_input - 1].rstrip()}")
        else:
            print(f"Invalid line number. Please enter a number between 1 and {total_lines}.")


if __name__ == "__main__":
    main()
