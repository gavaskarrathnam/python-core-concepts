import json

'''
jsonfile = 'profileScrap.json'
with open(jsonfile) as f:
    data = json.load(f)
    for item in data:
        print(" fullName : " + item.get("general").get("fullName"))
        print(" Company : " + item.get("general").get("company"))
        print(" Skills : ")
        for skl in item['skills']:
            print("   " + skl['name'] + " ( " + skl['endorsements'] + " )")
        print('---------------------------------------------------------------')
'''

j = json.loads('{"password": "123456", "id": 1, "name": "ashley"}')
print(type(j))


d = {
    'first_name': 'gavas',
    'last_name': 'rathnam',
    'titles': ['Java', 'Developer'],
}

json = json.dumps(d)
print(json)



