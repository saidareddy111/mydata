'''
Created on Jun 30, 2015

@author: harika
'''
def pyramid(rows=8):
    for i in range(rows):
        print ' '*(rows-i-1) + '#'*(2*i+1)
        

pyramid(4)

"""

def row(n):
    return list(reversed(range(2, n+1))) + list(range(1, n+1))


for n in range(1, 5):
    print(row(n))
    
    
    """