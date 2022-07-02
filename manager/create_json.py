import json
import os


def create_json_file(data, filename, path_to_save):
    """
    Create new json file from given data under given filename and save it to the given path_to_save
    """
    desired_dir = path_to_save
    full_path = os.path.join(desired_dir, filename)
    with open(full_path, 'w') as json_file:
        json.dump(data, json_file)

    return print(f'File {filename} was successfully created.')
