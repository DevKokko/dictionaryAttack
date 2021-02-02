import sys
import nacl.pwhash

help_text = """
Usage:
python hash.py 
"""

if len(sys.argv)>1:
    print help_text
    exit(0)

# A dictionary object which stores user's data (username, password)
userData = {
    "user001" : "hello",
    "user002" : "pass2",
    "user003" : "athens",
    "user004" : "pass4",
    "user005" : "pass5",
    "user006" : "pass6",
}

f = open("passwords.txt", "w")
#iterrate throught userData's dictionary and store the data into a file named passwords.txt
for username,password in sorted(userData.iteritems()): 
    hashed_password = nacl.pwhash.str(password)
    f.write(username + "\t")
    f.write(hashed_password + "\n")
f.close()