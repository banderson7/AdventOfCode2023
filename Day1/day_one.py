from Shared.open_file import open_file

number_words = {
    "one": 1,
    "1": 1,
    "two": 2,
    "2": 2,
    "three": 3,
    "3": 3,
    "four": 4,
    "4": 4,
    "five": 5,
    "5": 5,
    "six": 6,
    "6": 6,
    "seven": 7,
    "7": 7,
    "eight": 8,
    "8": 8,
    "nine": 9,
    "9": 9
}


def find_substrings(string, substring):
    substrings = []
    i = 0
    while i < len(string):
        j = string.find(substring, i)
        if j == -1:
            return substrings
        substrings.append(j)
        i = j + len(substring)
    return substrings


def day_one_part_one():
    data = open_file(1)
    numbers = []
    for line in data:
        numbers_in_row = [int(i) for i in [*line] if i.isdigit()]
        number = int(str(numbers_in_row[0]) + str(numbers_in_row[-1]))
        numbers.append(number)
    print(f'Day One Part 1 result: {sum(numbers)}')


def day_one_part_two():
    data = open_file(1)
    numbers = []
    for line in data:
        numbers_in_row = []
        for value in number_words.keys():
            indices = find_substrings(line, value)
            if len(indices) > 0:
                for index in indices:
                    numbers_in_row.append([index, number_words[value]])
        numbers_in_row.sort(key=lambda x: x[0])
        number = int(str(numbers_in_row[0][1]) + str(numbers_in_row[-1][1]))
        numbers.append(number)
    print(f'Day One Part 2 result: {sum(numbers)}')
