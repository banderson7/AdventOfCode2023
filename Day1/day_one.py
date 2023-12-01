from Shared.open_file import open_file


def day_one_part_one():
    data = open_file(1)
    numbers = []
    for line in data:
        numbers_in_row = [int(i) for i in [*line] if i.isdigit()]
        number = int(str(numbers_in_row[0]) + str(numbers_in_row[-1]))
        numbers.append(number)
    print(sum(numbers))
