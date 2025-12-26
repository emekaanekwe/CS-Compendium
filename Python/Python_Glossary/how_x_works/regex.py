import re
'''
On regular expressions
'''

"""validates email address
Returns:
    _type_: string
use regex to process the .csv data 
and validate the email addresses
"""
"""re.search()
Returns:
    _type_: a truthy object 
    
"""
"""
Returns:
    _type_: _description_
"""

s = "'s' is true iff 'x' is 1"
x = 1
re_sol = re.search('1',s)
#print(re_sol)

email_pattern = '^([a-zA-Z]+\.?){1,}@([a-zA-Z]+\.?){1,}'

valid = 'wyatt@student.monash.edu'
invalid = 'a@s.mo#$%^&(*&^%$#nash..#edu'


'''
span=(<str idx=0>, <str idx=len(str)>)

'''
email_match = re.match(email_pattern, invalid)
print(email_match)
if not email_match:
    print("valid email")
else:
    print("invalid email")







# validate an email address
def is_valid_email(email):
    """
    Check if the given email address is valid.
    
    Args:
    email (str): The email address to be checked.
    
    Returns:
    bool: True if the email is valid, False otherwise.
    """
    # Regular expression pattern for validating email addresses
    
    # Check if the email matches the pattern
    if re.match(email):
        return True
    else:
        return False

# Test the function
'''
email = input("Enter an email address: ")
if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
'''



