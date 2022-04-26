def divide_five(num):
    try:
         value= 5/num
    except ZeroDivisionError:
        print('divide by zero error')
        value="Sorry use another number"
    return value


print(divide_five(2))
print (divide_five(0))