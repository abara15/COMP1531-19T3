# Author: @abara15 (GitHub)
# I saw that the same for loop occurred to find the product of the first 4 and last 4 numbers.
# So I condensed this into the function "product", which took in different min and max ranges - the only thing that differed between the code for those bits.
# I also saw there was a lot of repetition with the inputs, so I made my_list an empty list and created a new list for the alphabet, and I just appended each input into the empty my_list

def product(min_range, max_range, product):
    for i in range(min_range, max_range):
        product = product * my_list[i]
    print(f"  {product}")

if __name__ == '__main__':
    alphabet = ["a", "b", "c", "d", "e"]
    my_list = []
    for i in range(0, 5):
        my_list.append(int(input(f"Enter {alphabet[i]}: ")))
    
    my_min = 999999
    for i in range(0, 5):
        if my_list[i] < my_min:
            my_min = my_list[i]
    print("Minimum: " + str(my_min))

    print("Product of first 4 numbers: ")
    product(0, 4, 1)
    print("Product of last 4 numbers")
    product(1, 5, 1)

# if __name__ == '__main__':
#     a = input("Enter a: ")
#     a = int(a)
#     b = input("Enter b: ")
#     b = int(b)
#     c = input("Enter c: ")
#     c = int(c)
#     d = input("Enter d: ")
#     d = int(d)
#     e = input("Enter e: ")
#     e = int(e)
#     my_list = [a, b, c, d, e]
#     my_min = 999999
#     for i in range(0, 5):
#         if my_list[i] < my_min:
#             my_min = my_list[i]
#     print("Minimum: " + str(my_min))
#     print("Product of first 4 numbers: ")
#     product = 1
#     for i in range(0, 4):
#         product = product * my_list[i]
#     print(f"  {product}")

#     print("Product of last 4 numbers")
#     product = 1
#     for i in range(1, 5):
#         product = product * my_list[i]
#     print(f"  {product}")