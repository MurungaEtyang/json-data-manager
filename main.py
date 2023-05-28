import json
import hashlib
import pywhatkit

print("Validate Data")
username = input("Enter your username: ")
new_password = input("Enter your password: ")

n_pd = hashlib.md5(new_password.encode()).hexdigest()
with open("data.json", "r") as f:
    data1 = json.load(f)

# Search for matching credentials in the data
matching_section = None
for section in data1:
    if section["username"] == username and section["password"] == n_pd:
        matching_section = section
        break

if matching_section:
    matching_json = json.dumps(matching_section, indent=2)
    pywhatkit.sendwhatmsg("PHONE NUMBER", matching_json,17, 11)
    print(matching_json, type(matching_json))
else:
    print("Invalid username or password")
