import json
import sys
from pprint import pprint


def load_data(filepath):
    """
        Load json data from file to string.
        return as a string
    """
    with open(filepath) as file_handler:    
        return json.load(file_handler)


def pretty_print_json(raw_json):    
    """
        Pretty Print string data.
        print Pretty data 
    """
    if raw_json is not None:
        pprint(raw_json)
    else:
        print('raw_json is empty!')


if __name__ == '__main__':    
    try:
        json_path = sys.argv[1:2].pop()
        raw_json = load_data(json_path)
        pretty_print_json(raw_json)
    except (IndexError, FileNotFoundError, json.decoder.JSONDecodeError):
        print('warning: please add valid json file as argument: ' + 
            'python pprint_json.py data.json')
    
