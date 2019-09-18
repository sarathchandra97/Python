# myls.py
# Import the argparse library
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(prog="myls",description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))

# before
# 186590d11d1d:argparse syakka$ python after_argparse.py -h
# usage: after_argparse.py [-h] path

## After
# 186590d11d1d:argparse syakka$ python setting_up_program_name.py
# usage: myls [-h] path
# myls: error: too few arguments


