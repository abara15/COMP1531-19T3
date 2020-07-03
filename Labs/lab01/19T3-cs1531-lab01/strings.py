# Author: @abara15 (GitHub)
'''
TODO Complete this file by following the instructions in the lab exercise.
'''

strings = ['This', 'list', 'is', 'now', 'all', 'together']

string_to_print = ""
for x in strings:
    string_to_print += x + " "

print(string_to_print[:-1])
print(' '.join(strings))
