import json
from collections import namedtuple

def json2obj(d): 
    return namedtuple('X', d.keys())(*d.values())