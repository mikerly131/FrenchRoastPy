"""
Program that processes the set CSV transaction file to create an account log with balances based on the transactions
"""
import utilities
import sys


def main():

    # Get the list of transactions to process
    transaction_list = utilities.get_txns_list()

    # Get the accounts by customer id from dataframe, make it a dict, will be of lists
    cust_accts_list = utilities.get_cust_acct_list()

    # Create a dictionary of customer ids mapped to accounts
    cust_acct_log = utilities.get_account_log(cust_accts_list)

    # Process transactions to update the account log -> aka update balance of each account in log for each transaction
    updated_account_log = utilities.process_transactions(cust_acct_log, transaction_list)


if __name__ == "__main__":
    sys.exit(main())

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