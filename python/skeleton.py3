#!/usr/bin/env python3
""" Skeleton file for python3 command line scripts"""

import argparse
import sys
import logging

try:
    import os
except ImportError as e:
    print(e)
    quit(1)


def main():
    """Main Execution"""
    # Setup help output
    parser = argparse.ArgumentParser(
        description='PROGRAM DESCRIPTION HERE',
        #formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="THIS APPEARS AT THE END OF THE HELP MSG Example: \n\t %s EXAMPLE_HERE"%sys.argv[0])
    
    # add an argument referred as 
    #https://docs.python.org/3/library/argparse.html#the-add-argument-method
    parser.add_argument(
        '-a','--argument',
        #metavar='NAME_OF_VAR_IN_HELP_MESSAGES', #not used because of action='store_true'
        dest='argument_name_in_parsed_args',
        action='store_true', #https://docs.python.org/3/library/argparse.html#action-classes
        help='ARGUMENT DESCRIPTION HERE',
        )

    parser.add_argument(
        '-b','--bargument ASDF',
        metavar='VAR_NAME_IN_HELP',
        dest='VAR_NAME_IN_ARGS',
        help='ARGUMENT DESCRIPTION HERE',
        )
    
    parser.add_argument(
        '-d', '--debug',
        help="Include debugging output",
        action="store_const", 
        dest="loglevel", 
        const=logging.DEBUG,
        default=logging.WARNING,
        )

    parser.add_argument(
        '-v', '--verbose',
        help="Verbose output",
        action="store_const", 
        dest="loglevel", 
        const=logging.INFO,
        )

    args = parser.parse_args() #reference args with args.argument_name

   
    #setup logging functions. Default is WARNING, but can set for INFO (--verbose) and DEBUG (--debug)
    logging.basicConfig(level=args.loglevel)

    print(args)

    if args.argument:
        # do something with argument value
        print("Your supplied argument for -a is: " + args.argument)
        
if __name__ == '__main__':
    sys.exit(main())