import json
from . import configutil 
import os
import errno

def openJSON(filepath):    
    """ open a json file and return a JSON object """   
    with open(filepath) as data_file:    
        data = json.load(data_file)
    return data

def save(data):
    """ save some data into the output file """
    with open(configutil.getOutputFilePath(),"w") as file:        
        file.write(data)

def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise