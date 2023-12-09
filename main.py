# import pandas as pd
import pandas as pd
import numpy as np
import collections as cts

# Get the CSV file as dataframe
csv_main = pd.read_csv('./resources/transactions.csv', low_memory=False)

# Get the accounts by customer id from dataframe, make it a dict, will be of lists
csv_mod1 = pd.read_csv('./resources/transactions.csv', low_memory=False, header=0, usecols=['customerId', 'accountId'], index_col=None)
csv_mod1_dict = csv_mod1.to_dict(orient='split')
cust_acct_mod = csv_mod1_dict['data']

# Create a dictionary of customer ids mapped to accounts
id_dict = {}
for item in cust_acct_mod:
    key, value_to_add = item
    if key in id_dict and value_to_add not in id_dict[key]:
        id_dict[key].append(value_to_add)

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



