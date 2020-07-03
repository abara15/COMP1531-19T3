# Author: @abara15 (GitHub)
# I added functions that get the name and birth year because we don't want to directly access self.name and self.birth_year.
# Also imported datetime to get the current year and find the correct age.

import datetime

class Student:
    def __init__(self, firstName, lastName, birth_year):
        self.name = firstName + " " + lastName
        self.birth_year = birth_year
    def get_name(self):
        return self.name
    def get_birth_year(self):
        return self.birth_year

if __name__ == '__main__':
    s = Student("Rob", "Everest", 1961)
    years_old = datetime.datetime.now().year - s.get_birth_year()
    print(f"{s.get_name()} is {years_old} years old")





# class Student:
#     def __init__(self, firstName, lastName, birth_year):
#         self.name = firstName + " " + lastName
#         self.birth_year = birth_year

# if __name__ == '__main__':
#     s = Student("Rob", "Everest", 1961)
#     years_old = 2019 - s.birth_year
#     print(f"{s.name} is {years_old} old")
