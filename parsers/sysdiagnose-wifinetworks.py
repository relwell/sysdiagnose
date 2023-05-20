#! /usr/bin/env python3

# For Python3
# Script to parse the swcutil_show.txt file
# Author: Emilien Le Jamtel

"""sysdiagnose intialize.

Usage:
  sysdiagnose-wifinetwork.py -i <logfolder>
  sysdiagnose-wifinetwork.py (-h | --help)
  sysdiagnose-wifinetwork.py --version

Options:
  -h --help     Show this screen.
  -v --version     Show version.
"""

import sys
from optparse import OptionParser
import plistlib
import json
from docopt import docopt
import glob
import re
import datetime
import binascii

# ----- definition for parsing.py script -----#

parser_description = "Parsing com.apple.wifi plist files"
parser_input = "wifi_data"  # list of log files - only get the .txt files from the list
parser_call = "parsewifinetwork"

# --------------------------------------------------------------------------- #

def parsewifinetwork(wifi_data):
    output = {}
    for data in wifi_data:
        if data.endswith('com.apple.wifi.recent-networks.json'):
            print('parsing: ' + data)
            with open(data, 'r') as f:
                output['recent_networks'] = json.load(f)            
        elif data.endswith('com.apple.wifi.plist'):
            with open(data, 'rb') as f:
                print('parsing: ' + data)
                # loading the plist file
                plist = plistlib.load(f)
                # resolving datetime objects
                plist = find_datetime(plist)
                # cleaning bytes objects
                plist = find_bytes(plist)
                output['com.apple.wifi.plist'] = plist
    return output

def find_datetime(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print('dict : ' + str(v))
            find_datetime(v)
        elif isinstance(v, list):
            for item in v:
                find_datetime(item)
        elif isinstance(v, datetime.datetime):
            d[k]=v.isoformat()
    return d

def find_bytes(d):
    for k, v in d.items():
        if isinstance(v, dict):
            find_bytes(v)
        elif isinstance(v, list):
            for item in v:
                find_bytes(item)
        elif isinstance(v, bytes):
            d[k]=binascii.hexlify(v).decode('utf-8')
    return d

# --------------------------------------------------------------------------- #

def main():
    """
        Main function, to be called when used as CLI tool
    """

    arguments = docopt(__doc__, version='parser for com.apple.wifi plist files v0.2')

    if arguments['-i']:
        # list plist files in folder and build a list
        plist_files = glob.glob(arguments['<logfolder>'] + '/com.apple.wifi*.plist')
        plist_files.append(arguments['<logfolder>'] + '/com.apple.wifi.recent-networks.json')
        output = parsewifinetwork(plist_files)
        print(json.dumps(output, indent=4))

# --------------------------------------------------------------------------- #


"""
   Call main function
"""
if __name__ == "__main__":

    # Create an instance of the Analysis class (called "base") and run main
    main()

# That's all folk ;)