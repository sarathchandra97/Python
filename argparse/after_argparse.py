# myls.py
# Import the argparse library
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

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


# 186590d11d1d:argparse syakka$ python after_argparse.py
# usage: after_argparse.py [-h] path
# after_argparse.py: error: too few arguments
# 186590d11d1d:argparse syakka$ python after_argparse.py -h
# usage: after_argparse.py [-h] path
#
# List the content of a folder
#
# positional arguments:
#   path        the path to list
#
# optional arguments:
#   -h, --help  show this help message and exit
# 186590d11d1d:argparse syakka$ python after_argparse.py ~
# .pgAdmin4.15182351514808255573.log
# .config
# Music
# .pgAdmin4.17635054442383556018.addr
# .docker
# .anyconnect
# .DS_Store
# .CFUserTextEncoding
# .zcompdump-186590d11d1d-5.3
# .zshrc
# .sqlworkbench
#
# 186590d11d1d:argparse syakka$ python after_argparse.py sdj/
# The path specified does not exist
# 186590d11d1d:argparse syakka$ python after_argparse.py ld dd
# usage: after_argparse.py [-h] path
# after_argparse.py: error: unrecognized arguments: dd


