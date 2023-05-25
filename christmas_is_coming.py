n = 27

# print upside down christmas tree
for i in range(n, 0, -1):
    print(' ' * (n-i), end = '')
    print('*' * (2*i -1))

# print normal christmas tree

for i in range(1,n+1):
    print(' ' * (n-i), end = '')
    print('*' * (2*i- 1) , end = '')
    print('')