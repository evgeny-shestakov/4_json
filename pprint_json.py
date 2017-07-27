import json
import sys
import os.path
  

def load_filedata(filepath):
    if os.path.isfile(filepath):
        with open(filepath, 'r') as file_handler:
            try:
                return json.load(file_handler)
            except ValueError:
                return None


def pretty_print_json(raw_json):    
    if raw_json is not None:
        print(json.dumps(raw_json, ensure_ascii=False, 
                        sort_keys=True, indent=4))
    else:
        print('no json data!')


if __name__ == '__main__':
    raw_json = None 
    
    try: 
        raw_json = load_filedata(sys.argv[1])
    except IndexError:
        print('warning: please add valid json file as argument: ' + 
            'python pprint_json.py data.json')
            
    pretty_print_json(raw_json)        
    
