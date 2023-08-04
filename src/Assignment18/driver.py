'''
        username@websitename.extension
        username = [a-z],[A-Z],[0-9],[_-]
        website name = [a-z],[A-Z],[0-9]
        extension = [a-z],[A-Z]
        maximum length of extension = 3

INPUT:
3
abc@gamil.com
xyyz12@gmail.com
ab123@gmail.in

'''
from util import *

n = int(input())
emails = []
for i in range(n):
    email = input().strip()
    emails.append(email)
email_validation(emails)
