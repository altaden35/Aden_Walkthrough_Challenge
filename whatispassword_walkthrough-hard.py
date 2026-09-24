#Hard challenge - Inspired by buffer overflow 
from nth import nth1, actual_password

import base64
print('CLEARANCE: LEVEL III')
print('FACILITY: KPA SOF command bunker')
print('AUTHENTICATION METHOD:PASSWORD ')
print('')
user_input = input('Enter the bunker password: ')

while user_input != '':
    if user_input != actual_password: 
        print('=== ACCESS DENIED ===')
        actual_password = user_input
        user_input = input('Enter your password: ')

        
    else:
        print('=== ACCESS GRANTED ===') 
        print('Heres your flag:',base64.b64decode(nth1).decode())
        break
print('')
print('=== WARNING ===')
print('Turn it back on now or face charges.')
print('Turning of the bunker authentication system is againts North Korean military law.')
print('=== WARNING ===')