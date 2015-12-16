'''
Created on Dec 15, 2015

@author: Robert
'''
import hashlib
import re

secret_key = str("ckczppom").encode(encoding='utf_8', errors='strict')
print(secret_key)

ctr = 0
while 1 == 1:
    md5_hash = hashlib.md5()
    md5_hash.update(secret_key)
    md5_hash.update(str(ctr).encode(encoding='utf_8', errors='strict'))
    hex_digest = md5_hash.hexdigest()
    if re.search('^000000', hex_digest):
        break
    ctr += 1
print(ctr)

