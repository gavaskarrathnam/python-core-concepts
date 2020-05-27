# employee = {
#     "name" : ["gavaskar rathnam", "Taanve", "Krishna", "Ramya"],
#     "possition": "SVP"
# }
#
# for key, value in employee.items():
#     print(key, " --- ", value)
#
#
# for key in employee:
#     print(employee[key])
#
# for key in employee.keys():
#     print(key)
#
# for value in employee.values():
#     print(value)


# exercises
pink_band = (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
        "Speak to Me",
        "Breathe",
        "On the Run",
        "Time",
        "The Great Gig in the Sky",
        "Money",
        "Us and Them",
        "Any Colour You Like",
        "Brain Damage",
        "Eclipse"
    )
)

music_bands = {}
music_bands['album'] = pink_band[0]
music_bands['artist'] = pink_band[1]
music_bands['year'] = pink_band[2]
music_bands['tracks'] = pink_band[3]

print("----- Initial Music bands -----")
for key, value in music_bands.items():
    print(f"{key}: {value}")

# backsteet_band = {
#     'album': "The Rock",
#     'artist': "Backstreet Boys",
#     'year': "1995",
#     'tracks': ['you are my girl', 'who are you']
# }
#
# music_bands.update(backsteet_band)
#
# print("----- Music bands -----")
# for key, value in music_bands.items():
#     print(f"{key}: {value}")

'''
Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. 
Once you've tried this, repeat the step using the get method to prevent the exception being raised.
'''

del music_bands['year']
#print(music_bands['year']) # will get KeyError

music_bands['country'] = 'US'

print(music_bands.get('year', "Unknown Key"))

print(music_bands.get('country', "Unknown Key"))




# Create your dictionary class
class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

    # Function to add key:value
    def add(self, key, value):
        self[key] = value

# Main Function
dict_obj = my_dictionary()

for i in range(10):
    dict_obj.add(i, "data "+ str(i))

print(" --- DICTIONARY --- ")
for key, value in dict_obj.items():
    print("KEY {} : VALUE {} ".format(key, value))



