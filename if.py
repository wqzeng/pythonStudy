age=5
print('your age is:',age)
if age>=18:
    print('adult')
elif age>=6:
    print('teenager')    
else:
    print('kid')

age=input('enter your age:')
#需要转换int
age=int(age)
if age>=18:
    print('adult')
elif age>=6:
    print('teenager')    
else:
    print('kid')    