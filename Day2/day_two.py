from dataclasses import dataclass

from Shared.open_file import open_file

contents = {
    "red": 12,
    "green": 13,
    "blue": 14
}


@dataclass
class CubeSet:
    color: str
    count: int


@dataclass
class Handful:
    cube_sets: [CubeSet]


@dataclass
class Game:
    count: int
    handfuls: [Handful]

    def __init__(self, input_data: str):
        self.handfuls = []
        game = input_data.strip("\"")
        game_count, cubes = game.split(':')
        self.count = int(game_count.split(' ')[1])
        handfuls = cubes.split(";")
        for handful in handfuls:
            cube_sets_data = handful.split(',')
            cube_sets = []
            for cube_set in cube_sets_data:
                count, color = cube_set.strip().split(" ")
                cube_sets.append(CubeSet(color, int(count)))
            self.handfuls.append(Handful(cube_sets))


def day_two_part_one():
    data = open_file(2)
    valid_games = []
    for line in data:
        game = Game(line)
        valid_game = True
        for handful in game.handfuls:
            for cube_set in handful.cube_sets:
                if cube_set.count > contents[cube_set.color]:
                    valid_game = False
                    continue
        if valid_game:
            valid_games.append(game.count)
    print(f'Day Two Part 1 result: {sum(valid_games)}')


def day_two_part_two():
    data = open_file(2)
    powers = []
    for line in data:
        game = Game(line)
        minimum_cubes = {
            "red": 0,
            "blue": 0,
            "green": 0,
        }
        for handful in game.handfuls:
            for cube_set in handful.cube_sets:
                if cube_set.count > minimum_cubes[cube_set.color]:
                    minimum_cubes[cube_set.color] = cube_set.count
        power = 1
        for minimum in minimum_cubes.values():
            power *= minimum
        powers.append(power)
    print(f'Day Two Part 2 result: {sum(powers)}')
