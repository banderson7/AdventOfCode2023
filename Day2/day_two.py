from Shared.open_file import open_file

contents = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def day_two_part_one():
    data = open_file(2)
    valid_games = []
    for line in data:
        game = line.strip("\"")
        game_count, cubes = game.split(':')
        game_number = int(game_count.split(' ')[1])
        cube_sets = cubes.split(";")
        valid_game = True
        for cube_set in cube_sets:
            pull = cube_set.split(',')
            for color_group in pull:
                count, color = color_group.strip().split(" ")
                if int(count) > contents[color]:
                    valid_game = False
                    continue
        if valid_game:
            valid_games.append(game_number)
    print(f'Day Two Part 1 result: {sum(valid_games)}')
