"""
Program that processes the set CSV transaction file to create an account log with balances based on the transactions
"""
from app_utils import acct_utils, file_utils
import sys


def run_again():
    choice = input("Run program again? Y or N \n")
    if choice == 'Y' or choice == 'y':
        main()
    else:
        print("Goodbye")


def main():

    # Prompt for file selection
    file_name = file_utils.get_file_name()

    # Get the list of transactions to process
    raw_txn_list = acct_utils.get_txns_list(file_name)
    txn_list = acct_utils.convert_txn_amounts(raw_txn_list)

    # Get the accounts by customer id from dataframe, make it a dict, will be of lists
    cust_accts_list = acct_utils.get_cust_acct_list(file_name)

    # Create a dictionary of customer ids mapped to accounts
    cust_acct_log = acct_utils.get_account_log(cust_accts_list)

    # Process transactions to update the account log -> aka update balance of each account in log for each transaction
    # updated_account_log = acct_utils.process_transactions(cust_acct_log, transaction_list)
    list_unpack_test = acct_utils.process_transactions(txn_list, cust_acct_log)

    # Write the account_log to a json file in json_file directory
    file_utils.write_to_json(list_unpack_test, file_name)
    run_again()


if __name__ == "__main__":
    sys.exit(main())
