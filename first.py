def christmas_tree():
    """Entry point"""
    height = int(input("Input the desired height: "))
    while height <= 3 or height > 19:
    
        if height <= 3:
            height = int(input("Error!! Input a number greater than 3: "))
        else:
            height = int(input("Error!! Input a number lesser than 20: "))
    value = '*'
    ref = 0
    h = height



    while ref < height:
        space = create_space(h + 50)
        print(space + value)
        value = value + '**'
        ref = ref + 1
        h = h - 1
    space = create_space(height + 49)
    print(space + '***')
    print(space + '***')
    print(space + '***')
 
    qn = input("Do you wish to continue? y/n: ")
    if qn == 'y':
        christmas_tree()


def create_space(h):
    """This function creates space before the value"""
    i = 0
    space = ""
    while i < h:
        space = space + " "
        i = i + 1
    return space
christmas_tree()
