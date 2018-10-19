from Crypto.Cipher import AES
import base64

THIS_IS_US = "1997051819920725"
universe = True
stars = True
entity = True


def decrypt_val(birthday_wish):
    dec_secret = AES.new(THIS_IS_US[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(birthday_wish))
    happy_birthday = raw_decrypted.rstrip("\0")
    return happy_birthday


birthday_wish = """OUvQ7imqNpKjUw+ck6Bs1urrrFrU4gq59kMsST9s3bcFy8MQwEoEvb/RqeSWGhbOFHzUtZJqQ4DnKBbj7vw7CdTmkjVTBZsdxbtb2j4Kbk9xFKYorP2m3bSqoy+MOoU/fxEiTQuK7CcTx/Od/P4SWW8N5t8qwgixTDH6UQcOSgZwb08MS55sbbxqB7YOGiYF3zO9rMdPJNbJU5sC/9BKoZktVQPGCiEPjDCf3XPhzCoUy6Olzp0l8TM73kAGAvu+VyW3Ax400+4pCePylhg6uM4COjc5MnnhLEo/k2pQhDTXYtulcgzcacSgs+3qySPH3Bywivu4NKAYN3h3+ty/YbTjmUKS42SC3+P+wVYEmxGY+rSv9zU7DP1HjWn5MQWt2VtG/CT7i+P5cRjgPQrtm0T5CNsYcKO53UpoP+HIsShmGB60TVF4Uv7DZRUPa6aFaCGqR7oS66Ls0Pxi3DVhNwdIHZDvEP7RJcSf33cueWMeAHD1VlJinmVVrhKobtvRLrVmkuw4Fh2btUSrOyiIc7RfFnNFOfYeVRT7Dlr9UFDiLSuTgHHu0GK/BIPl4k/Qbsqod7ZHwlpjGdVIyIM3Y629mkvmR8nRc6WXw/u2BoI531TZHpoHTXBntJavT5h0SaGpAqH2InslG/xd4glWDo5qfL0x3GqjwQDnQpxeEBv1ZFU+hHrTrPCIg/K2k1+eHTjFOGH7vftnsx/07JgWgupgvOChqGW5XePx4kKOJWB2fqocKdZW2HKlXJjhNBWQ6/6fs0LZHFnP7Q5MmD+jTI3HxR4zpMk1//ywALNLDvPvXvD5h0TZk9tRLWb1X90dV4NENFk4AMjt4CfT4cxfZipvbzXXZV8J8BNs+MaUgrLyprqeHU3Di0Dm0kKXZ/JPAUujq+YN03zAdie/aYzJJumV9RmLMRQIXuqIjmbSrMo4wlAG/UL+7lFuvKzyRkPQqBwFE1V5PsomzCBdxnkFMHgtmk9ZBjcURXVoDbgpzzxbKxy6Nwex5jq3o0bQGyZWt9uxTVZ1Ju4oNFBuV+P3Q0eumWANQtCkgg4RtRFARqc="""
my_wish = decrypt_val(birthday_wish)

while(universe & stars & entity):
    print my_wish
    print
    print "I Love youuuuu sooooo muchhhh Shwethaaa!! <3 :*"
    print ""