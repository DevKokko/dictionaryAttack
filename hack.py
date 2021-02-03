import sys
import nacl.pwhash

help_text = """
-h --help       prints help menu (you're looking at it)

Usage:
python hack.py <password file> <wordlist file>
python hack.py passwords.txt word-list.txt

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

#A function that takes a password value and returns a hashed value
def simple_hash(value):
    return hash_function(value).hexdigest()

# A dictionary which stores only passwords 
dictData = {}  

#Filtering data from the input file with the passwords
with open(sys.argv[1], 'r') as f:
    for line in f:
        data = line.split() #Spliting the data for every line
        dictData[data[0]] = data[1] #Storing passwords 

with open(sys.argv[2], 'r') as f:
    password_list = f.read()
    
password_list = password_list.split("\n") 


#Checking if passwords in the password's file match to the word list file 
print "Cracking...\n"
found = False
for key in dictData:
    for test in password_list:
		try:
			nacl.pwhash.verify(dictData[key], test)
			print "Found password for --> " +key
			print "password is -->" +test + "\n"
			found = True
			break
		except:
			pass
            
if found == True:
    print "Success! Passwords in the txt file given match to the input file  " 
else:
    print "No matching passwords found"


