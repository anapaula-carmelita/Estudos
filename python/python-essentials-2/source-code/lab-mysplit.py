#
#  File name: mysplit.py
#  Description: A possible solution for the 'Your own split' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-17
#  Version: 1.0
#  License: Apache
#

def mysplit(strng):
    strng = strng.strip()
    word_list = [] 
    
    if strng == '':
        return word_list

    s =''
    for c in strng:
        if c == ' ':
            if s != '':
                word_list.append(s)
            s = ''
            continue
        s += c
    if s != '':
        word_list.append(s)
    return word_list

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To    be or not to be,that is the question"))
print(mysplit(" "))
print(mysplit(" abc "))
print(mysplit(""))