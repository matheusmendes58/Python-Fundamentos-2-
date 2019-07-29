import emoji
from time import sleep
for c in range(10, 0, -1):
    sleep(0.5)
    print(c)
print('Booom')
print(emoji.emojize(':fireworks:' * 50, use_aliases=True))

