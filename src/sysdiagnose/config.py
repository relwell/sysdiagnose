import os

"""
This file contains all of the configuration values for the project.
"""


cases_file = "cases.json"
data_folder = "/tmp/sysdiagnose_data/"
parsed_data_folder = "/tmp/sysdiagnose_parsed_data/"
parsers_folder = f"{os.path.dirname(__file__)}/parsers/"
analysers_folder = f"{os.path.dirname(__file__)}/analyzers/"
debug = False
