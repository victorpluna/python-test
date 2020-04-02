#!/usr/bin/env python3

import argparse
import json

from controllers.main_controller import MainController


def main():
    parser = argparse.ArgumentParser(description='Generate Joyjet output')
    parser.add_argument(
        '-l', '--level', type=int, choices=[1, 2, 3], required=True,
        help='an integer to inform the output level'
    )
    args = parser.parse_args()

    with open(f'data/level{args.level}.json') as f:
        input_data = json.loads(f.read())

        controller = MainController(input_data=input_data, level=args.level)
        return controller.generate_output()


if __name__ == "__main__":
    output = main()
    print(output)
