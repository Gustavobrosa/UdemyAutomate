import re, pyperclip
pyperclip.copy('''Ken Dawson868-388-6332gefcnxvuo28@gmail.comRoland Buck809-571-4553rbuck46@verizon.netJeffery Bray704-894-9878jbray68@optonline.netAlfred Britt714-915-5120abritt10@msn.comMike Howell671-514-2487mhowell@sbcglobal.netCedric Harrell848-959-8580charrell@gmail''')

#Create a regex for phone numbers
phoneRegex = re.compile(r'(((\d\d\d)|(\(\d\d\d))(\s|-)\d\d\d-\d\d\d\d(((ext(\.)?\s)|x)(\d{2,5}))?)', re.VERBOSE)

#Create a regex for e-mail address
emailRegex = re.compile(r'@')


#Get text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedphone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)

allphonenumbers = [] 

print(extractedphone)
print(extractedemail)

#TODO: Copy the extracted email/phone to the clipboard
