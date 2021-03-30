# This program says hello and ask for your name and age.

print ('Hello World')

print ('Whats is your name? ') # ask for their name
myName = input()
print ('It is good to meet you, ' + myName)
print ('The length of your name is : ')
print (len(myName))

print ('{}, what is your age?'.format(myName)) # ask for their name
myAge = input()
print ('{}, you will be {} in a year'.format(myName, str(int(myAge)+1)))