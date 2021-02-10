
import sys
import os
import requests


dc = input("DC ip?: ")
domain = input("domain?: ")
computername = input("computername?: ")

print("Ок, поехали")

if not os.path.exists(r"C:\temp"):
    os.mkdir(r"C:\temp")
    print("Папка создана.")

url = f"http://{dc}/invite?computername={computername}&domain={domain}"
r = requests.get(url)
invite_bin = r.content
invite_file = "C:\\temp\\temp.invite"
with open(invite_file, "wb") as f:
    f.write(invite_bin)
