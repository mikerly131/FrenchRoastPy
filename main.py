"""
Program that processes the set CSV transaction file to create an account log with balances based on the transactions
"""
import utilities
import sys


def run_again():
    choice = input("Run program again? Y or N \n")
    if choice == 'Y' or choice == 'y':
        main()
    else:
        print("Goodbye")


def main():

    # Prompt for file selection
    file_name = utilities.get_file_name()

    # Get the list of transactions to process
    raw_txn_list = utilities.get_txns_list(file_name)
    txn_list = utilities.convert_txn_amounts(raw_txn_list)

    # Get the accounts by customer id from dataframe, make it a dict, will be of lists
    cust_accts_list = utilities.get_cust_acct_list(file_name)

    # Create a dictionary of customer ids mapped to accounts
    cust_acct_log = utilities.get_account_log(cust_accts_list)

    # Process transactions to update the account log -> aka update balance of each account in log for each transaction
    # updated_account_log = utilities.process_transactions(cust_acct_log, transaction_list)
    list_unpack_test = utilities.process_transactions(txn_list, cust_acct_log)

    # Write the account_log to a json file in json_file directory
    utilities.write_to_json(list_unpack_test, file_name)
    run_again()


if __name__ == "__main__":
    sys.exit(main())

