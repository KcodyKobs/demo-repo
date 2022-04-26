myfavoritefoods= ['banku','banku', 'rice','beans','fufu']
#print (myfavoritefoods[0])
#to add to a list using the APPEND function
myfavoritefoods.append('omena')
#print(myfavoritefoods)
myfavoritefoods.append('yam')
mylists =myfavoritefoods


#adding an item to a list at a particular point in the list using INSERT
mylists.insert(0,'gari')
#print(mylists)

mymusiclists=['hiplife','afrobeat','hippop']


#adding two differnt lists using EXTEND
myfavoritefoods.extend(mymusiclists)
#print(myfavoritefoods)

#removing an item from a list using POP()
#myfavoritefoods.pop(1)
#print(myfavoritefoods)

#using the DEL function
#del myfavoritefoods[3]
#print(myfavoritefoods)


#using the FOR LOOP (looping through a list)
#for item in myfavoritefoods:
    #print(item)

#number of items in a list using len()
#print (len(myfavoritefoods))

#SORTING

#myfavoritefoods.sort()

#in sorting , space and uppercase have precedence over lowercase
#reverse sorting
myfavoritefoods.sort(reverse=True)

#print(myfavoritefoods)

#sorting numbers
mynumbers=[2,4,3,5,56,7,6,12]
print(mynumbers)
mynumbers.sort()
print(mynumbers)
mynumbers.sort(reverse=True)
print(mynumbers)