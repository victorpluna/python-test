#!/usr/bin/env python3

import argparse, sys, json
import os.path


def main():
    parser = argparse.ArgumentParser(description='Generate Joyjet output')
    parser.add_argument(
        'level', metavar='level<number>', type=str,
        choices=['level1', 'level2', 'level3'],
        help='an label to inform the output level'
    )
    args = parser.parse_args()
    
    with open(f'data/{args.level}.json') as f:
        content = json.loads(f.read())
        print(content)


if __name__ == "__main__":
    main()