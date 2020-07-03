# Author: @abara15 (GitHub)
import pickle

def frequent(load, key):
    new_list = []
    for p in load:
        new_list.append(p[key])

    counter = 0
    num = new_list[0] 
      
    for i in new_list: 
        curr_frequency = new_list.count(i) 
        if(curr_frequency > counter): 
            counter = curr_frequency 
            num = i 
    return num

unpickle_file = open("shapecolour.p", "rb")
load = pickle.load(unpickle_file)
unpickle_file.close()

colour = frequent(load, 'colour')
shape = frequent(load, 'shape')

print("Colour:", colour)
print("Shape:", shape)