def main():
    filename = input("Enter the filename: ")
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    lines = [line.rstrip('\n') for line in lines]
    num_lines = len(lines)

    if num_lines == 0:
        print("The file is empty.")
        return

    while True:
        print(f"\nThe file has {num_lines} lines.")
        try:
            line_num = int(input(f"Enter a line number (1-{num_lines}, or 0 to quit): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if line_num == 0:
            print("Exiting program.")
            break
        elif 1 <= line_num <= num_lines:
            print(f"Line {line_num}: {lines[line_num - 1]}")
        else:
            print("Invalid line number.")

if __name__ == "__main__":
    main()