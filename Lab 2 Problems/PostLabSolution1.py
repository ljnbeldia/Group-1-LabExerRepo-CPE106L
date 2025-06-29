# stats.py10

def mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def median(numbers):
    if not numbers:
        return 0
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 1:
        return sorted_nums[mid]
    else:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2


def mode(numbers):
    if not numbers:
        return 0
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]
    return min(modes)


def main():

    user_input = input("Enter numbers separated by spaces: ")


    try:
        numbers = [float(x) for x in user_input.split()]
    except ValueError:
        print("Please enter valid numbers.")
        return

    print("Data:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Mode:", mode(numbers))


if __name__ == "__main__":
    main()
