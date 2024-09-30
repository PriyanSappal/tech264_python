import yaml  # Import the json module to work with YAML files

# Step 1: Open the converted.yaml file and load its content into a Python dictionary
with open('converted.yaml', 'r') as yaml_file:
	details = yaml.safe_load(yaml_file)  # Parse the YAML file into a Python dictionary

print(type(details))
print(details)
print(details['address'])
print(details['age'])

