from Crypto.Cipher import AES
import base64

MASTER_KEY = "1992199219921992"


def encrypt_val(clear_text):
    enc_secret = AES.new(MASTER_KEY[:32])
    tag_string = (str(clear_text) +
                  (AES.block_size -
                   len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))

    return cipher_text


def decrypt_val(cipher_text):
    dec_secret = AES.new(MASTER_KEY[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text))
    clear_val = raw_decrypted.rstrip("\0")
    return clear_val

msg = """She is beautiful ban :P :(
"""

msg2 = "Happy Birthday Shwetha! My pondatti <3"
encryVal = encrypt_val(msg2)
print encryVal
decryVal = decrypt_val(encryVal)
print 'Decrypted!'
print ''
print decryVal
