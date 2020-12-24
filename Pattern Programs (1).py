#Pyramid
'''
N = int(input())

for i in range(N):
    print(' ' *(N-i-1) + (i+1)*'* ')

'''

#Inverted Pyramid
'''
N = int(input())

for i in range(N):
    print(' '*i + (N-i)*'* ')
'''

#Right Angle Triangle
'''
N = int(input())

for i in range(N):
    print((i+1)* '* ')
'''

#Inverted Right Angle Triangle-1
'''
N = int(input())

for i in range(N):
    print(' ' * (N-i-1) + (i+1)*'*')
'''

#Inverted Right Angle Triangle-2
'''
N = int(input())

for i in range(N):
    print('* '*(N-i))
'''

#Inverted Right Angle Triangle-3
'''
N = int(input())

for i in range(N):
    print(i * ' ' + (N-i)*'*')
'''

#Hallow Pyramid
'''
N = int(input())

for i in range(N):
    if i==0:
        print(' ' * (N-i-1) + '*')
    elif (i>=1) and (i<N-1):
        print(' ' * (N-i-1) + '*' + i * ' ' + (i-1) * ' ' + '*')
    else:
        print(' ' * (N-i-1) + ((2*N)-1)*'*')
'''
#Inverted Hallow Pyramid
'''
N = int(input())

for i in range(N-1,-1,-1):
    if i==0:
        print(' ' * (N-i-1) + '*')
    elif (i>=1) and (i<N-1):
        print(' ' * (N-i-1) + '*' + i * ' ' + (i-1) * ' ' + '*')
    else:
        print(' ' * (N-i-1) + ((2*N)-1)*'*')
'''
#Diamond
'''
N = int(input())

for i in range(N):
    print(' ' *(N-i-1) + (i+1)*'* ')
N = N-1
for i in range(N):
    print(' '*i + (N-i)*' *')
'''

#Hallow Diamond

'''

N = int(input())

for i in range(N):
    if i==0:
        print(' ' * (N-i-1) + '*')
    elif (i>=1) and (i<N-1):
        print(' ' * (N-i-1) + '*' + i * ' ' + (i-1) * ' ' + '*')
    
N = N-1
for i in range(N-1,-1,-1):
    if i==0:
        print(' ' * (N-i-1) + ' *')
    elif (i>=1) and (i<N-1):
        print(' ' * (N-i-1) + ' *' + i * ' ' + (i-1) * ' ' + '*')
    
'''

#Half Hallow Diamond
'''
N = int(input())

for i in range(N):
    if i==0:
        print(' ' * (N-i-1) + '*')
    elif (i>=1) and (i<N-1):
        print(' ' * (N-i-1) + '*' + i * ' ' + (i-1) * ' ' + '*')
'''
#Half Diamond - Left
'''
N = int(input())

for i in range(N):
    print((i+1)* '* ')
N = N-1
for i in range(N):
    print('* '*(N-i))
'''

#Half Diamond - Right
'''
N = int(input())

for i in range(N):
    print(' ' * (N-i-1) + (i+1)*'*')
N = N-1

for i in range(N):
    print((i+1) * ' ' + (N-i)*'*')
'''
