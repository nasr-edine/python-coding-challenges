def migratoryBirds(arr):
    frequency = {}

    for n in arr:
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1

    min_key = 6
    max_freq = max(frequency.values())

    for n in frequency.items():
        if n[1] == max_freq:
            if n[0] < min_key:
                min_key = n[0]

    return min_key


if __name__ == "__main__":
    test = [1, 4, 4, 4, 5, 3]
    print(migratoryBirds(test))