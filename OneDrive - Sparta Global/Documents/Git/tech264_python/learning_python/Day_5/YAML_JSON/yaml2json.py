import json
import os
import sys
import yaml

# Checking there is a file name passed
if len(sys.argv) > 1:
    # Opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    # Failing if the file isn't found
    else:
        print("ERROR: " + sys.argv[1] + " not found")
        exit(1)
# No source file specified
else:
    print("ERROR: No JSON file was specified")
    print("Usage: yaml2json.py <source_file.yaml> <target_file.json>")
    exit(1)
# 1. Convert the JSON to YAML - use yaml library
# WRITE YOUR CODE HERE
convert_json = json.dumps(source_content, indent=4)
# 2. Save the YAML into a new file with the name for it received as a argument
# 2.1 Check the target file name was specified as an argument, if not, output the YAML to the screen instead
# WRITE YOUR CODE HERE

if len(sys.argv) > 2:
    target_file_name = sys.argv[2]
# 2.2 Check the target file doesn't already exist
# WRITE YOUR CODE HERE
    if os.path.exists(target_file_name):
        print(f"ERROR: {target_file_name} already exists")
        exit(1)

# 2.3 If the previous conditions are not met, save the YAML file
    with open(target_file_name, "w") as yaml_file:
        yaml_file.write(convert_json)
    print(f"JSON content successfully saved to {target_file_name}")
else:
# 2.3 If previous conditions not met, then save YAML file
# WRITE YOUR CODE HERE
    print("No target file specified. Outputting YAML content to screen:")
    print(convert_json)