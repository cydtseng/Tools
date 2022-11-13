import string
# get true random numbers
import secrets

def gen_pw(pw_len: int, include_symbols: bool, include_upper: bool):
    # let users decide if they wish to include symbols or uppercase letters
    combination = string.ascii_lowercase + string.digits
    if include_upper:
        combination += string.punctuation
    if include_symbols:
        combination += string.ascii_uppercase

    combination_len = len(combination)
    new_password = ""

    for _ in range(pw_len):
        new_password += combination[secrets.randbelow(combination_len)]

    return new_password

for index in range(5):
    print("Password" , index+1, ":", gen_pw(pw_len=20, include_symbols=True, include_upper=False))


