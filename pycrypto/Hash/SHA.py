#https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Hash/SHA.py

from Crypto.Hash import SHA

h = SHA.new()
h.update(b'Hello')
print h.hexdigest()