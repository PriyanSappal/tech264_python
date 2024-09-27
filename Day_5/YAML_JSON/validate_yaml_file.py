import os
import sys
import yaml

if len(sys.argv) > 1:
# check file exists; the arguments above needs to be more than one because the first file
# will be the file

    if os.path.exists(sys.argv[1]):
# the index of one here will be the JSON file
# open file for reading
        file = open(sys.argv[1], "r")
# parse the YAML file - if it loads then the file contains valid JSON
        yaml.safe_load(file)
        file.close()
        print("YAML file is valid!")
    else:
# alert user that file specified does not exist
        print("ERROR: File '" + sys.argv[1] + "' not found")
else:
    print("ERROR: No YAML file was specified to check")
    print(f"Usage: {sys.argv[0]} <YAML filename>")