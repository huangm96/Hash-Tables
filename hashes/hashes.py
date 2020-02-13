import hashlib

key = b"str"
my_string = "something here".encode()

for i in range(10):
    hashed = hashlib.sha256(key).hexdigest()
    print(hashed)
    # breakpoint()

for i in range(10):
    hashed = hash(key)
    print(hashed)
    print(hashed % 8)

