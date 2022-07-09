total = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        total = cont + total
        print(cont)
print(total)