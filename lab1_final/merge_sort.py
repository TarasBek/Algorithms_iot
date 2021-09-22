from enum import Enum

class Sort(Enum):
    ASC = 1
    DESC = 2

def merge_sort(input, order = Sort.ASC):
    comparisons = 0

    if len(input) == 1:
        return

    left_array = input[:len(input) // 2]
    right_array = input[len(input) // 2:]

    merge_sort(left_array, order)
    merge_sort(right_array, order)

    def compare(first_numb, second_numb, order):
        nonlocal comparisons
        comparisons += 1

        if order == Sort.ASC:
            return first_numb > second_numb
        else:
            return second_numb > first_numb

    def merge(input, first_array, second_array):
        first_index = second_index = sorted_index = 0

        while first_index < len(first_array) and second_index < len(second_array):
            if compare(first_array[first_index], second_array[second_index], order):
                input[sorted_index] = second_array[second_index]
                second_index += 1
            else:
                input[sorted_index] = first_array[first_index]
                first_index += 1

            sorted_index += 1

        if first_index == len(first_array):
            for i in range (second_index, len(second_array)):
                input[sorted_index] = second_array[i]
                sorted_index += 1

        else:
            for i in range(first_index, len(first_array)):
                input[sorted_index] = first_array[i]
                sorted_index += 1

    merge(input, left_array, right_array)
    return comparisons
