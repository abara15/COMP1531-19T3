# Author: @abara15 (GitHub)
import sys

MESSAGE_LIST = []

def authorise(function):
    def wrapper(*args, **kwargs):
        if args[0] == "CrocodileLikesStrawberries":
            return function(*args, **kwargs)
        else:
            return "Invalid authentication"
    return wrapper

@authorise
def get_messages(token):
    return MESSAGE_LIST

@authorise
def add_messages(token, msg):
    global MESSAGE_LIST
    MESSAGE_LIST.append(msg)

if __name__ == '__main__':
    auth_token = ""
    if len(sys.argv) == 2:
        auth_token = sys.argv[1]

    add_messages(auth_token, "Hello")
    add_messages(auth_token, "How")
    add_messages(auth_token, "Are")
    add_messages(auth_token, "You?")
    print(get_messages(auth_token))
















# import sys

# MESSAGE_LIST = []

# def authorised(auth_token):
#     return auth_token == "CrocodileLikesStrawberries"

# def get_messages(auth_token):
#     if not authorised(auth_token):
#         raise ValueError("Invalid authentication")
#     return MESSAGE_LIST

# def add_messages(auth_token, msg):
#     global MESSAGE_LIST
#     if not authorised(auth_token):
#         raise ValueError("Invalid authentication")
#     MESSAGE_LIST.append(msg)

# if __name__ == '__main__':
#     auth_token = ""
#     if len(sys.argv) == 2:
#         auth_token = sys.argv[1]

#     add_messages(auth_token, "Hello")
#     add_messages(auth_token, "How")
#     add_messages(auth_token, "Are")
#     add_messages(auth_token, "You?")
#     print(get_messages(auth_token))
