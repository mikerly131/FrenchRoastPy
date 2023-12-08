import csv


# Function to empty rows 1 to n from a csv file into a list
def get_csv_data(filepath):

    with open(f'{filepath}', 'r') as csvfile:
        # create the object of csv.reader()
        csv_file_reader = csv.reader(csvfile,delimiter=',')
        for row in csv_file_reader:
            print(row)



