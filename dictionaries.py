#it a collection that has a key and a value. it uses {}

peopleandtheircolors={'Gideon': 'blue', 'Sonia':'aquamarine', 'Susan':'gold', 'Kafui':'indigo'}
print(peopleandtheircolors['Gideon'])
print(peopleandtheircolors['Sonia'])

# #using the get command

# theircolors=peopleandtheircolors.get('Kafui')
# print (theircolors)

#adding items to a dictionary
peopleandtheircolors['Ibrahim'] ='pink'
peopleandtheircolors['Edward'] ='red'
print(peopleandtheircolors)

#to use the get command you have to pass it to a variable
theircolors= peopleandtheircolors.get('Ibrahim')
print(theircolors)
theircolors= peopleandtheircolors.get('Edward')
print(theircolors)