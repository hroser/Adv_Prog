import re

'''
str = 'the mail address is al22_.ice.b@google.com thanks'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
# If-statement after search() tests if it succeeded
if match:
  print('found:', match.group()) ## 'found word:cat'
else:
  print('did not find')
'''

## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
  # do something with each found email string
  print(email)