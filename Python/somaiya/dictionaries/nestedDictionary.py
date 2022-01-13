
sampleDict = {
    "classes":{
        "student":{
            "name": "Mike", 
            "marks": {
                "physics": 70,
                "history": 90,
            }
        }
    }
}
print(sampleDict["classes"]["student"]["marks"]["history"])

sampleDict = {
    "name": "kelly", 
    "salary": 23300, 
    "age": 23, 
    "city": "New York"
}

print(sampleDict["name"], sampleDict["salary"])

for x, y in sampleDict.items():
    if x == "name" or x == "salary":
        print(x, ": ", y)
    
# Work around 
keys = ['name', 'salary']
res = dict()
for k in keys: 
    res.update({k:sampleDict[k]});
print(res)
