#taken from https://stackoverflow.com/questions/14097061/easier-way-to-enable-verbose-logging
import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument(
    '-d', '--debug',
    help="Debug level output",
    action="store_const", 
    dest="loglevel", 
    const=logging.DEBUG,
    default=logging.WARNING,
)
parser.add_argument(
    '-v', '--verbose',
    help="verbose logging",
    action="store_const", 
    dest="loglevel", 
    const=logging.INFO,
)
args = parser.parse_args()    
logging.basicConfig(level=args.loglevel)