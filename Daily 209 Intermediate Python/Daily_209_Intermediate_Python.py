import math, sys

sentence = ''.join(sys.stdin.readline().strip().split())

for i in range(math.floor(math.sqrt(len(sentence))), 1, -1):
    if len(sentence) % i == 0:
        width, height = (i, len(sentence) // i)

print('{}, {}'.format(width, height))

for i in range(height):
    line = sentence[i*width:(i+1)*width]
    if i % 2 == 0:
        print(line)
    else:
        print(line[::-1])