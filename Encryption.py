import secrets
import string
class Encryption:
    alphabet = string.ascii_letters
    seed = ''.join(secrets.choice(alphabet) for i in range(100)).upper()
    print(seed)

