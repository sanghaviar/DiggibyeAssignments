import re
def email_validation(emails):
    # return True if s is a valid email, else return False
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    valid_emails = []
    for email in emails:
        if re.match(pattern, email):
            valid_emails.append(email)
    # print("Valid email addresses:")
    sorted_emails = sorted(valid_emails)
    print(sorted_emails)
    return sorted_emails
