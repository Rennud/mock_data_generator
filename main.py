import os

from manager.create_data import create_mock_data
from manager.create_json import create_json_file


def main():
    """
    User manual,
    get input from the user and used it as an args to create data and json file
    """
    print(
        '''
        Welcome to data generator
        - first u need to define number of rows and columns
        - there must be at least one row as well as column
        - num of columns is limited to 8
        - second u need to specify name of new json_file
        - you can choose where you want to save the file
            if u leave option blank it wil save to cwd
        '''
    )
    cwd = os.getcwd()

    rows = input("Define number of rows: ")
    columns = input("Define number of columns: ")

    # Needed to change dir before cal create_mock_data cuz all csv files are in dir /csv_and_handler
    os.chdir(cwd + '/csv_and_handler')
    mock_data = create_mock_data(int(rows), int(columns))
    json_filename = input("Json file name: ")
    save_file_dest = input("Save file to: ")

    # If save_file_dest is not specified file will save to cwd
    if len(save_file_dest) == 0:
        save_file_dest = cwd

    create_json_file(mock_data, json_filename, save_file_dest)

    return print(f'File was saved to {save_file_dest}')


if __name__ == '__main__':
    main()
