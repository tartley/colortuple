import sys

from .options import create_parser


def main():
    # setup.py install/develop creates an executable that calls 'main()'
    options = create_parser().parse_args(sys.argv[1:])

