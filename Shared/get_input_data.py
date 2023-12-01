import csv
import requests
import os.path


def get_input_data(day: int):
    if os.path.exists(f'./Day{day}/Day{day}_input.txt'):
        return
    session_id = open('./config').read()
    r = requests.get(f'https://adventofcode.com/2023/day/{day}/input', cookies={
        'session': session_id
    })
    with open(f'./Day{day}/Day{day}_input.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        for line in r.text.split('\n'):
            writer.writerow([
                line
            ])
