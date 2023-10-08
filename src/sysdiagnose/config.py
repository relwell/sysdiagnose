import os

"""
This file contains all of the configuration values for the project.
"""


cases_file = "cases.json"
data_folder = "/tmp/sysdiagnose_data/"
parsed_data_folder = "/tmp/sysdiagnose_parsed_data/"
parsers_folder = os.path.abspath("./parsers/")
analysers_folder = os.path.abspath("./analyzers")
debug = False
