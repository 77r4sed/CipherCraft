import random 
import string 



def generate_password(length: int = 34):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password
 
    
print("*********************************************")
print("*          Password Generator Tool          *")
print("*          Developed by [77r4sed]        *")
print("*          Version 1.0                      *")
print("*          (c) 2024 [77r4sed]            *")
print("*********************************************")
print("")

    

def generate_multiple_passwords(num_passwords=10, length=20):
    passwords = []
    for _ in range(num_passwords):
        passwords.append(generate_password(length))
    return passwords
# Get number of passwords from user
num_passwords = int(input("Enter number of passwords to generate: "))

# Generate passwords
generated_passwords = generate_multiple_passwords(num_passwords)

# Print generated passwords
for password in generated_passwords:
    print(password)







