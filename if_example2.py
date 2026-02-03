# if + else
import random

num = random.randint(1, 10)
print("random number is", num)
# check for odd
if not num % 2:
    print("number",num,"is even")
else:
    print("number",num,"is odd")
    print("this only shows for odd numbers")
print("this shows always: thanks for playing")