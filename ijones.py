def find_ways_count(matrix, width, height):
    flow_arr = [[1 for _ in range(width)] for _ in range(height)]

    counter_for_letter = dict()
    letter_in_column = dict()

    #вибераємо рядок
    for i in range(width):
        #вибераємо елемент
        for j in range(height):
            #присвоюємо letter значення елемента в матриці
            letter = matrix[j][i]
            # робимо 2 перевірки
            # перша чи наша ширина в матриці мешша від зазначеної ширини
            # друга чи
            if i+1 < width:
                if matrix[j][i] == matrix[j][i+1]:
                    flow_arr[j][i+1] -= 1


            if letter in counter_for_letter:
                flow_arr[j][i] += counter_for_letter[letter]

            if letter in letter_in_column:
                letter_in_column[letter] += flow_arr[j][i]
            else:
                letter_in_column[letter] = flow_arr[j][i]

        for (letter, count) in letter_in_column.items():
            if letter in counter_for_letter:
                counter_for_letter[letter] += letter_in_column[letter]
            else:
                counter_for_letter[letter] = letter_in_column[letter]
        letter_in_column = dict()

    return flow_arr


