import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument('-p', type=int, default='8000', metavar='<Port Number>', 
        required=True,
        help="Provide a port the server will listen on")

args = parser.parse_args()
port = sys.argv[2]

print('Your port is ' + port)
