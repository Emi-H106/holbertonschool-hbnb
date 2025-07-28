import bcrypt

hashed = bcrypt.hashpw(b"admin1234", bcrypt.gensalt())
print(hashed.decode())

