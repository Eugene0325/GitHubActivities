def median(numbers):
    numbers.sort()
    n = len(numbers)
    mid = n // 2
    if n % 2 == 0:
        return (numbers[mid - 1] + numbers[mid]) / 2
    else:
        return numbers[mid]

print("Median:", median([1, 2, 3, 4, 5]))

def mean(numbers):
    return sum(numbers) / len(numbers)

print("Mean:", mean([1, 2, 3, 4, 5]))