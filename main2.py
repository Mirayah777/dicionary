test = {"condingal" : 2 ,"is" : 2,"best" : 2,"for" : 2,"coding" : 1}

k = 2
count = 0

for value in test.values():
    if value == k:
        count += 1 

print("frequency of 2 is ",count)
