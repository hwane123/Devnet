import yaml

with open("YAML/yaml_sample.yaml") as data:
    yaml_read = data.read()

# Now we will load the variable called read
yaml_python = yaml.load(yaml_read, Loader=yaml.FullLoader)

# Now we will print and see that the YAML file has now been converted to a dict
# print(yaml_python)

description = yaml_python["interface"]["ConfigIf-Configuration"]['description']["UpTo200CharactersInterface"] = "Successfully Changed by python_admin"
with open("yaml_sample1.yaml", "w") as data:
    data.write(yaml.dump(yaml_python, default_flow_style=False))
    
