# Author: @abara15 (GitHub)
def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    strong = 1
    moderate = 2
    poor = 3
    horrible = 4

    length = len(password)
    num_count = 0
    upper_count = 0
    lower_count = 0

    for i in password:
        if (i.isdigit()):
            num_count += 1
        if (i.isupper()):
            upper_count += 1
        if (i.islower()):
            lower_count += 1
    
    if (length >= 12 and num_count >= 1 and upper_count >= 1 and lower_count >= 1):
        return strong
    elif (length >= 8 and num_count >= 1):
        return moderate
    elif (password == "password" or password == "iloveyou" or password == "123456"):
        return horrible
    else:
        return poor

    #pass

if __name__ == '__main__':
    print(check_password("ihearttrimesters"))

def test_strong_password():
    password = "Programming7"
    assert(check_password(password) == 1)

def test_moderate_password():
    password = "character1"
    assert(check_password(password) == 2)

def test_poor_password():
    password = "poor"
    assert(check_password(password) == 3)

def test_horrible_password():
    password = "123456"
    assert(check_password(password) == 4)

def test_random_test():
    password = "thisisalongpasswordwithnouppercase1"
    assert(check_password(password) == 2)