
import json  # Import the json module to work with JSON files

# Step 1: Open the servers.json file and load its content into a Python dictionary
with open('servers.json', 'r') as json_file:
	servers = json.load(json_file)  # Parse the JSON file into a Python dictionary

# Step 2: Print the type of the "servers" variable to confirm it's a dictionary
print(f"The type of 'servers' is: {type(servers)}")

# Step 3: Print the record with the key "server1"
print(f"Record with key 'server1': {servers['server1']}")

# Step 4: Print the record with the key "server2"
print(f"Record with key 'server2': {servers['server2']}")

# Step 5: Loop through the dictionary and print all keys and values
for server_key, server_info in servers.items():
	print(f"Key and value: '{server_key}' = '{server_info}'")

	# Step 6: Loop through each sub-key in the server info (hostname, ip_address, etc.)
	for info_key, info_value in server_info.items():
		print(f"Record key and sub value: '{info_key}' = '{info_value}'")
