from random import choice, shuffle
from string import ascii_letters

while True:
    while True:  # getting passwords length from user
        print("Do you want to generate password just by total length or by number of particular signs?")
        generate_type = input("Enter 'l' for length or 'n' for number: ")
        if generate_type == 'l':
            length_password = int(input("How long you want password to be? Enter number: "))
            break
        elif generate_type == 'n':
            number_letters = int(input("Enter how many letters password will contain: "))
            number_num = int(input("Enter how many numbers password will contain: "))
            number_special = int(input("Enter how many special characters password will contain: "))
            length_password = number_letters + number_num + number_special
            break
        else:
            print("Error, press 'l' for length or 'n' for number")
            continue
    special_characters = ['$', '#', '@', '!', '*']
    letters = [letter for letter in ascii_letters]
    nums = [str(i) for i in range(10)]
    password = []
    signs = special_characters + letters + nums
    for random_sign_index in range(length_password):
        if generate_type == 'l':
            password.append(choice(signs))
        elif generate_type == 'n':
            password = [choice(special_characters) for i in range(number_special)]
            password += [choice(letters) for i in range(number_letters)]
            password += [choice(nums) for i in range(number_num)]
        shuffle(password)
    print("".join(map(str, password)))
