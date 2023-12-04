from Day1.day_one import day_one_part_one, day_one_part_two
from Day2.day_two import day_two_part_one, day_two_part_two
from Day3.day_three import day_three_part_one
from Shared.get_input_data import get_input_data


def main():
    get_input_data(1)
    day_one_part_one()
    day_one_part_two()
    get_input_data(2)
    day_two_part_one()
    day_two_part_two()
    get_input_data(3)
    day_three_part_one()


if __name__ == '__main__':
    main()
