from dataclasses import dataclass

from Shared.open_file import open_file


@dataclass
class PartNumber:

    surrounding_indices = []


@dataclass
class Schematic:
    rows: [] = None

    def add_row(self, row):
        if self.rows is None:
            self.rows = []
        self.rows.append(row)


def day_three_part_one():
    data = open_file(3)
    schematic = Schematic()
    for line in data:
        schematic.add_row([*line])
    for x, row in enumerate(schematic.rows):
        for y, column in enumerate(row):
            print(schematic.rows[x][y])
            pass

    pass
