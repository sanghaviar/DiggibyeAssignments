from util import *
'''
        username@websitename.extension
        username = [a-z],[A-Z],[0-9],[_-]
        website name = [a-z],[A-Z],[0-9]
        extension = [a-z],[A-Z]
        maximum length of extension = 3
'''

n = int(input())
emails = []
for i in range(n):
  email = input().strip()
  if email_validation(email):
    emails.append(email)
print(sorted(emails))