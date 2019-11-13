import sys, os

author_ = 'samuel shoyemi a.k.a SHOW'
copyright()

# encrypting a message
print('''This is a program to help encrypt your messagge
with two keys known to you and the receiver alone.
The first key is a set of less than 10 non repeating alphabets,
with key two as a set of numerals from 0 to 9,
corresponding to number of key one.
E.g Key one = "aeioutgyls
    Key two = "1234567890"
Well that's a suggestion, you can use any key values of your choice
TIP: Key one may contain space to make the encrypted message look more complex
''')


def encrypt(msg):
    key_one = str(input("Input key one: "))  # E.g  "aeioutgyls"
    key_two = str(input("Input key two: "))  # E.g  "1234567890"

    try:
        transkeys = str.maketrans(key_one, key_two)
    except ValueError:
        print('Sorry, both keys must have equal length')

    # the make.trans() method returns a translation table that maps each
    # character in the first tab into the same position in the second tab.
    # Then this table is passed to the translate() function

    msg_input = str(input("Write message to be encrypted: "))
    print("\n")
    msg += msg_input.translate(transkeys)  # encrypting the input message

    return msg, key_one, key_two

# calling the above function by assigning a return tuple


msg = ''
encrypted_msg, key_one, key_two = encrypt(msg)

# to store the encrypted message


def store_message(encrypted_msg):
    mymessage = open('mymessage.txt', 'w+')
    mymessage.write(encrypted_msg)
    mymessage.close()

store_message(encrypted_msg)

# print(encrypted_msg)

path = 'C:\\Users\\SAMUEL PC\\Python37\\Examples\\mymessage.txt'
print(f'Your message have been encrypted Successfully and stored in path {path}')
print("\n")
print('Would you like to decrypt your message? Yes/No')

# this function checks the user's entered keys, a similar function is the
# username and password function


def check_func(key_one, key_two):
    print('Please input correct Keys to decrypt\n')

    print('Note you only have 3 trials')
    # set count to an initial value of 0
    count = 0
    # set the true count to zero, this will be used for returning a confirmation
    true = 0
    while count < 3:
        key_1 = input('Key_one: ')
        key_2 = input('Key_two: ')

        if key_1 == key_one and key_2 == key_two:
            print('Decrypting.....')
            true += 1
            break
        else:
            print('Incorrect Keys\nPlease Retry')
            count += 1
            if count == 3:
                print('Number of trials over')
            continue
    return true

# a decrypt function


def decrypt(key_one, key_two, command, encrypted_msg):
    # after the above function is been executed and returned true=1
    # and the input command is yes
    if command == "YES":
        correct = check_func(key_one, key_two)  # calling the check_func function
        # the check function returns a 1 as true or a 0 as false, and stored in the variable correct
        if correct == 1:
            # decrypt the message if the inputs is found true
            transkeys = encrypted_msg.maketrans(key_two, key_one)
            decrypted_msg = encrypted_msg.translate(transkeys)
            print('msg = '+decrypted_msg)
    elif command == "NO":
        print("Thank you and Good bye!")
        sys.exit()
    else:
        print('Invalid Input')
        print("Good Bye!")
        sys.exit()
    return encrypted_msg


command = input(": ").upper()
decrypt(key_one, key_two, command, encrypted_msg)

