def find_min(piles, hours):
    maximal_value = max(piles)
    low = 1
    high = maximal_value
    required_h = 0

    if len(piles) == hours:
        return maximal_value

    while required_h != hours:
        k = (high + low) // 2

        required_h = 0
        for each_pile in piles:
            required_h += each_pile // k + (0 if each_pile % k == 0 else 1)

        if required_h == hours:
            min_speed = k
        if required_h < hours:
            high = k - 1
        if required_h > hours:
            low = k + 1

    return min_speed


if __name__ == "__main__":
    print(find_min([3, 6, 7, 11], 8))
    print(find_min([30, 11, 23, 4, 20], 5))
    print(find_min([30, 11, 23, 4, 20], 6))