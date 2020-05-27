import json

''' how to know the target '''
my_list = [1,2,3,4,5]
my_target = 7
'''
for i in my_list:
    #target = my_list.index(i) + my_list.index(i)+1
    print (my_list[i-1] )
    #if target == my_target:
    #    print(target)
'''

'''
Function
--------
def <function_name>:
    logic
    
function call:
assignment_variable = function_name()


# function should have to return something
It can be
> print
> return

'''
def add(a, b):
    return (a + b)

#add_var = add(10,20)
#print (add_var)

'''
Anonomymous function aka lanbda function

syntex:
function_name = lambda variable:opertions
'''
#lambda_add = lambda a,b:a+b
#print(lambda_add(10, 50))


'''

'''
def getevennumberlist(no_range):
    even_no_list = []
    for idx in range(no_range):
        if (idx % 2 == 0):
            even_no_list.append(idx)
    return even_no_list

#print(getevennumberlist(10))

'''
def lambda_even_no(num_range):
    num_list = []
    for idx in range(num_range):
        num_list.append(idx)

    return list(filter(lambda number: (number % 2 == 0), num_list))

print(lambda_even_no(20))
'''

'''
PEP rule
'''
'''
def getval(*args):
    print(args)

print(getval(1,2,3))
'''
'''
function overloading
'''

'''
Python dir() function returns the list of names in the current local scope. If the object on which method is called has a method named __dir__(),
this method will be called and must return the list of attributes. It takes a single object type argument.

'''

#import os
#print(dir())
'''
a = [1,2,3]
b = ["A", "B", "C"]
c = {}
for i in range(len(a)):
    c[a[i]] = b[i]
print(c)
'''
'''
a = [1,2,3,4,5]
b = [1,3,1,2,5]
c = []

for i in a:
    if i in b:
        c.append(i)

print(c)
'''

'''
find the largest no.
'''
'''
a = [10, 20, 30, 50, 40]
f = a[0]
for i in a:
    if i > f:
        f = i
print(f)

# way 2
a1 = [10, 20, 30, 50, 40]
largestno = 0
for i in a1:
    if (i > largestno):
        largestno = i

print(largestno)
'''


'''
find no. of occurence
'''
'''
a = [1,2,3,4,5,5]
b = {}
temp = []
occur = 0
for i in a:
    if i in temp:
        occur = occur + 1
    else:
        occur = 1
        temp.append(i)

    b[i] = occur

print(b)
'''




'''
How to access the json
'''
json = {
  "cart": [
    {
      "itemname": [
        "A",
        "B"
      ]
    },
    {
      "itemvalue": [
        "100",
        "200"
      ]
    }
  ]
}

process_json = {}
process_json.update(json)
# print(process_json) #{'cart': [{'itemname': ['A', 'B']}, {'itemvalue': ['100', '200']}]}
'''
for key, value in process_json.items():
    for i in value:
        for key, value in i.items():
            print(key + " " + value[-1])
'''
#print(process_json['cart'][0]['itemname'][-1])
#print(process_json['cart'][1]['itemvalue'][-1])


'''
create json
'''
#data = {'cart': [{'itemname': ['A', 'B']}, {'itemvalue': ['100', '200']}]}
#final_json = {}
#final_json = json.dumps(data)
#print(final_json)



#[{'itemname': ['A', 'B']}, {'itemvalue': ['100', '200']}]

firstdict = {}
list1 = ['A', 'B']
firstdict['itemname'] = list1

mydict = {}
mydict["cart"] = []
mydict["cart"].append(firstdict)

print(mydict)



a = "someithing"
b = [data for data in a]
print (b)

c = [data for data in a if data == "i"]
print(len(c))

'''

'''
mydict = {}


mydict[2] = [i for i in range(50) if i%2==0]
print(mydict)






