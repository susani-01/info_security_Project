from itertools import count
OFFSET = 2048

def encode(msg, mask, encoded):
    msg = [ord(ch) for ch in msg]
    img = bytearray(open(mask, 'rb').read())
    for k, n in zip(count(OFFSET), msg):
        img[k] ^= n
    open(encoded, 'wb').write(img)

def decode(mask, encoded):
    img1 = bytearray(open(mask, 'rb').read())[OFFSET:]
    img2 = bytearray(open(encoded, 'rb').read())[OFFSET:]
    msg = [chr(b1 ^ b2) for b1, b2 in zip(img1, img2) if b1 != b2]
    return ''.join(msg)

# Encoding
mask = 'sane.bmp'
encoded = 'sane2.bmp'
message = 'To be or not to be, that is the question.'
encode(message, mask, encoded)
# note: no on-screen output, new file is created containing hidden message

# Decoding
mask = 'sane.bmp'
encoded = 'sane2.bmp'
message = decode(mask, encoded)
print(message)
# prints the secret message retreived from the image file