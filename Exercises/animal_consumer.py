import json

def getdata(): 
    with open("data_file.json", 'r') as json_file:
        userdata = json.load(json_file)
        
    return userdata

test = getdata()
print(type(test))
#print(test)
output = [x for x in test if x['head'] == 'snake']
output1 = [x for x in test if x['legs'] == 12]
print(output)
print(output1)