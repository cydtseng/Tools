import hashlib
import requests
import sys

# get user's choice of password from telegram
password = input("Provide desired password.")
# hash the password
hash = hashlib.sha1(password.encode("utf-8"))
hashed = hash.hexdigest().upper()

# first 5 characters of hashed password
pw_head = hashed[0:5]
pw_tail = hashed[5:]

try:
    resp = requests.get("https://api.pwnedpasswords.com/range/"+pw_head)
    resp_str = resp.content.decode("utf-8")
    #print(resp)
    resp_arr = []
    start = 0
    n = 2
    
    
    for c in resp_str:
        if n >= len(resp_str):
            break
        if resp_str[n] == '\r':
            k = n
            for i in range(2):
                resp_str.replace(resp_str[k],"")
                k+=1
            resp_arr.append(resp_str[start:n])
            n += 2
            start = n
        else:
            n+=1
    
   # print(resp_arr)

    is_detected = False
    for res in resp_arr:
        if res[0:35] == pw_tail:
            print("Given password was compromised: " + res[36:] + " times.")
            is_detected = True

    if not is_detected:
        print("Given password was compromised 0 times.")


except (requests.ConnectionError, requests.Timeout) as e:
    print("[*] Connection error.")


