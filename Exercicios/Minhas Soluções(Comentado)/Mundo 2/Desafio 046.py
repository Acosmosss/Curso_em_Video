import time
import emoji

print('Contagem Regressiva para os fogos de artificio')
time.sleep(0.8)
print('começa em:')
for c in range(10, 0, -1):
    print(c)
    time.sleep(1)
print(emoji.emojize(':fireworks: :fireworks: :sparkler: :sparkler: :fireworks: :fireworks:'))
