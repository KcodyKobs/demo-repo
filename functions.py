# a piece code which usable and used to performa specific function
#there are two types are user defined and pro
#area of 

def demo(r):
    '''this funtion retuns the area of a circle
       Args:
       r(int): the radius of the circle'''
    pi=3.142
    y=pi *r**2
    return y

rad=int(input('please enter a number'))
print (demo(rad))