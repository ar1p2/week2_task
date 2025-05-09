import hashlib


users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    if username in users:
        print("User already exists!")
    else:
        users[username] = hash_password(password)
        print(f"Created new user: {username}")

def login(username, password):
    hashed = hash_password(password)
    if username in users and users[username] == hashed:
        print("Login Successful")
    else:
        print("Login Failed")


register("Appi", "mypassword")   
login("Appi", "mypassword")      
login("Appi", "wrongpassword")   
register("Appi", "anotherpass")  
