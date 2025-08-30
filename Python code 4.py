import re

def check_password_strength(password):
    strength=0

    #Length check
    if len(password)>=8:
        strength+=1

    #Uppercase check
    if re.search(r'[A-Z]',password):
        strength+=1

    #Lowercase check
    if re.search(r'[a-z]',password):
        strength+=1

    #Digit check
    if re.search(r'\d',password):
        strength+=1

    #Special character check
    if re.search(r'[!@#$%^&*()><?":{}|]',password):
        strength+=1

    #Strength rating
    if strength<=2:
        return"Weak"
    elif strength==3 or strength==4:
        return "Good"
    else:
        return "Strong"

#Example usage
password=input("Enter your password:")
print("Password Strength:",check_password_strength(password))
