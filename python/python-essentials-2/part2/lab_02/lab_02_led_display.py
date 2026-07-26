#  File name: lab_led_display.py
#  Description: A possible solution for the 'YA LED Display' LAB from Python Essentials 2
#  Author: Ana Paula da Silva Souza
#  Date: 2026-07-26
#  Version: 1.0
#  License: Apache
#

def leddisplay(snumber):
    # string with numer in leds
    lednumbers =[   ['### ',
                     '# # ',
                     '# # ',
                     '# # ',
                     '### '    
                    ],
                    ['  # ',
                     '  # ',
                     '  # ',
                     '  # ',
                     '  # ' 
                    ],
                    ['### ',
                     '  # ',
                     '### ',
                     '#   ',
                     '### ',
                    ],
                    ['### ',
                     '  # ',
                     '### ',
                     '  # ',
                     '### ',
                    ],
                    ['# # ',
                     '# # ',
                     '### ',
                     '  # ',
                     '  # '
                    ],
                    ['### ',
                     '#   ',
                     '### ',
                     '  # ',
                     '### '
                    ],
                    ['### ',
                     '#   ',
                     '### ',
                     '# # ',
                     '### '    
                    ],
                    ['### ',
                     '  # ',
                     '  # ',
                     '  # ',
                     '  # ' 
                    ],
                    ['### ',
                     '# # ',
                     '### ',
                     '# # ',
                     '### '    
                    ],
                    ['### ',
                     '# # ',
                     '### ',
                     '  # ',
                     '### '    
                    ]
                ]
    numbers = []
    for c in snumber:
        i = int(c)
        numbers.append(i)
    s = ''
    for i in range(5):
        for j in numbers:
            s += lednumbers[j][i]
        s += '\n'
    return(s)
    



#leddisplay(input())
