def monkey_count(n):
    monkeys = n * [0]

    for i in range(n):
        monkeys[i] = i + 1

    return monkeys


if __name__ == "__main__":
    print(monkey_count(10))