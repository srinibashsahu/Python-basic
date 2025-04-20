def reminder_division(a,b):
    if b==0:
        raise Exception('deviser can not be zero')
    result=a//b
    reminder= a%b
    return reminder


acrnyms = {'LOL': 'lough out loud',
           'EOF': 'End of file',
           'EOD':'end of the day'}
try:
    defination = acrnyms['BTW']
except:
    print("key word does not exist")
finally:
    print(acrnyms)


print("programm keep running ")
reminder_division(10,0)