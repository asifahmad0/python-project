import re
email=" ^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$ "
user=input("entre your email ")

if re.search(email, user):
    print(" email conformed")

else:
    print(" wrong email ")