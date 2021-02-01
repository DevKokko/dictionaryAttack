import hashlib
import sys

help_text = """
-h --help       prints help menu (you're looking at it)

Usage:
python hack.py <password file> <wordlist file>
python hack.py pswd.txt rockyou.txt

"""
try:
    sys.argv[1]
except IndexError:
    print help_text
    exit(0)

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
    print help_text
    exit(0)

try:
    sys.argv[1]
    sys.argv[2]
except IndexError:
    print "Not enough arguments."
    print help_text
    exit(0)

#using md5 function to encryct passwords
hash_function = hashlib.md5


def simple_hash(value):
    return hash_function(value).digest()

dictData = {}  
with open(sys.argv[1], 'r') as f:
    for line in f:
        data = line.split()
        dictData[data[0]] = data[1]

with open(sys.argv[2], 'r') as f:
    password_list = f.read()

password_list = password_list.split("\n")

n_pass = len(password_list)

print "Cracking...\n"
found = False
for key in dictData:
    for test in password_list:
        if simple_hash(test) == dictData[key]:
            print "Found password for --> " ,key
            print "password is -->", test + "\n"
            found = True
            break
if found == True:
    print "Found " 
else:
    print "No matching passwords found"


