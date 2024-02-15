if __name__ == '__main__':
    records = {}
    smallest, second_smallest = float('inf'), float('inf')
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
    records = dict(sorted(records.items(), key=lambda x: x[0]))
    for num in records.values():
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and smallest != num:
            second_smallest = num
    for key, val in records.items():
        if val == second_smallest:
            print(key)
