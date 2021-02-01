import sys
import hashlib

help_text = """
Usage:
python hash.py <username> <password>
"""
# make sure that the first argument is given
try:
    sys.argv[1]
except IndexError:
    print help_text
    exit(0)
 
# check for second argument
try:
    sys.argv[1]
except IndexError:
    print help_text
    exit(0)
# check for third argument
try:
    sys.argv[2]
except IndexError:
    print help_text
    exit(0)

hash_function = hashlib.md5

username = sys.argv[1]
hashed_pass = hash_function(sys.argv[2]).digest()

f = open("passwords.txt", "a")
f.write(username + "\t")
f.write(hashed_pass + "\n")
