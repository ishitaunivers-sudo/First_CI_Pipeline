
"""Program 23: Sort a list using Bubble Sort."""


def bubble_sort(numbers):
    result = numbers.copy()
    n = len(result)

    for i in range(n):
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = (
                    result[j + 1], result[j]
                )

    return result


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1]))
