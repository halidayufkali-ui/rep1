password = input("create password: ")

if len(password) >= 8:
    print("Password is strong enough.")
else:
    print("Password is too easy.")