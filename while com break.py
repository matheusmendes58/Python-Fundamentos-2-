n = 0
s = 0
while True:
    n = int(input('digite um numero'))
    if n == 999:
        break
    s = s + n
print(s)
# print com f string funcionamento python 3.6+
print(f'a soma é {s}')
