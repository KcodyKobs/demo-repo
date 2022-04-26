import json

filename = 'userdetails.json'
name= ''

try:

    with open(filename,'r') as r:
        name= json.load(r)
except IOError:
    print('first-time login')


if name != '':
    print ('welcome back' + name + '!')
else:
    name= input("Hello! What's your name? ")
    print('welcome'+ name+ '!')