y = 0
c = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        y = y + 1
        c = x + c
print('a soma de {} valores solicitados é {} '.format(y, c))




