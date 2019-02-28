import base64

data = 'aGVsbG8gd29ybGQgdGhpcyBpcyBiNjQgZW5jb2RlZCBkYXRhLCB5YXkh'

with open('data.d64.out', 'wb') as f:
    f.write(base64.b64decode(data))
