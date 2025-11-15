# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.

def max_two_in_list(numbers):
    numbers = list(numbers)
    if len(numbers) == 1:
        return numbers[0], None

    max1 = max(numbers)
    while max1 in numbers:
        numbers.remove(max1)

    if not numbers:
        return max1, None
    
    max2 = max(numbers)
    return max1, max2



# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    num = min(numbers)
    while num <= max(numbers):
        if numbers.count(num) > 1:
            numbers.remove(num)
        else:
            num += 1
            continue

    numbers.sort()

    return numbers

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(array):
    list = array[:]
    for i in range(1, len(list)):
        list[i] = list[i] + list[i - 1]

    return list

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    transposed_matrix = []
    for j in range(len(matrix[0])):
        transposed_matrix.append([i[j] for i in matrix])

    return transposed_matrix

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(list, step):
    i = 0
    result = []
    n = 1

    while i < len(list):
        if i == 0:
            result.append(list[i])
            i += 1
        elif i == step * n:
            result.append(list[i])
            n += 1
            i += 1
        else:
            i += 1

    return result

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    product = sum([a * b for a, b in zip(list1, list2)])
    return product

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    matrix2_transposed = list(zip(*matrix2))
    result = [
        [sum(a * b for a, b in zip(row, column)) for column in matrix2_transposed]
        for row in matrix1
    ]
    
    return result

