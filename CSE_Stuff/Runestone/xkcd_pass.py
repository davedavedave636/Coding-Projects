letters = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

# Make an 8 letter password by combining characters from the three strings
import random
x = letters + caps + numbers
p = ''
for _ in range (8):
    z = x[random.randint(0,61)]
    p = p + z
print(p)
