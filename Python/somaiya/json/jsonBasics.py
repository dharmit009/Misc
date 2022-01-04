import json

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type":"intl", 
        "number":"+91 1234567890"
    }, 
    "email":{
        "hide":"yes"
    }

}
'''

print("Data: \n", data);
print(type(data));

info = json.loads(data)

print("Info: \n", info);
print(type(info));

print("Accessing Data ...")
print("Name: ", info["name"])
print("Phone No: ", info["phone"]["number"])
print("Hide: ", info["email"]["hide"])
