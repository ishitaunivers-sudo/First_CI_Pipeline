
"""Program 26: Find the sum using a loop."""


def sum_of_list(numbers):
    total = 0

    for number in numbers:
        total += number

    return total


if __name__ == "__main__":
    print(sum_of_list([1, 2, 3, 4]))
