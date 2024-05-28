
import hashlib



password="password"
hash=hashlib.sha256(password1.encode('utf-8'))
print(hash.hexdigest())