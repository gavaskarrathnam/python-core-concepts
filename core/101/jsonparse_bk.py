import json

def locateByName(e,name):
    for child in e.get(name,[]):
        result = locateByName(child,name)
        if result is not None:
            return result

    return None

file = 'profileScrap.json'
node = locateByName(file, 'general')
print (node['fullName'], node['connections'])