#christmas tree
lines= int(input('how big do you want to your tree to be?'))

#
length= (lines *2 -1)
spaces = int((length -1)/2)
i=1

# while i<=lines:
#     print (" "*(spaces -i + 1 ) + '*'*(2*i-1))
#     i=i+1


# i=1
# while i<lines:
#     print (" "*(spaces -i+2 ) + '*'*(2*(i+2)+1))
#     i=i+1



# i=1
# while i<(lines):
#     print (" "*(spaces +4 ) + '*')

while i<=lines:
    print (" "*(spaces -i + 5 ) + '*'*(2*i-1))
    i=i+1



for i in range(1,lines-1):
    print (" "*(spaces -i+2 ) + '*'*(2*(i+2)+1))
    i=i+1



for i in range(1,lines-1):
    print (" "*(spaces +4 ) + '*')
   