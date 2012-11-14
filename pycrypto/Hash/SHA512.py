##https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Hash/SHA512.py

from Crypto.Hash import SHA512

h = SHA512.new()
h.update(b'Hello')
print h.hexdigest()

