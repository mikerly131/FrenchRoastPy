import pandas as pd


# Function to get a list of transactions from a csv file
def get_txns_list() -> list:

    csv_txn_df = pd.read_csv('./resources/transactions.csv', low_memory=False, header=0,
                         usecols=['customerId', 'accountId', 'transactionType', 'amount'], index_col=None)
    csv_txn_dict = csv_txn_df.to_dict(orient='split')
    txn_list = csv_txn_dict['data']
    return txn_list


# Function to get a list of customers and accounts from given CSV
def get_cust_acct_list() -> list:
    csv_df = pd.read_csv('./resources/transactions.csv', low_memory=False, header=0,
                           usecols=['customerId', 'accountId'], index_col=None)
    csv_dict = csv_df.to_dict(orient='split')
    cust_acct_list = csv_dict['data']
    return cust_acct_list


# Function to get account log (list of dictionaries, each dictionary has 2 kvps, cust id and account,
# Accounts is a list of dictionaries, each dictionary is has 2 kvps account number and balance
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
def process_transactions(account_log: list, txns: list):

    # Now to figue out how to process transactions...
    # could make a transaction list like i made a list to make an account log
    # then i'd need some looping to go trough the transaction list 1 at a time
    # grab the cust id from transaction list, find matching cust id in account log
    # grab accounts, for accounts
    # find where acct id from txn list match acct num from accounts
    # look at transaction type, update that balance in the log
    pass