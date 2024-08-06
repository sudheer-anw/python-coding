print('wellcome to the rollercoster ride!')
name = input('what is your name? : ')

height = int(input('enter your height? : '))
bill = 0
if height >= 120:
    print('yes you can have a ride')
    age = int(input('enter your age : '))
    if age < 12:
        bill = 50
        print('childrens ticket prise is 50 rupees')
    elif age <= 18:
        bill = 100
        print('teenage ticket is 100 rupees')
    elif age >= 45:
        print('to the seniour citizens this ride is for free')
    else:
        bill = 120
        print('adult ticket prise is 120 rupees')
    want_photo = input('do you want photo? yes or no : ')
    if want_photo == 'yes':
        bill+=3
        print(f'your final bill is : {bill} ')
else:
    print('sorry! you are not able to have this ride')

print(f'have a safe ride dear {name}')












