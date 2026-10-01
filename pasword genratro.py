import secrets
import string
print("dobar dan evo random pasword")
alphabet=string.ascii_letters + string.digits
password = ""
while len(password)<12:
    password +=secrets.choice(alphabet)

print(password)