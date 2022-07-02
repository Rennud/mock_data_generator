import itertools
import json

from manager.generate_data_func import *


def create_mock_data(num_rows, num_columns):
    """
    Returns array of dicts,
    That contains desired mock data
    num_rows must be at least 1,
    num_colums must be at least 1 and maximum value is 8
    """
    mock_data = []
    if num_rows < 0 or num_columns > 8 or num_columns < 0:
        print('''
            First arg num_rows must be at least 1\n,
            Second arg num_colums must be at least 1 and maximum value is 8''')
        return False
    for _ in range(num_rows):
        person = {
            'id': get_id(),
            'name': get_name_and_gender()[0],
            'age': get_age(),
            'gender': get_name_and_gender()[1],
            'income': get_income(),
            'status': get_status(),
            'proffesion': get_random_value('professions.csv'),
            'dog': has_dog()
        }
        mock_data.append(dict(itertools.islice(person.items(), num_columns)))

    return mock_data


def create_json_file(data, filename, path_to_save):
    """
    Create new json file from given data under given filename and save it to the given path_to_save
    """
    desired_dir = path_to_save
    full_path = os.path.join(desired_dir, filename)
    with open(full_path, 'w') as json_file:
        json.dump(data, json_file)

    return print(f'File {filename} was successfully created.')
