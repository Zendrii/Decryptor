# ask the user for input 
user_input = input('\n\033[92mInput the encrypted text/s to decrypt: ')

# check each character, then:
# if *, change to a
user_input = user_input.replace('*','a')

# if &, change to e
user_input = user_input.replace('&','e')

# if #, change to i
user_input = user_input.replace('#','i')

# if +, chenge to o
user_input = user_input.replace('+','o')

# if !, change to u
user_input = user_input.replace('!','u')

# print the output
print('\nDecrypted text/s: ', '\033[1m', user_input, '\n')