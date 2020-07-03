# Author: @abara15 (GitHub)
import pickle
from unpickle import frequent
from json import dumps

unpickle_file = open("shapecolour.p", "rb")
load = pickle.load(unpickle_file)
unpickle_file.close()

dataStructure = {
    "mostCommon" : {
        "colour" : frequent(load, 'colour'), # "[most-common-colour]",
        "shape" : frequent(load, 'shape') # "[most-common-shape]"
    },
    "rawData" : load # [insert-raw-data-from-shapecolour.p]
}

def write_file(filename, json):
    f = open(filename, 'a')
    f.write(json)
    f.close()

write_file('processed.json', dumps(dataStructure))