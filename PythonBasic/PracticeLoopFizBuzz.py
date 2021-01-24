'''
Below are requirements
- repeat the process n times
- print 'fizz' at multiplier of 3
- print 'buzz" at the multiplier of 5
- print numbers for other items
'''

# end=' ' in print() changes the statement for: I am replacing from \r\n to ' '
for i in range(1, 100):
    message =''
    if i % 3 == 0:
        message += 'fizz'
    if i % 5 == 0:
        message += 'buzz'

    # if message:
    #     print(message, end=' ')
    # else:
    #     print(i, end=' ')
    print(message or i, end=' ')
