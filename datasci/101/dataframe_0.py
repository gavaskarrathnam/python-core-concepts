# Import pandas package
import pandas as pd

# Define a dictionary containing employee data
emplst = {
    'FirstName':['johnk', 'neil', 'shown', 'ram', 'randall'],
    'LastName':['Keyes', 'silverman', 'O\' Conner', 'Somesh', 'ralf'],
    'Age':[50,45,30,36,46],
    'Qualification':['Msc', 'MA', 'MCA', 'Phd','Phd']
}

df = pd.DataFrame(emplst)
# Convert the dictionary to DataFrame
# print(df)

# Convert the selected dictionary column to Dataframe
print(df[['LastName','Age']])