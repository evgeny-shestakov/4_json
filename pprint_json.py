import json
import sys
from pprint import pprint

"""
    Load json data from file to string.
    return as a string
"""
def load_data(filepath):
    with open(filepath) as data_file:    
        return json.load(data_file)


"""
    Pretty Print string data.
    print Pretty data 
"""
def pretty_print_json(data):
    if data is not None:
        pprint(data)
    else:
        print('data is empty!')


if __name__ == '__main__':    
    try:
        json_path = sys.argv[1:2].pop()
        data = load_data(json_path)
        pretty_print_json(data)
    except:
        print('warning: please add valid json file as argument: ' + 
            'python pprint_json.py data.json')
    
