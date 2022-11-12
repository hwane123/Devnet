import xmltodict

with open("interface_G1.xml") as data:
    interface = data.read()
    
xml_to_python = xmltodict.parse(interface)

with open("xmlsample.xml", "w") as data:
    data.write(xmltodict.unparse(xml_to_python, pretty=True))
    

