#! /usr/bin/python3

import re, pyperclip

#Create a regex for phone numbers
"""phoneRegex = re.compile(r'''
# 123-456-7890, 123-4567, (123)345-6789, ext.12345, x12345
(
((\d\d\d)|(\(\d\d\d)))?     # area code
(\s|-)                      # first separator
\d\d\d                      # first 3 digits
-                           # separator
(\d\d\d\d                    # last 4 digits
(((ext(\.)?\s)|x)           # extention
(\d{2,5}))?                 # other kind of extention
)
''', re.VERBOSE)"""
phoneRegex = re.compile(r'(((\d\d\d)|(\(\d\d\d))(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))?)', re.VERBOSE)


#Create a regex for e-mail address
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+
@
[a-zA-Z0-9_.+]+''', re.VERBOSE)


#Get text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedphone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)

allphonenumbers = [] 
for phonenumber in extractedphone:
    allphonenumbers.append(phonenumber[0])
print(allphonenumbers)
#print(extractedemail)

#TODO: Copy the extracted email/phone to the clipboard


#(((\d\d\d)|(\(\d\d\d)))?(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))?)