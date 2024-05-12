def listDivs(number):
    list = [1]
    for i in range(2, number//2 +1):
        if number % i == 0:
            list.append(i)
    if number > 1:
        list.append(number)
    return list

print(listDivs(1))
print(listDivs(24))
