#! /usr/bin/env python3

# For Python3
# DEMO - Skeleton
# Author: david@autopsit.org

import logging
import os
import sys
import json
from datetime import datetime
from optparse import OptionParser

logger = logging.getLogger()
version_string = "sysdiagnose-demo-analyser.py v2023-04-28 Version 0.1"

# ----- definition for analyse.py script -----#
# -----         DO NOT DELETE             ----#

analyser_description = "Do something useful (DEMO)"
analyser_call = "generate_something"
analyser_format = "json"


def generate_something(jsondir, filename):
    """
    Generate the timeline and save it to filename
    """
    logger.info("DO SOMETHING HERE")
    return


# --------------------------------------------------------------------------- #
"""
    Main function
"""
def main():

    if sys.version_info[0] < 3:
        logger.info("Must be using Python 3! Exiting ...")
        exit(-1)

    logger.info(f"Running {version_string}\n")

    usage = "\n%prog -d JSON directory\n"

    parser = OptionParser(usage=usage)
    parser.add_option("-d", dest="inputdir",
                      action="store", type="string",
                      help="Directory containing JSON from parsers")
    parser.add_option("-o", dest="outputfile",
                      action="store", type="string",
                      help="JSON file to save output")
    (options, args) = parser.parse_args()

    # no arguments given by user, print help and exit
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(-1)

    if options.inputdir:
        # do something
        if options.outputfile:
            logger.info("Hello World")
        else:
            logger.info("Something else")
    else:
        logger.info("WARNING -i option is mandatory!")


# --------------------------------------------------------------------------- #

"""
   Call main function
"""
if __name__ == "__main__":

    # Create an instance of the Analysis class (called "base") and run main
    main()

# That's all folks ;)
