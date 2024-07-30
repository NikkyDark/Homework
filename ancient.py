def code(c):
    result = ""
    for i in range(1, c):
        for j in range(i + 1, c):
           if c % (i + j) == 0:
               result = result + str(i) + str(j)

    return result

for c in range(3,21):
    print(c, code(c))

