# Prettify JSON

Uses: json, sys, os.path


Module consists of 2 functions:


load_filedata(filepath):

- Load json data from file to string.

and


pretty_print_json(raw_json):

- Pretty Print string raw_json.


# Quickstart

please add valid json file as argument

get some json data file and feed it as a param!

python pprint_json.py data.json

Example of script launch on Linux, Python 3.5:

```#!bash

$ python pprint_json.py <path to file>
[                                                                                                                                                                                                                   
    {                                                                                                                                                                                                               
        "Cells": {                                                                                                                                                                                                  
            "Address": "улица Академика Павлова, дом 10",                                                                                                                                                           
            "AdmArea": "Западный административный округ",                                                                                                                                                           
            "ClarificationOfWorkingHours": null,                                                                                                                                                                    
            "District": "район Кунцево",                                                                                                                                                                            
            "IsNetObject": "да",                                                                                                                                                                                    
            "Name": "Ароматный Мир",                                                                                                                                                                                
            "OperatingCompany": "Ароматный Мир",                                                                                                                                                                    
            "PublicPhone": [                                                                                                                                                                                        
                {                                                                                                                                                                                                   
                    "PublicPhone": "(495) 777-51-95"                                                                                                                                                                
                }                                                                                                                                                                                                   
            ],   

...


```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
