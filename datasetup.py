# datasetup.py -- defines the class to hold the literature data and reads it in
# Written with support from ChatGPT, edited by HM

import csv

class Data:
    def __init__(self, name, value, bounds, category, spread):
        self.name = name  
        self.value = value
        self.bounds = bounds  # Error bounds (e.g., tuple containing lower and upper bounds)
        self.category = category  # Category of the data point (e.g., 'U' for unknown or 'K' for known)
        self.spread = spread  # Range of the data point, calculated from the error bounds (e.g., array of evenly-spaced values from the min to the max)

# Read data from handmade .csv
data = [] #array to store objects of type Data, one for each variable
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = str(row['name'])
        value = float(row['value'])
        bounds = (float(row['lower_bound']), float(row['upper_bound']))
        category = str(row['category'])
        spread = [x/100 for x in range(((value + bounds[0])*100), ((value + bounds[1])*100), 1)] # evenly spaced array form min value to max value by applying error bars. The weird integer arithmetic is to avoid floating point errors
        data.append(Data(name, value, bounds, category, spread))

# Print to double check
for var in data:
    print(var.name, var.value, var.bounds, var.category, var.spread)

