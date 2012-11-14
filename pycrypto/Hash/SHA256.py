##https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Hash/SHA256.py

from Crypto.Hash import SHA256

h = SHA256.new()
h.update(b'Hello')
print h.hexdigest()