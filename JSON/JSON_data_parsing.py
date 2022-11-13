import json


with open('JSON/json_sample.json', 'r') as data:
   Json_file = data.read()
   
json_python = json.loads(Json_file)

#Getting values from the keys
Interface = json_python["interface"]["Param"]
IPAddress = json_python["interface"]["ConfigIf-Configuration"]["ip"]['address']["IPAddress"]
print(IPAddress)

