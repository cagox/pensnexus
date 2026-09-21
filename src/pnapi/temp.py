from crypto.passwords import hash_password, verify_password

#
# Feel free to ignore this file. It is just for testing various things.
#

password = "my_secure_password"

hash = hash_password(password)
print(f"Hashed password: {hash}")

is_valid = verify_password(hash, password)
print(f"Password is valid: {is_valid}")

is_valid_wrong = verify_password(hash, "wrong_password")
print(f"Password is valid for wrong password: {is_valid_wrong}")