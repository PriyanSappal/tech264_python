import json

# create the dictionary
servers_dict = {
    "server1": {
        "hostname": "web-server-1",
        "ip_address": "192.168.1.1",
        "role": "web",
        "status": "active"
    },
    "server2": {
        "hostname": "db-server-1",
        "ip_address": "192.168.1.2",
        "role": "database",
        "status": "maintenance"
    }
}

# Convert the dictionary to a JSON-formatted string
json_string = json.dumps(servers_dict, indent=4)  # 'indent=4' is used for pretty-printing
print(json_string)

# Convert the dictionary to a JSON file
with open("output.json", 'w') as json_file:
    json.dump(servers_dict, json_file, indent=4)  # Write dictionary to file in JSON format
