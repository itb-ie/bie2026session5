num = 1
while num <= 100:
    print(num)
    num = num + 1


# infinite loop with escape mechanism
num = 1
counter = 0
while True:
    print(num)
    counter += 1

    if counter == 10:
        break # break is the escape from loop
