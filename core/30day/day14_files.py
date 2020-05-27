
# below syntex called "Context Manager"
with open("iris.csv", "r") as iris_file:
	iris_data = iris_file.readlines()

headers = iris_data[0].strip().split(",")
print("Header :", headers)
irises = []

for row in iris_data[1:]:
	iris = row.strip().split(",")
	iris_dict = dict(zip(headers, iris)) # dict build-in create dictionary object

	irises.append(iris_dict)

print(" ")
print(irises)

print(" ")

print(" ----- Exercise #1 ----- ")

with open("hello_world.txt", "a") as f:
	f.write("Hello, World! ")
	f.write("\n How are you? ")


with open("hello_world.txt", "r") as file:
	print("Content from Hello world: ", file.readlines())

with open("iris_new.json", "a") as csv:
	csv.write(str(irises))

''' 
3) Take the list of dictionaries we created from the Iris flower data set and write it to a new file in CSV format.
'''
irises = [
	{'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.9', 'sepal_width': '3',   'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.6', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '5',   'sepal_width': '3.6', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '7',   'sepal_width': '3.2', 'petal_length': '4.7', 'petal_width': '1.4', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '4.9', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '5.5', 'sepal_width': '2.3', 'petal_length': '4',   'petal_width': '1.3', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.5', 'sepal_width': '2.8', 'petal_length': '4.6', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6',   'petal_width': '2.5', 'species': 'Iris-virginica'},
	{'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9', 'species': 'Iris-virginica'},
	{'sepal_length': '7.1', 'sepal_width': '3',   'petal_length': '5.9', 'petal_width': '2.1', 'species': 'Iris-virginica'},
	{'sepal_length': '6.3', 'sepal_width': '2.9', 'petal_length': '5.6', 'petal_width': '1.8', 'species': 'Iris-virginica'},
	{'sepal_length': '6.5', 'sepal_width': '3',   'petal_length': '5.8', 'petal_width': '2.2', 'species': 'Iris-virginica'}
]

def write_file(filename):
	with open(filename, "a") as f:
		for iris in irises:
			f.write(f"{iris['sepal_length'].strip()}, {iris['sepal_width'].strip()}, {iris['petal_length'].strip()}, {iris['petal_width'].strip()}, {iris['species'].strip()} \n")
			
write_file("iris_new_2.csv")




