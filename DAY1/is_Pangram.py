'''import string'''


def is_pangram(str: object) -> object:
    '''

    :return:
    :type str: object
    :rtype: object
    '''
    alphabet:str="abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
        return True


string:str='helllooo world'
if is_pangram(string):
    print("Given string is pangram")
else:
    print("given string is not pangram")
