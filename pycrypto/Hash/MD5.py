##https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/Hash/MD5.py

from Crypto.Hash import MD5

h = MD5.new()
h.update(b'Hello')
print h.hexdigest()