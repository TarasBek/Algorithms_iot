d = 256  # кількість цифр в алфавіті


def rabin_carp(pattern, input_text, prime_num):
    len_pattern = len(pattern)
    len_input = len(input_text)
    i = 0
    j = 0
    hash_pattern = 0
    hash_input = 0
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(len_pattern - 1):
        h = (h * d) % prime_num

    # вираховуємо хеш номер першого елемента в патерні та в шуканій стрічці
    for i in range(len_pattern):
        hash_pattern = (d * hash_pattern + ord(pattern[i])) % prime_num
        hash_input = (d * hash_input + ord(input_text[i])) % prime_num

    # переміуємо патерн на один символ в бік
    for i in range(len_input - len_pattern + 1):
        # перевіряємо чи хеш  співпадається
        if hash_pattern == hash_input:
            # перевіряємо кожну букву чи вона співпадає
            for j in range(len_pattern):
                if input_text[i + j] != pattern[j]:
                    break
                else:
                    j += 1

            if j == len_pattern:
                print(str(i))

            # рахуємо значення для наступної частини патрену
        if i < len_input - len_pattern:
            hash_input = (d * (hash_input - ord(input_text[i]) * h) + ord(input_text[i + len_pattern])) % prime_num

            # конверуємо негативні значення
            if hash_input < 0:
                hash_input = hash_input + prime_num
