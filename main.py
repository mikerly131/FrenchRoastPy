# import pandas as pd
# import numpy as np
import csv

# Check the resources folder for csv file to process
# Maybe a function at some point to read a desired csv in the resources folder

with open('csvfile.csv' , 'r') as csvfile:
    # create the object of csv.reader()
    csv_file_reader = csv.reader(csvfile,delimiter=',')
    for row in csv_file_reader:
        print(row)

id_dict = {}
id_dict.update('key')

# Output data needs to be a json array
# Each thing in the array is an object for the customer/customer id
# The customer object  with comma separated json objects within for each customer
# within each customer object, list of objects -> account number, balance

# import json -> json package / standard library for handling json

# Object relations from python to JSON
# python = json
# dict = object
# list, tuple = array
# str = string
# int, float, etc = number
# tru = true
# false = false
# none = null

# json.loads(will put a json entry into a dictionary?)
# will handle/convert the data types properly
# example - if dict has lists and dicts inside, the type conversion for json will be correct
#
# json dumps does reverse?  put a dictionary into json?



