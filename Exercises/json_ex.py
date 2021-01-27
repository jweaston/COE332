import json

def check_char_count(mystr):
    if ( len(mystr) == 2 ):
        return( f'{mystr} count passes' )
    else:
        return( f'{mystr} count FAILS' )

def check_char_type(mystr):
    if (mystr.isalpha() and mystr.isupper()):
        return( f'{mystr} type passes' )
    else:
        return( f'{mystr} type FAILS' )

with open('states.json', 'r') as f:
    states = json.load(f)

for i in range(50):
    print(check_char_count( states['states'][i]['abbreviation']))
    print(check_char_type( states['states'][i]['abbreviation']))
