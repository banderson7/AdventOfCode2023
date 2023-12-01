def open_file(day: int):
    opened_file = open(f'./Day{day}/Day{day}_input.txt')
    lines = []
    for line in opened_file:
        lines.append(line.strip())
    return lines
