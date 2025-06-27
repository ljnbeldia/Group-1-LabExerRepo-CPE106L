# Programming Problem 1:
# Statisticians would like to have a set of functions to compute
# the median and mode of a list of numbers. The median is the number
# that would appear at the midpoint of a list if it were sorted.
# The mode is the number that appears most frequently in the list.
# Define these functions in a module named stats.py. Also include a
# function named mean, which computes the average of a set of numbers.
# Each function expects a list of numbers as an argument and returns a
# single number.

from collections import Counter
import random

def meanCalc (NoList):
    summation = 0
    count = 0
    for numbers in NoList:
        summation += numbers
        count += 1
    mean = summation / count
    return mean

def GetMedian(NoList):
    if not NoList:
        return None  # Handle empty list
    sorted_list = sorted(NoList)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        # Even number of elements: average the two middle values
        median = (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        # Odd number of elements: take the middle value
        median = sorted_list[mid]
    return median

def GetMode(NoList):
    if not NoList:
        return None, 0  # Handle empty list
    counts = Counter(NoList)
    mode, count = counts.most_common(1)[0]
    return mode, count

if __name__ == "__main__":
    print("Choose input method:")
    print("1. Generate a random list")
    print("2. Enter your own list")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        n = int(input("How many numbers in the random list? "))
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
        NoList = [random.randint(lower, upper) for _ in range(n)]
        print("Random list generated:", NoList)
    elif choice == "2":
        NoList = list(map(float, input("Enter numbers separated by spaces: ").split()))
    else:
        print("Invalid choice.")
        exit()

    print("Mean:", meanCalc(NoList))
    
    print("Median:", GetMedian(NoList))

    mode, count = GetMode(NoList)
    print("Mode:", mode, "Count:", count)
