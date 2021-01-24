'''
while Assertion A:
    process a
'''
print('while statement by count')
count = 0
while count <= 10:
    print('current count is: ', count)
    count += 1
print('*******')

print('while statement by input()')
flg = True
while flg:
    user_input = input()
    if user_input == 'exit':
        flg = False
print('*******')

'''
break = terminate the process/loop
continue = do not continue to successive processes and go back to beginning (of the loop)
'''
print('while statements with break/continue')
while True:
    exInput = input()
    if exInput == 'exit':
        break
    elif exInput == 'skip':
        continue
    message = 'Your inserted value is: {0}'.format(exInput)
    print(message)
