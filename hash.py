import sys
import hashlib

help_text = """
--help -h       prints help menu (you're looking at it)

Usage:
python hash.py <hash option> <word>
python hash.py md5 password
"""
# make sure that the first arguent is given
try:
    sys.argv[1]
except IndexError:
    print help_text
    exit(0)
# check for help needed
if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print help_text
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
