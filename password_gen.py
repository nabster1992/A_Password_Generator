import random
import string
from csv import writer


    



def passgen():
    s1 = string.ascii_lowercase
    
    s2 = string.ascii_uppercase

    s3 = string.digits

    s4 = string.punctuation

    platform = input("Enter name of the platform: - \n")

    pass_length  = int(input("Enter the desired length of the password: - \n"))


    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = ("".join(s[0:pass_length ]))
    print(password )
    
    passdata = [platform, password]
    
    with open('pass.csv', 'a' ) as f:
        writedata = writer(f)
        writedata.writerow(passdata)

passgen()