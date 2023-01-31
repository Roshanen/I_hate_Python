answer = 0
for i in range(100, 999):
    for j in range(100, 999):
        try_number = i * j
        test = str(try_number)
        if (test == test[::-1]) and (try_number > answer):
            answer = try_number
print(answer)
