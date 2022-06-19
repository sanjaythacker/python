# ****************************************************
# Sanjay N Thacker
# sanjaythacker@hotmail.com
# ****************************************************
# The Fizz Buzz coding example:
# https://k3no.medium.com/fizz-buzz-in-python-2edea331d715

# Problem: Find all numbers between 1 and 100 that are
# 1. divisible by 3 only
# 2. divisible by 5 only
# 3. divisible by both 3 and 5

for i in range(1, 101):
    # print(i)
    if (i % 3 == 0) and (i % 5 == 0):
        print(i, ' is a multiple of both 3 and 5')
    elif i % 3 == 0:
        print(i, ' is a multiple of 3')
    elif i % 5 == 0:
        print(i, ' is a multiple of 5')
    else:
        print(i)
