email = "  daveshashwat46@gmail.com  " 
print(f"email = {email}")
print(f"len = {len(email)}")
#it removes extra spaces from both ends
#lstrip-> removes spaces from left side
email= email.lstrip()
print(f"Email = {email}")
print(f"Email length={len(email)}")
#rstrip-> Removes spaces from right side 
email= email.rstrip()
print(f"Email = {email}")
print(f"Email length={len(email)}")
email  = email.strip()
print(f"email = {email}")
print(f"len = {len(email)}")