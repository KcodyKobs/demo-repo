#Collecting user input for size of tree
# arg lines=integer
lines= int(input('how big do you want to your tree to be?'))

#multipying user number by 2 and subtracting 1 to get an odd number
length= (lines *2 -1)
spaces = int((length -1)/2)
i=1

for i in range(1,lines+1):
    print (" "*(spaces -i + (5*10 )) + '*'*(2*i-1))
    i=i+1



for i in range(1,lines-1):
    print (" "*(spaces -i+(2*24) -1) + '*'*(2*(i+2)+1))
    i=i+1



for i in range(1,lines-1):
    print (" "*(spaces +(3*16) ) + '***')
   