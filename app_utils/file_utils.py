"""
Module for the choosing a file, and writing to a file
"""
import json


# Function to prompt for file to run program on
def get_file_name():
    while True:
        try:
            file_id = int(input('Select file to process: 1 for first csv, 2 for second csv: \n'))
        except ValueError:
            print('Enter a 1 or a 2')
        if 0 <= file_id <= 3:
            break
        else:
            print('Enter a 1 or a 2')

    if file_id == 1:
        file_name = "transactions"
    else:
        file_name = "secondset"

    return file_name


# Function to write the account_log to a json file in json_file directory
def write_to_json(account_log: list, file_name):

    with open(f'./json_files/account_log_{file_name}.json', 'w') as output_file:
        json.dump(account_log, output_file)
        output_file.close()
