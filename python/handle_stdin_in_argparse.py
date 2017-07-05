#!/usr/bin/env python3
# for STDIN to work, you just need to read from it.
# the problem is it will hang if it's empty
# it's best to create a mutually exclusive option in argparse
# This allows you to supply the --stdin option and read from there

import argparse
import sys

def main():
    print('starting main')
    parser = argparse.ArgumentParser(
        description='PROGRAM DESCRIPTION HERE',
        #formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="THIS APPEARS AT THE END OF THE HELP MSG Example: \n\t %s EXAMPLE_HERE"%sys.argv[0])
    
    either_or = parser.add_mutually_exclusive_group(required=True)
    
    either_or.add_argument(
    	'-a','--argument',
    	#metavar='NAME_OF_VAR_IN_HELP_MESSAGES', #not used because of action='store_true'
    	dest='argument_name_in_parsed_args',
    	action='store_true', #https://docs.python.org/3/library/argparse.html#action-classes
    	help='ARGUMENT DESCRIPTION HERE',
    	)
    either_or.add_argument(
        '--stdin',
        dest='stdin',
        action='store_true',
        help='Supply input via STDIN',
        )

    args = parser.parse_args()
    print(args)
    # Handle STDIN
    # If some other var doesnt exist or whatever, then just read from sys.stdin    
    if args.stdin:
        ##do something with stdin
        stdin_data = sys.stdin.readlines()
        for line in stdin_data:
            print(line.strip())


if __name__ == '__main__':
    sys.exit(main())