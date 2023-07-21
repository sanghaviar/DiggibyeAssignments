import re
def email_validation(emails):
    # return True if s is a valid email, else return False
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, emails)