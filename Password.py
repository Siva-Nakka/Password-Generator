import random
chars1 = "abcdefghijklmnopqrstuvwxyz"
chars2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars3="1234567890"
chars4="/-+=!@#$%^&*"
length_of_password = int(input("Enter Number Of Characters In Password:"))
def pass_generator(size):
    password = ''
    for i in range(size):
        password += random.choice(chars1)+random.choice(chars2)+random.choice(chars3)+random.choice(chars4)
    return password[0:size]
print(pass_generator(length_of_password))
