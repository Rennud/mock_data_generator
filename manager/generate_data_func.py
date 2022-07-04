import random
import uuid
import os
import random

from csv_and_handler.handle_csv import read_csv


def get_random_value(filename) -> str:
    """
    Returns random value from csv file
    Using this func for professions and names
    """

    path = (os.getcwd() + '/' + filename)
    value_arr = []
    for arr in read_csv(path):
        for item in arr:
            value_arr.append(item)

    return random.choice(value_arr)


def get_name_and_gender(last_names_file='last_names.csv', female_names_file='female_names.csv', male_names_file='male_names.csv'):
    """Return random full name and gender based on the first name"""
    last_name: str = (get_random_value(last_names_file))
    male_or_female = random.choice(['m', 'f'])
    gender: str = male_or_female
    if male_or_female == 'm':
        male_first_name: str = (get_random_value(male_names_file))
        return male_first_name + ' ' + last_name, gender
    elif male_or_female == 'f':
        female_first_name: str = get_random_value(female_names_file)
        return female_first_name + ' ' + last_name, gender


def get_id() -> str:
    """Returns eight chars id long"""
    return str(uuid.uuid4())[:8]


def get_age() -> int:
    """Returns int between 18-65 """
    return random.randint(18, 65)


def get_income() -> str:
    """Returns random annual income between 10 000 - 200 000 in USD"""
    return '$' + str(random.randint(10000, 200000))


def get_status() -> str:
    """Returns random status"""
    return random.choice(['single', 'married', 'in relationship'])


def get_has_dog() -> str:
    """Returns a random boolean representing whether the person has a dog"""
    return random.choice(['yes', 'no'])
