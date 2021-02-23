"""
Module for working with a json object.
"""

import json


def read_json(path: str) -> dict:
    """
    Reads JSON file.
    """
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def if_dict(data: dict):
    """
    Return resault for the dict and ask user to choose a key.
    """
    key_list = [key for key in data.keys()]
    print("This is a dict. Choose a key from the list:")
    print(key_list)
    choosen_key = input()
    return data[choosen_key]


def if_list(data: list):
    """
    Return resault for the list and ask user to choose an element.
    """
    element_list = [element for element in data]
    ranging = len(element_list)
    print("This is a list. Choose an index in range from 0 to " + str(ranging-1) +" to see an element:")
    choosen_element = int(input())
    return data[choosen_element]


def if_str_int_float_bool(data):
    """
    Return resault for str, int, float and bool.
    """
    type_data = type(data)
    if type_data == str:
        print("This is a string. Do you want to display the string?")
    elif type_data == int or type_data == float:
        print("This is a number. Do you want to display this number?")
    else:
        print("This is boolean. Do you want to display it?")
    answer = input()
    while answer:
        if answer.lower() in ['yes', 'y']:
            print(data)
            answer = False
        elif answer.lower() in ['no', 'n']:
            print('This is the end of the file.')
            answer = False
        else:
            answer = input('Enter a correct answer:')


def main(path: str):
    """
    Main function.
    """
    data = read_json(path)
    while type(data) in [dict, list, str, int, bool, float]:
        data_type = type(data)
        if data_type == dict:
            data = if_dict(data)
        elif data_type == list:
            data =  if_list(data)
        else:
            return if_str_int_float_bool(data)
    print('This is the end of the file.')


if __name__ == "__main__":
    path = 'file.json'
    main(path)