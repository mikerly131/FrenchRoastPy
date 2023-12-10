"""
Module to provide methods (functions) for main program.
They are utilities to create an account log from a csv file of transactions and determine the balance for accounts.
"""
import pandas as pd


# Function to get a list of transactions from a csv file
def get_txns_list(file_name) -> list:

    csv_txn_df = pd.read_csv(f'./resources/{file_name}.csv', low_memory=False, header=0,
                         usecols=['customerId', 'accountId', 'transactionType', 'amount'], index_col=None)
    csv_txn_dict = csv_txn_df.to_dict(orient='split')
    txn_list = csv_txn_dict['data']
    return txn_list


# Function to convert the txn amouns in a txn list to ints
def convert_txn_amounts(txns: list):

    for txn in txns:
        val = int(txn[3] * 100)
        d_val = round(float(val) / 100, 2)
        txn[3] = round(d_val, 2)

    return txns


# Function to get a list of customers and accounts from given CSV
def get_cust_acct_list(file_name) -> list:
    csv_df = pd.read_csv(f'./resources/{file_name}.csv', low_memory=False, header=0,
                           usecols=['customerId', 'accountId'], index_col=None)
    csv_dict = csv_df.to_dict(orient='split')
    cust_acct_list = csv_dict['data']
    return cust_acct_list


# Function to get account log (list of dictionaries, each dictionary has 2 kvps, cust id and account,
# Accounts is a list of dictionaries, each dictionary has 2 kvps account number and balance
def get_account_log(cust_acct_list: list) -> list:

    cust_acct_dict = make_cust_acct_dict(cust_acct_list)
    cust_acct_log = list(cust_acct_dict.values())

    # Loop through the dictionaries in the cust acct list, update the lists in them
    for ca_dict in cust_acct_log:

        # Get the list of accounts for dict, lcs to change each account to dict with account number and balance
        accts = ca_dict['accounts']
        updated_accts_list = [{'accountNumber': account, 'balance': 0} for account in accts]
        ca_dict['accounts'] = updated_accts_list

    return cust_acct_log


# Helper function to create a dictionary where each cust id is the key to a dictionary of cust id and accounts
def make_cust_acct_dict(a_list: list) -> dict:

    cust_acct_dict = {}
    for item in a_list:
        cust_id, account_val = item
        if cust_id not in cust_acct_dict:
            cust_acct_dict[cust_id] = {'id': cust_id, 'accounts': []}
        elif account_val not in cust_acct_dict[cust_id]['accounts']:
            cust_acct_dict[cust_id]['accounts'].append(account_val)
    
    return cust_acct_dict


# Function to process transactions on the accounts' balances in the account log
def process_transactions(txns: list, account_log: list):

    # Setup loop to process each transaction
    for txn in txns:
        cust_id, account_id, txnType, amount = txn
    # grab the cust id from transaction list, find matching cust id in account log
        for cust in account_log:
            if cust_id == cust['id']:
                # grab accounts, for customer
                for acct in cust['accounts']:
                    # find where acct id from txn list match acct num from accounts
                    if account_id == acct['accountNumber']:
                        # look at transaction type, update that balance in the log
                        if txnType == "withdrawal":
                            acct['balance'] = round(acct['balance'] + amount, 2)
                        else:
                            acct['balance'] = round(acct['balance'] - amount, 2)
    return account_log


# For test outputting 5 rows of data like df.head()
# counter = 0
# for i in sequence:
#     comma separate variables in i = i to get assign each one
#     print(variable) - to test its been assigned to one of them
#     counter +=1
#     if counter > 5:
#         break
