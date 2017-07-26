# Prettify JSON

Uses: pprint, sys, json modules


Module consists of:

"""
    Load json data from file to string.
    return as a string
"""
def load_filedata(filepath):

and

"""
    Pretty Print string raw_json.
    print Pretty data 
"""
def pretty_print_json(raw_json):


# Quickstart

please add valid json file as argument
 
python pprint_json.py data.json

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>

[{'Cells': {'Address': 'улица Академика Павлова, дом 10',                                                                                                                                                           
            'AdmArea': 'Западный административный округ',                                                                                                                                                           
            'ClarificationOfWorkingHours': None,                                                                                                                                                                    
            'District': 'район Кунцево',                                                                                                                                                                            
            'IsNetObject': 'да',                                                                                                                                                                                    
            'Name': 'Ароматный Мир',                                                                                                                                                                                
            'OperatingCompany': 'Ароматный Мир',                                                                                                                                                                    
            'PublicPhone': [{'PublicPhone': '(495) 777-51-95'}],                                                                                                                                                    
            'TypeService': 'реализация продовольственных товаров',                                                                                                                                                  
            'WorkingHours': [{'DayOfWeek': 'понедельник',                                                                                                                                                           
                              'Hours': '09:30-22:30'},                                                                                                                                                              
                             {'DayOfWeek': 'вторник', 'Hours': '09:30-22:30'},                                                                                                                                      
                             {'DayOfWeek': 'среда', 'Hours': '09:30-22:30'}, DO add output example

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
